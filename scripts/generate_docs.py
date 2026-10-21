#!/usr/bin/env python3
"""Generate one Jekyll page per hook/feature from plugin DOCS.md sources."""

from __future__ import annotations

import re
import shutil
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "_source"


@dataclass
class DocPage:
    """One documentation page to write."""

    plugin: str
    plugin_name: str
    doc_type: str  # filter | action | javascript | shortcode | guide | feature | rest
    slug: str
    title: str
    summary: str
    body: str
    category: str = ""
    heading_is_code: bool = True

    @property
    def rel_dir(self) -> Path:
        type_dirs = {
            "filter": "filters",
            "action": "actions",
            "javascript": "javascript",
            "shortcode": "shortcodes",
            "guide": "guides",
            "feature": "features",
            "rest": "rest",
        }
        return Path(self.plugin) / type_dirs[self.doc_type]

    @property
    def url_path(self) -> str:
        return f"/{self.rel_dir.as_posix()}/{self.slug}/"


TYPE_LABELS = {
    "filter": "PHP filter",
    "action": "PHP action",
    "javascript": "JavaScript API",
    "shortcode": "Shortcode",
    "guide": "Guide",
    "feature": "Feature",
    "rest": "REST API",
}

TYPE_LIST_URL = {
    "filter": "filters",
    "action": "actions",
    "javascript": "javascript",
    "shortcode": "shortcodes",
    "guide": "guides",
    "feature": "features",
    "rest": "rest",
}


def yaml_escape(value: str) -> str:
    """Escape a string for double-quoted YAML."""
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def liquid_url(path: str) -> str:
    """Emit a Liquid path that respects site.baseurl on GitHub Pages."""
    return "{{ '" + path + "' | relative_url }}"


def first_paragraph(text: str) -> str:
    """Return the first non-empty prose paragraph as a short summary."""
    chunks = re.split(r"\n\s*\n", text.strip())
    for chunk in chunks:
        clean = chunk.strip()
        if not clean or clean.startswith("|") or clean.startswith("```") or clean.startswith("#"):
            continue
        # Skip markdown tables that lack a blank line before the first row
        if clean.startswith("|") or re.match(r"^\|", clean, re.M):
            continue
        # Strip links / emphasis without destroying snake_case identifiers
        clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", clean)
        clean = clean.replace("`", "")
        clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", clean)
        clean = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"\1", clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        clean = re.sub(r"^[-*]\s+", "", clean)
        # Prefer a real sentence over a leftover table fragment
        if clean.startswith("|") or clean.count("|") >= 3:
            continue
        if clean:
            return clean[:220] + ("…" if len(clean) > 220 else "")
    return ""


def rewrite_internal_links(body: str, pages_by_hook: dict[str, DocPage], plugin: str) -> str:
    """Rewrite markdown anchors like (#scry_ms_foo) to generated page URLs."""

    def repl(match: re.Match[str]) -> str:
        label, anchor = match.group(1), match.group(2)
        # strip leading #
        key = anchor.lstrip("#")
        # normalize common anchors
        key = key.replace("frontend-windowscrysearch-upgrade", "window-scrysearch-upgrade")
        if key in pages_by_hook:
            return f"[{label}]({liquid_url(pages_by_hook[key].url_path)})"
        # try slugify
        slug = slugify(key)
        for page in pages_by_hook.values():
            if page.slug == slug and page.plugin == plugin:
                return f"[{label}]({liquid_url(page.url_path)})"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\((#[^)]+)\)", repl, body)


def slugify(value: str) -> str:
    """URL-safe slug."""
    value = value.strip().lower()
    value = value.replace("`", "")
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[-\s]+", "-", value)
    return value.strip("-")


def split_sections(markdown: str, pattern: str) -> list[tuple[str, str]]:
    """Split markdown on heading pattern; return (heading_text, body) pairs."""
    out: list[tuple[str, str]] = []
    # ^/$ must match line boundaries inside the document body
    matches = list(re.finditer(pattern, markdown, flags=re.MULTILINE))
    if not matches:
        return out
    for i, match in enumerate(matches):
        heading = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        body = markdown[start:end].strip()
        # trim trailing horizontal rules
        body = re.sub(r"\n---\s*$", "", body).strip()
        out.append((heading, body))
    return out


def extract_between(markdown: str, start_heading: str, end_heading: str | None = None) -> str:
    """Extract content from a ## heading until the next ## or end_heading."""
    start = markdown.find(start_heading)
    if start < 0:
        return ""
    rest = markdown[start + len(start_heading) :]
    if end_heading:
        end = rest.find(end_heading)
        if end >= 0:
            return rest[:end].strip()
    # stop at next ## at beginning of line
    m = re.search(r"\n## ", rest)
    if m:
        return rest[: m.start()].strip()
    return rest.strip()


def parse_scry_search(md: str) -> list[DocPage]:
    """Parse base plugin DOCS.md into pages."""
    pages: list[DocPage] = []
    plugin = "scry-search"
    plugin_name = "Scry Search"

    # Guides from top matter
    naming = extract_between(md, "## Hook naming", "## Plugin lifecycle")
    if naming:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "hook-naming",
                "Hook naming",
                "Every PHP hook is namespaced with the scry_ms_ prefix.",
                naming,
                category="Basics",
                heading_is_code=False,
            )
        )

    lifecycle = extract_between(md, "## Plugin lifecycle", "## PHP Filters")
    if lifecycle:
        # drop the WP conventions reminder into its own page if present
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "plugin-lifecycle",
                "Plugin lifecycle",
                "What happens on deactivation and uninstall.",
                lifecycle.split("A quick reminder")[0].strip(),
                category="Basics",
                heading_is_code=False,
            )
        )
        if "A quick reminder" in lifecycle:
            reminder = "A quick reminder" + lifecycle.split("A quick reminder", 1)[1]
            pages.append(
                DocPage(
                    plugin,
                    plugin_name,
                    "guide",
                    "wordpress-hook-conventions",
                    "WordPress hook conventions",
                    "Filters return values; actions are for side effects.",
                    reminder,
                    category="Basics",
                    heading_is_code=False,
                )
            )

    # Filters section: track ### categories and #### hooks
    filters_block = extract_between(md, "## PHP Filters", "## PHP Actions")
    current_category = "General"
    # Walk line by line to keep category context
    filter_chunks: list[tuple[str, str, str]] = []
    lines = filters_block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("### "):
            current_category = line[4:].strip()
            i += 1
            continue
        m = re.match(r"^#### `([^`]+)`\s*$", line)
        if m:
            name = m.group(1)
            i += 1
            body_lines: list[str] = []
            while i < len(lines):
                if re.match(r"^#### `", lines[i]) or lines[i].startswith("### "):
                    break
                body_lines.append(lines[i])
                i += 1
            body = "\n".join(body_lines).strip()
            body = re.sub(r"\n---\s*$", "", body).strip()
            filter_chunks.append((name, current_category, body))
            continue
        i += 1

    for name, category, body in filter_chunks:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "filter",
                slugify(name),
                name,
                first_paragraph(body),
                body,
                category=category,
            )
        )

    # Actions
    actions_block = extract_between(md, "## PHP Actions", "## JavaScript API")
    for heading, body in split_sections(actions_block, r"^#### `([^`]+)`\s*$"):
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "action",
                slugify(heading),
                heading,
                first_paragraph(body),
                body,
                category="Lifecycle",
            )
        )

    # JavaScript API subsections under ### 
    js_block = extract_between(md, "## JavaScript API", None)
    # Intro paragraph as overview page
    intro_end = re.search(r"\n### ", js_block)
    intro = js_block[: intro_end.start()].strip() if intro_end else ""
    if intro:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "javascript",
                "overview",
                "JavaScript runtime overview",
                first_paragraph(intro),
                intro,
                category="Runtime",
                heading_is_code=False,
            )
        )

    js_sections = {
        "Form discovery": (
            "form-discovery",
            "Form discovery",
            "Runtime",
            "How the runtime finds <form> elements and wraps them as ScrySearch_SearchForm instances.",
        ),
        "Readiness: the `scrySearchReady` event": (
            "scrysearchready",
            "scrySearchReady",
            "Runtime",
            "Event dispatched on document after forms are discovered — wait for this before using the API.",
        ),
        "`window.scrySearch`": (
            "window-scrysearch",
            "window.scrySearch",
            "Runtime",
            "Global runtime object: version, form getters, and registerUpgrade().",
        ),
        "`ScrySearch_SearchForm`": (
            "scrysearch-searchform",
            "ScrySearch_SearchForm",
            "Runtime",
            "Per-form wrapper with submit/submitAjax and ordered pre/post action hooks.",
        ),
        "The pre/post submit action pipeline": (
            "submit-action-pipeline",
            "Submit action pipeline",
            "Runtime",
            "Ordered pre/post actions for normal and AJAX submits.",
        ),
        "Upgrades": (
            "upgrades",
            "Upgrades",
            "Runtime",
            "Reserve a namespace on window.scrySearch.upgrades for premium add-ons.",
        ),
        "Front‑end configuration via `windowLocalized`": (
            "windowlocalized",
            "windowLocalized",
            "Runtime",
            "PHP-localized config object read by the front-end runtime.",
        ),
        "Front-end configuration via `windowLocalized`": (
            "windowlocalized",
            "windowLocalized",
            "Runtime",
            "PHP-localized config object read by the front-end runtime.",
        ),
    }

    for heading, body in split_sections(js_block, r"^### (.+?)\s*$"):
        # skip nested #### inside form discovery — keep whole ### sections
        meta = js_sections.get(heading)
        if not meta:
            slug = slugify(heading.replace("`", ""))
            title = heading.replace("`", "")
            category = "Runtime"
            summary = first_paragraph(body)
        else:
            slug, title, category, summary = meta
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "javascript",
                slug,
                title,
                summary or first_paragraph(body),
                body,
                category=category,
                heading_is_code=title.startswith("window") or title.startswith("ScrySearch") or title == "scrySearchReady" or title == "windowLocalized",
            )
        )

    return pages


def parse_scry_search_filters(md: str) -> list[DocPage]:
    """Parse Filters upgrade DOCS.md into pages."""
    pages: list[DocPage] = []
    plugin = "scry-search-filters"
    plugin_name = "Scry Search Filters"

    # Intro guide
    intro = md.split("## Quick reference")[0]
    # strip title
    intro = re.sub(r"^# .+\n+", "", intro).strip()
    if intro:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "overview",
                "Filters upgrade overview",
                first_paragraph(intro),
                intro,
                category="Basics",
                heading_is_code=False,
            )
        )

    # Shortcode section
    shortcode = extract_between(md, "## Shortcode: `[scry-search-facets]`", "## Frontend:")
    if not shortcode:
        shortcode = extract_between(md, "## Shortcode: `[scry-search-facets]`", "## Frontend")
    if shortcode:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "shortcode",
                "scry-search-facets",
                "[scry-search-facets]",
                "Renders a facet form that syncs into Scry Search forms on submit.",
                shortcode,
                category="Shortcodes",
                heading_is_code=True,
            )
        )

    # Frontend upgrade
    frontend = extract_between(md, "## Frontend: `window.scrySearch` upgrade", "## Search")
    if frontend:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "javascript",
                "window-scrysearch-upgrade",
                "window.scrySearch filters upgrade",
                first_paragraph(frontend),
                frontend,
                category="Runtime",
                heading_is_code=False,
            )
        )

    # Hook sections: ## Search / ## Shortcode script / ## Excluded / ## Analytics
    search_block = extract_between(md, "## Search", "## Shortcode script localization")
    for heading, body in split_sections(search_block, r"^### (.+?)\s*$"):
        hook = re.match(r"`([^`]+)`", heading)
        if hook:
            pages.append(
                DocPage(
                    plugin,
                    plugin_name,
                    "filter",
                    slugify(hook.group(1)),
                    hook.group(1),
                    first_paragraph(body),
                    body,
                    category="Search",
                )
            )
        elif "built-in" in heading.lower():
            pages.append(
                DocPage(
                    plugin,
                    plugin_name,
                    "guide",
                    "built-in-filter-construction",
                    "Built-in filter construction",
                    first_paragraph(body),
                    body,
                    category="Search",
                    heading_is_code=False,
                )
            )

    for section_title, category in [
        ("## Shortcode script localization", "Shortcode"),
        ("## Excluded taxonomies", "Catalog"),
        ("## Analytics", "Analytics"),
    ]:
        block = extract_between(md, section_title, None)
        for heading, body in split_sections(block, r"^### `([^`]+)`\s*$"):
            pages.append(
                DocPage(
                    plugin,
                    plugin_name,
                    "filter",
                    slugify(heading),
                    heading,
                    first_paragraph(body),
                    body,
                    category=category,
                )
            )

    # Guides at the end
    flow = extract_between(md, "## Typical customization flow", "## Notes")
    if flow:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "customization-flow",
                "Typical customization flow",
                "Shortcode, custom Meilisearch filters, and generator catalog tips.",
                flow,
                category="Guides",
                heading_is_code=False,
            )
        )

    notes = extract_between(md, "## Notes", None)
    if notes:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "notes",
                "Notes & unsupported surfaces",
                first_paragraph(notes),
                notes,
                category="Guides",
                heading_is_code=False,
            )
        )

    return pages


def parse_scry_search_ajax(md: str) -> list[DocPage]:
    """Parse Ajax upgrade DOCS.md into pages."""
    pages: list[DocPage] = []
    plugin = "scry-search-ajax"
    plugin_name = "Scry Search Ajax"

    # Intro / prefixes
    intro = md.split("## REST API")[0]
    intro = re.sub(r"^# .+\n+", "", intro).strip()
    if intro:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "overview",
                "Ajax upgrade overview",
                "Premium add-on hooks use scry_ms_aj_; shared main-plugin hooks keep the scry_ms_ prefix.",
                intro,
                category="Basics",
                heading_is_code=False,
            )
        )

    # REST endpoint (one route)
    rest = extract_between(md, "## REST API", "## Filters (this plugin)")
    if rest:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "rest",
                "post-search",
                "POST /wp-json/scry-search-ajax/v1/search",
                "Federated Meilisearch search used by the [scry-search-ajax] shortcode.",
                rest,
                category="REST",
                heading_is_code=True,
            )
        )

    # This plugin's filters
    filters_block = extract_between(md, "## Filters (this plugin)", "## Shared / main-plugin hooks used by this plugin")
    for heading, body in split_sections(filters_block, r"^### `([^`]+)`\s*$"):
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "filter",
                slugify(heading),
                heading,
                first_paragraph(body),
                body,
                category="Ajax search",
            )
        )

    # Shared main-plugin hooks (guide + pages for hooks unique to this DOCS)
    shared = extract_between(md, "## Shared / main-plugin hooks used by this plugin", "## Frontend:")
    if not shared:
        shared = extract_between(md, "## Shared / main-plugin hooks used by this plugin", "## Frontend")
    if shared:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "guide",
                "shared-main-plugin-hooks",
                "Shared main-plugin hooks",
                first_paragraph(shared),
                shared,
                category="Integration",
                heading_is_code=False,
            )
        )
        consumed = extract_between(shared, "### Consumed (listen)", None)
        for heading, body in split_sections(consumed, r"^#### `([^`]+)`"):
            # Drop the leftover "*(filter)*" / "*(action)*" marker from the heading line
            body = re.sub(r"^\s*\*\([^)]+\)\*\s*", "", body).strip()
            if heading == "scry_ms_premium_upgrade_settings_ui":
                doc_type = "action"
            elif heading == "scry_ms_premium_upgrades_display":
                doc_type = "filter"
            else:
                doc_type = "filter"
            pages.append(
                DocPage(
                    plugin,
                    plugin_name,
                    doc_type,
                    slugify(heading),
                    heading,
                    first_paragraph(body),
                    body,
                    category="Integration",
                )
            )

    # Frontend runtime
    frontend = extract_between(md, "## Frontend: `window.scrySearch` upgrade", None)
    intro_end = re.search(r"\n### ", frontend) if frontend else None
    frontend_intro = frontend[: intro_end.start()].strip() if intro_end else ""
    if frontend_intro:
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "javascript",
                "overview",
                "Ajax JavaScript runtime",
                first_paragraph(frontend_intro),
                frontend_intro,
                category="Runtime",
                heading_is_code=False,
            )
        )

    js_sections = {
        "Base runtime (from main plugin)": (
            "base-runtime",
            "Base runtime",
            "Runtime",
            "Pieces of window.scrySearch that this add-on uses.",
            False,
        ),
        "Registration": (
            "registration",
            "Upgrade registration",
            "Runtime",
            "How the ajax upgrade registers on scrySearchReady and wraps matching forms.",
            False,
        ),
        "Localized `scrySearchAjax`": (
            "scrysearchajax",
            "scrySearchAjax",
            "Runtime",
            "Localized object for the Ajax shortcode script (filterable via scry_ms_aj_ajax_localized).",
            True,
        ),
        "`ScrySearchAjax_SearchForm`": (
            "scrysearchajax-searchform",
            "ScrySearchAjax_SearchForm",
            "Runtime",
            "Per-form controller for pagination, federation hidden inputs, and results rendering.",
            True,
        ),
        "Pre / post AJAX actions registered": (
            "ajax-action-pipeline",
            "Ajax action pipeline",
            "Runtime",
            "Pre/post AJAX actions this add-on registers on each wrapped search form.",
            False,
        ),
        "Extending from custom JS": (
            "extending-from-custom-js",
            "Extending from custom JS",
            "Runtime",
            "Hook your own post-AJAX actions after the Ajax upgrade has registered.",
            False,
        ),
    }

    for heading, body in split_sections(frontend, r"^### (.+?)\s*$"):
        meta = js_sections.get(heading)
        if meta:
            slug, title, category, summary, heading_is_code = meta
        else:
            slug = slugify(heading.replace("`", ""))
            title = heading.replace("`", "")
            category = "Runtime"
            summary = first_paragraph(body)
            heading_is_code = title.startswith("window") or title.startswith("ScrySearch")
        pages.append(
            DocPage(
                plugin,
                plugin_name,
                "javascript",
                slug,
                title,
                summary or first_paragraph(body),
                body,
                category=category,
                heading_is_code=heading_is_code,
            )
        )

    return pages


def write_page(page: DocPage) -> Path:
    """Write a single doc markdown file with front matter."""
    out_dir = ROOT / page.rel_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{page.slug}.md"

    type_url = f"/{page.plugin}/{TYPE_LIST_URL[page.doc_type]}/"
    plugin_url = f"/{page.plugin}/"
    heading_line = ""
    # layout uses page.heading if set
    fm_heading = ""
    if not page.heading_is_code:
        fm_heading = f'heading: "{yaml_escape(page.title)}"\n'

    content = f"""---
layout: doc
title: "{yaml_escape(page.title)}"
{fm_heading}summary: "{yaml_escape(page.summary)}"
plugin: {page.plugin}
plugin_name: "{page.plugin_name}"
plugin_url: "{plugin_url}"
doc_type: {page.doc_type}
doc_type_label: "{TYPE_LABELS[page.doc_type]}"
type_url: "{type_url}"
category: "{yaml_escape(page.category)}"
---

{page.body.strip()}
"""
    path.write_text(content, encoding="utf-8")
    return path


def write_list_page(
    plugin: str,
    plugin_name: str,
    doc_type: str,
    pages: list[DocPage],
) -> None:
    """Write a list/index page for a plugin + type."""
    folder = TYPE_LIST_URL[doc_type]
    out = ROOT / plugin / folder / "index.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    by_category: dict[str, list[DocPage]] = defaultdict(list)
    for p in sorted(pages, key=lambda x: (x.category, x.title.lower())):
        by_category[p.category or "General"].append(p)

    sections: list[str] = []
    for category, items in by_category.items():
        rows = []
        for item in items:
            rows.append(
                f"| [`{item.title}`]({liquid_url(item.url_path)}) | {item.summary} |"
                if item.heading_is_code and item.doc_type in {"filter", "action", "shortcode", "rest"}
                else f"| [{item.title}]({liquid_url(item.url_path)}) | {item.summary} |"
            )
        sections.append(
            f"### {category}\n\n| Name | Summary |\n| ---- | ------- |\n" + "\n".join(rows) + "\n"
        )

    # Prefer HTML table with classes for filterable lists of hooks
    use_filter = doc_type in {"filter", "action", "rest"}
    if use_filter:
        body_parts = [
            '<table class="list-table"><thead><tr><th>Name</th><th>Category</th><th>Summary</th></tr></thead><tbody>'
        ]
        for item in sorted(pages, key=lambda x: x.title.lower()):
            name = f"<code>{item.title}</code>" if item.heading_is_code else item.title
            body_parts.append(
                f'<tr><td><a href="{liquid_url(item.url_path)}">{name}</a></td>'
                f"<td>{item.category}</td>"
                f'<td class="muted">{item.summary}</td></tr>'
            )
        body_parts.append("</tbody></table>")
        body = "\n".join(body_parts)
    else:
        body = "\n".join(sections)

    title_overrides = {
        "javascript": f"JavaScript API — {plugin_name}",
        "guide": f"Guides — {plugin_name}",
        "shortcode": f"Shortcodes — {plugin_name}",
        "feature": f"Features — {plugin_name}",
        "filter": f"PHP filters — {plugin_name}",
        "action": f"PHP actions — {plugin_name}",
        "rest": f"REST API — {plugin_name}",
    }
    summary_overrides = {
        "javascript": f"Runtime and front-end API pages for {plugin_name}.",
        "guide": f"Concepts and setup notes for {plugin_name}.",
        "shortcode": f"Shortcode reference for {plugin_name}.",
        "feature": f"Feature pages for {plugin_name}.",
        "filter": f"All PHP filter hooks for {plugin_name}.",
        "action": f"All PHP action hooks for {plugin_name}.",
        "rest": f"REST routes for {plugin_name}.",
    }
    content = f"""---
layout: list
title: "{title_overrides[doc_type]}"
summary: "{summary_overrides[doc_type]}"
plugin: {plugin}
plugin_name: "{plugin_name}"
plugin_url: "/{plugin}/"
doc_type: {doc_type}
doc_type_label: "{TYPE_LABELS[doc_type]}"
list_kind: type
show_filter_search: {str(use_filter).lower()}
---

{body}
"""
    out.write_text(content, encoding="utf-8")


def write_plugin_index(plugin: str, plugin_name: str, pages: list[DocPage], blurb: str) -> None:
    """Write plugin landing page."""
    out = ROOT / plugin / "index.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    counts: dict[str, int] = defaultdict(int)
    for p in pages:
        counts[p.doc_type] += 1

    list_labels = {
        "guide": "Guides",
        "filter": "PHP filters",
        "action": "PHP actions",
        "shortcode": "Shortcodes",
        "javascript": "JavaScript API",
        "feature": "Features",
        "rest": "REST API",
    }
    cards = []
    order = ["guide", "rest", "filter", "action", "shortcode", "javascript", "feature"]
    for doc_type in order:
        if counts.get(doc_type):
            n = counts[doc_type]
            cards.append(
                f"- **[{list_labels[doc_type]}]({liquid_url(f'/{plugin}/{TYPE_LIST_URL[doc_type]}/')})** — {n} page{'s' if n != 1 else ''}"
            )

    # Category breakdown for filters
    filter_cats: dict[str, int] = defaultdict(int)
    for p in pages:
        if p.doc_type == "filter":
            filter_cats[p.category] += 1
    cat_lines = [f"- {cat}: {n}" for cat, n in sorted(filter_cats.items())]

    content = f"""---
layout: list
title: "{plugin_name}"
summary: "{yaml_escape(blurb)}"
plugin: {plugin}
plugin_name: "{plugin_name}"
plugin_url: "/{plugin}/"
list_kind: plugin
show_sidebar: true
---

{blurb}

## Browse by type

{chr(10).join(cards)}

{"## Filter categories" + chr(10) + chr(10) + chr(10).join(cat_lines) if cat_lines else ""}

## Quick links

| Type | Index |
| ---- | ----- |
"""
    for doc_type in order:
        if counts.get(doc_type):
            content += f"| {list_labels[doc_type]} | [View all]({liquid_url(f'/{plugin}/{TYPE_LIST_URL[doc_type]}/')}) |\n"

    out.write_text(content, encoding="utf-8")


def write_home(all_pages: list[DocPage]) -> None:
    """Write site homepage."""
    scry = [p for p in all_pages if p.plugin == "scry-search"]
    filters = [p for p in all_pages if p.plugin == "scry-search-filters"]
    ajax = [p for p in all_pages if p.plugin == "scry-search-ajax"]

    content = f"""---
layout: default
title: Welcome
summary: Developer documentation for Scry Search and premium upgrades.
show_sidebar: true
---

<section class="hero">
  <p class="eyebrow">Developer reference</p>
  <h1>Scry Search Docs</h1>
  <p>
    One page per hook and runtime surface for the open-source
    <a href="https://wordpress.org/plugins/scry-search/">Scry Search</a> plugin
    and its premium upgrades. Hosted Meilisearch lives at
    <a href="https://scrywp.com/">scrywp.com</a>.
  </p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="{liquid_url('/scry-search/')}">Scry Search</a>
    <a class="btn btn-ghost" href="{liquid_url('/scry-search-filters/')}">Filters</a>
    <a class="btn btn-ghost" href="{liquid_url('/scry-search-ajax/')}">Ajax</a>
    <a class="btn btn-ghost" href="{liquid_url('/reference/')}">Browse everything</a>
  </div>
</section>

<div class="plugin-grid">
  <article class="plugin-card">
    <span class="badge">Core plugin</span>
    <h2>Scry Search</h2>
    <p>Meilisearch-powered WordPress search. PHP filters &amp; actions (<code>scry_ms_*</code>) plus the <code>window.scrySearch</code> runtime.</p>
    <div class="meta">
      <span class="badge type-filter">{sum(1 for p in scry if p.doc_type=='filter')} filters</span>
      <span class="badge type-action">{sum(1 for p in scry if p.doc_type=='action')} actions</span>
      <span class="badge type-javascript">{sum(1 for p in scry if p.doc_type=='javascript')} JS pages</span>
    </div>
    <a class="btn btn-primary" href="{liquid_url('/scry-search/')}">Open docs</a>
  </article>

  <article class="plugin-card">
    <span class="badge">Premium upgrade</span>
    <h2>Scry Search Filters</h2>
    <p>Faceted filtering via <code>[scry-search-facets]</code>, Meilisearch filter assembly, analytics payloads, and a <code>window.scrySearch</code> upgrade (<code>scry_ms_fa_*</code>).</p>
    <div class="meta">
      <span class="badge type-filter">{sum(1 for p in filters if p.doc_type=='filter')} filters</span>
      <span class="badge type-shortcode">{sum(1 for p in filters if p.doc_type=='shortcode')} shortcodes</span>
      <span class="badge type-javascript">{sum(1 for p in filters if p.doc_type=='javascript')} JS pages</span>
    </div>
    <a class="btn btn-primary" href="{liquid_url('/scry-search-filters/')}">Open docs</a>
  </article>

  <article class="plugin-card">
    <span class="badge">Premium upgrade</span>
    <h2>Scry Search Ajax</h2>
    <p>In-place results via <code>[scry-search-ajax]</code>, a public REST search route, and a <code>window.scrySearch</code> upgrade (<code>scry_ms_aj_*</code>).</p>
    <div class="meta">
      <span class="badge type-filter">{sum(1 for p in ajax if p.doc_type=='filter')} filters</span>
      <span class="badge type-rest">{sum(1 for p in ajax if p.doc_type=='rest')} REST</span>
      <span class="badge type-javascript">{sum(1 for p in ajax if p.doc_type=='javascript')} JS pages</span>
    </div>
    <a class="btn btn-primary" href="{liquid_url('/scry-search-ajax/')}">Open docs</a>
  </article>
</div>

<section class="section-block" style="margin-top:2.5rem">
  <h2>How this repo is organized</h2>
  <p>Each plugin has its own tree. Inside a plugin, pages are grouped by type (guides, REST, PHP filters, PHP actions, shortcodes, JavaScript API). Future upgrades can add another top-level folder the same way.</p>
</section>
"""
    (ROOT / "index.md").write_text(content, encoding="utf-8")


def write_reference(all_pages: list[DocPage]) -> None:
    """Global alphabetical reference list."""
    out = ROOT / "reference" / "index.md"
    out.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for p in sorted(all_pages, key=lambda x: x.title.lower()):
        name = f"<code>{p.title}</code>" if p.heading_is_code and p.doc_type in {"filter", "action", "shortcode", "rest"} else p.title
        rows.append(
            f'<tr><td><a href="{liquid_url(p.url_path)}">{name}</a></td>'
            f"<td>{p.plugin_name}</td>"
            f"<td>{TYPE_LABELS[p.doc_type]}</td>"
            f"<td>{p.category}</td>"
            f'<td class="muted">{p.summary}</td></tr>'
        )

    content = f"""---
layout: list
title: Full reference
summary: Every generated page across Scry Search and upgrades.
list_kind: reference
show_filter_search: true
---

<table class="list-table">
  <thead>
    <tr>
      <th>Name</th>
      <th>Plugin</th>
      <th>Type</th>
      <th>Category</th>
      <th>Summary</th>
    </tr>
  </thead>
  <tbody>
    {"".join(rows)}
  </tbody>
</table>
"""
    out.write_text(content, encoding="utf-8")


def write_data(all_pages: list[DocPage]) -> None:
    """Write _data/docs.yml for potential Liquid use."""
    lines = ["# Auto-generated by scripts/generate_docs.py", "pages:"]
    for p in sorted(all_pages, key=lambda x: (x.plugin, x.doc_type, x.title.lower())):
        lines.append(f"  - title: \"{yaml_escape(p.title)}\"")
        lines.append(f"    plugin: {p.plugin}")
        lines.append(f"    doc_type: {p.doc_type}")
        lines.append(f"    category: \"{yaml_escape(p.category)}\"")
        lines.append(f"    url: {p.url_path}")
        lines.append(f"    summary: \"{yaml_escape(p.summary)}\"")
    (ROOT / "_data" / "docs.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def clean_generated() -> None:
    """Remove previously generated plugin trees (keep assets/layouts)."""
    for name in ("scry-search", "scry-search-filters", "scry-search-ajax", "reference"):
        path = ROOT / name
        if path.exists():
            shutil.rmtree(path)


def main() -> None:
    clean_generated()

    scry_md = (SOURCE / "scry-search" / "DOCS.md").read_text(encoding="utf-8")
    filters_md = (SOURCE / "scry-search-filters" / "DOCS.md").read_text(encoding="utf-8")
    ajax_md = (SOURCE / "scry-search-ajax" / "DOCS.md").read_text(encoding="utf-8")

    pages = parse_scry_search(scry_md) + parse_scry_search_filters(filters_md) + parse_scry_search_ajax(ajax_md)

    # Build hook lookup for link rewriting
    pages_by_hook: dict[str, DocPage] = {}
    for p in pages:
        pages_by_hook[p.title] = p
        pages_by_hook[p.slug] = p
        pages_by_hook[slugify(p.title)] = p

    # Special alias anchors from Filters / Ajax DOCS
    for p in pages:
        if p.slug == "window-scrysearch-upgrade" and p.plugin == "scry-search-filters":
            pages_by_hook["frontend-windowscrysearch-upgrade"] = p
            pages_by_hook["connecting-to-a-specific-search-form"] = next(
                (x for x in pages if x.slug == "scry-search-facets"), p
            )
        if p.slug == "built-in-filter-construction":
            pages_by_hook["built-in-filter-construction"] = p
        if p.slug == "post-search":
            pages_by_hook["post-wp-jsonscry-search-ajaxv1search"] = p

    for p in pages:
        p.body = rewrite_internal_links(p.body, pages_by_hook, p.plugin)
        write_page(p)

    by_plugin: dict[str, list[DocPage]] = defaultdict(list)
    for p in pages:
        by_plugin[p.plugin].append(p)

    write_plugin_index(
        "scry-search",
        "Scry Search",
        by_plugin["scry-search"],
        "Public extension reference for Scry Search for Meilisearch — PHP filters, actions, and the window.scrySearch JavaScript runtime.",
    )
    write_plugin_index(
        "scry-search-filters",
        "Scry Search Filters",
        by_plugin["scry-search-filters"],
        "Public extension points for Scry Search: Meilisearch Filtered Search. All add-on hooks use the scry_ms_fa_ prefix.",
    )
    write_plugin_index(
        "scry-search-ajax",
        "Scry Search Ajax",
        by_plugin["scry-search-ajax"],
        "Public extension points for Scry Search Ajax — REST search, scry_ms_aj_* filters, and the window.scrySearch ajax upgrade.",
    )

    for plugin, plugin_pages in by_plugin.items():
        plugin_name = plugin_pages[0].plugin_name
        by_type: dict[str, list[DocPage]] = defaultdict(list)
        for p in plugin_pages:
            by_type[p.doc_type].append(p)
        for doc_type, typed in by_type.items():
            write_list_page(plugin, plugin_name, doc_type, typed)

    write_home(pages)
    write_reference(pages)
    write_data(pages)

    print(f"Generated {len(pages)} doc pages.")
    for plugin, plugin_pages in sorted(by_plugin.items()):
        counts = defaultdict(int)
        for p in plugin_pages:
            counts[p.doc_type] += 1
        print(f"  {plugin}: {dict(counts)}")


if __name__ == "__main__":
    main()
