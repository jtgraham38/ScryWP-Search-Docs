---
layout: doc
title: "scry_ms_aj_ajax_search_results_rendered"
summary: "Filters the HTML string produced by rendered_ajax.php before it is returned in the REST response."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters the HTML string produced by `rendered_ajax.php` before it is returned in the REST response.

| Arg | Type | Description |
|---|---|---|
| `$rendered_results` | string | HTML markup |
| `$results` | mixed | Results used for rendering |
| `$search_query` | mixed | Search context |
| `$request` | `WP_REST_Request` | Incoming REST request |

**Returns:** `string`
