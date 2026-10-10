---
layout: doc
title: "Filters upgrade overview"
heading: "Filters upgrade overview"
summary: "Public extension points for Scry Search: Meilisearch Filtered Search. All add-on hooks use the scry_ms_fa_ prefix."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search-filters/guides/"
category: "Basics"
---

Public extension points for **Scry Search: Meilisearch Filtered Search**. All add-on hooks use the `scry_ms_fa_` prefix.

Use these from a theme or companion plugin. Shared helper: `[includes/hooks-helpers.php](includes/hooks-helpers.php)` (`scry_ms_fa_get_excluded_taxonomies()`).

Front-end filters are primarily the `**[scry-search-facets]` shortcode**. It injects selected facets into Scry Search forms via the base plugin’s `window.scrySearch` runtime (see [Frontend: `window.scrySearch` upgrade](/scry-search-filters/javascript/window-scrysearch-upgrade/)).

---
