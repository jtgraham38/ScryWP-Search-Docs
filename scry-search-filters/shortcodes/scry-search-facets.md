---
layout: doc
title: "[scry-search-facets]"
summary: "Renders a facet form that syncs into Scry Search forms on submit."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: shortcode
doc_type_label: "Shortcode"
type_url: "/scry-search-filters/shortcodes/"
category: "Shortcodes"
---

**Location:** `ScrySearch_Filters_ShortcodeFeature` in `[features/shortcode/feature.php](features/shortcode/feature.php)`  
**Template:** `[features/shortcode/elements/filters.php](features/shortcode/elements/filters.php)`  
**Script:** `[features/shortcode/assets/js/filters.js](features/shortcode/assets/js/filters.js)`

Renders a facet form that syncs into one or more Scry Search forms on submit. Place it on the same page as a Scry Search form.

### Admin generator

A shortcode generator lives in the base plugin’s **Facets** premium-upgrade settings modal (`scry_ms_premium_upgrade_settings_ui`, slug `scry-search-facets`). Use the **Appearance** and **Groups** tabs, then copy the shortcode.

Catalog data (indexed post types + taxonomies/terms) respects `[scry_ms_fa_excluded_taxonomies](/scry-search-filters/filters/scry_ms_fa_excluded_taxonomies/)`.

### Attributes


| Attribute       | Default      | Description                                                                                                                                                           |
| --------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `groups`        | *(required)* | JSON object of facet groups (see below). Empty / invalid JSON → shortcode outputs nothing.                                                                            |
| `selector`      | `''`         | CSS selector that must match the search form’s **`<form>` tag** (see [Connecting to a specific search form](/scry-search-filters/shortcodes/scry-search-facets/)). Empty → all forms on `window.scrySearch.searchForms`. Stored as `data-scry-fi-selector`. |
| `layout`        | `column`     | `column`, `row`, or `grid`                                                                                                                                            |
| `bg_color`      | `#ffffff`    | Group background (hex)                                                                                                                                                |
| `text_color`    | `#111111`    | Text color (hex)                                                                                                                                                      |
| `border_color`  | `#dddddd`    | Group border color (hex)                                                                                                                                              |
| `border_width`  | `1px`        | CSS length (`px` / `em` / `rem` / `%`)                                                                                                                                |
| `border_radius` | `4px`        | CSS length                                                                                                                                                            |
| `group_spacing` | `16px`       | Gap between groups                                                                                                                                                    |
| `group_padding` | `12px`       | Padding inside each group                                                                                                                                             |
| `checked_color` | `#2271b1`    | Checkbox accent color (hex)                                                                                                                                           |


### Escaping square brackets

WordPress ends shortcodes at the first `]`, and also stripslashes attribute values. For **every** `[` / `]` in `groups` or `selector` (JSON syntax and string values), write `u005b` / `u005d` instead of literal brackets (don't you love WordPress 😅):

```
[scry-search-facets groups='{"general":{"label":"General","facets":{"publishDate":{"label":"Publish Date","name":"scry-searchu005bfacetsu005du005bgeneralu005du005bpost_date_unixu005d","type":"daterange"}}}}']
```

The shortcode restores `u005b` → `[` and `u005d` → `]` before `json_decode`. The admin generator does this escaping for you.

From PHP, when building `groups` yourself, escape **all** brackets the same way the admin generator does:

```php
$attr = str_replace( array( '[', ']' ), array( 'u005b', 'u005d' ), wp_json_encode( $groups ) );
// e.g. [scry-search-facets groups='…escaped json…']
```

### `groups` JSON shape

Top-level keys are group IDs. Each group has `label` and `facets`. Facet keys are **input values** (e.g. term slug); `name` is the shared request field path.

```json
{
  "general": {
    "label": "General",
    "facets": {
      "type": {
        "label": "Post Type",
        "name": "post_type",
        "type": "select",
        "options": [
          { "label": "Any", "value": "any" },
          { "label": "Post", "value": "post" }
        ]
      },
      "publishDate": {
        "label": "Publish Date",
        "name": "scry-search[facets][general][post_date_unix]",
        "type": "daterange"
      }
    }
  },
  "category": {
    "label": "Categories",
    "facets": {
      "news": {
        "label": "News",
        "name": "scry-search[facets][taxonomies][category][]",
        "type": "checkbox"
      }
    }
  }
}
```

#### Facet `type` values


| `type`      | Behavior                                                                                                                   |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| `checkbox`  | Checkbox; `name` is the field; **value** is the facet key (e.g. term slug). Prefer `name` ending in `[]` for multi-select. |
| `select`    | `<select>`; requires `options`: `{ label, value }[]`.                                                                      |
| `daterange` | Two date inputs: `{name}[from]` and `{name}[to]`.                                                                          |
| `hidden`    | Always-on hidden input. Optional `value` (defaults to the facet key).                                                      |


Legacy string facets (`"facet_key": "Label"`) are still accepted; they render as checkboxes with `name` = key.

### Request parameter format

Filters are submitted under `scry-search[facets]` (not the older `scry-search[filters][facets]` path):

```
scry-search[facets][taxonomies][category][]     # term slugs
scry-search[facets][general][post_date_unix][from]  # YYYY-MM-DD
scry-search[facets][general][post_date_unix][to]
post_type                                       # optional top-level select / hidden CPT lock
```

The search feature builds Meilisearch expressions only when the attribute is filterable on that index (e.g. `taxonomies.category.id`, `post_date_unix`). If a field is not filterable on an index, documents from that index are **not** excluded by that facet.

### Connecting to a specific search form

By default (empty `selector`), a facets shortcode attaches to **every** Scry Search form on the page. To bind it to one form (or a subset), set `selector` to a CSS selector that matches that form’s **`<form>` element**.

Matching uses `searchForm.formElement.matches(selector)`. The selector must therefore target the `<form>` tag itself — not a wrapper `div`, not an input inside the form. Selectors that only match a child (e.g. `#wp-block-search__input-3`) will not attach.

| Goal | Example `selector` |
| ---- | ------------------ |
| Form with a class | `form.qwerty_search` |
| Form with an id | `#my-search-form` (on the `<form>`) |
| Core Search block (select via an inner input) | `form:has(#wp-block-search__input-3)` |
| All forms (default) | omit `selector` or leave it empty |

```
[scry-search-facets selector="form.qwerty_search" groups='…']
```

In the admin shortcode generator (**Appearance** tab → **Search form selector**), enter the same CSS selector. Square brackets in the value are escaped automatically.

If nothing matches, the facets widget still renders but never injects fields into a search submit.

### How it wires to search forms

1. Front-end script depends on the base plugin handle `scry_ms_window-script`.
2. On `scrySearchReady`, it registers the `filters` upgrade and wraps each matching widget in `ScrySearchFilters_FilterForm`.
3. Each widget’s `selector` (if set) filters which registered search forms it attaches to — see [Connecting to a specific search form](/scry-search-filters/shortcodes/scry-search-facets/).
4. On form pre-submit, filter field values are copied into the search form as hidden inputs (see [Frontend upgrade](/scry-search-filters/javascript/window-scrysearch-upgrade/)).

---
