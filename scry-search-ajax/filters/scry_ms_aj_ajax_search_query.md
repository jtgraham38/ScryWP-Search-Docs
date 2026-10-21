---
layout: doc
title: "scry_ms_aj_ajax_search_query"
summary: "Filters each per-index Meilisearch\\Contracts\\SearchQuery before it is added to the multi-search batch."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-ajax/filters/"
category: "Ajax search"
---

Filters each per-index `Meilisearch\Contracts\SearchQuery` before it is added to the multi-search batch.

| Arg | Type | Description |
|---|---|---|
| `$search_request` | `SearchQuery` | Query for one index |
| `$post_type` | string | Post type for this query |
| `$index_name` | string | Index UID |

**Returns:** `SearchQuery`
