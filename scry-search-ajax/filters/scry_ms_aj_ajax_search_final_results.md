---
layout: doc
title: "scry_ms_aj_ajax_search_final_results"
summary: "Filters shaped / enriched hit results before HTML rendering."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters shaped / enriched hit results before HTML rendering.

| Arg | Type | Description |
|---|---|---|
| `$results` | mixed | Final results passed into the render template |
| `$search_query` | mixed | Search context |
| `$request` | `WP_REST_Request` | Incoming REST request |

**Returns:** mixed (same shape expected by the render template)
