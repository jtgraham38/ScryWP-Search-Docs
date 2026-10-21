---
layout: doc
title: "scry_ms_aj_ajax_search_index_names"
summary: "Filters the post-type → index-name map used for the request."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters the post-type → index-name map used for the request.

| Arg | Type | Description |
|---|---|---|
| `$index_names` | array | Map of `post_type => index_uid` |
| `$post_types` | array | Requested post types |

**Returns:** `array`
