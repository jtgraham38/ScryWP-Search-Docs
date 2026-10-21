---
layout: doc
title: "scry_ms_aj_ajax_search_raw_results"
summary: "Filters the raw Meilisearch multiSearch response before hits are enriched from WordPress."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters the raw Meilisearch `multiSearch` response before hits are enriched from WordPress.

| Arg | Type | Description |
|---|---|---|
| `$search_results` | array | Raw Meilisearch federated response |
| `$post_types` | array | Requested post types |
| `$federation` | array | Sanitized federation request array |

**Returns:** `array`
