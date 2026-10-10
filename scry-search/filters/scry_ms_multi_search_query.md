---
layout: doc
title: "scry_ms_multi_search_query"
summary: "Modify the per‑index search query object."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Modify the per‑index search query object.


|               |                                                                         |
| ------------- | ----------------------------------------------------------------------- |
| **Type**      | Filter                                                                  |
| **Arguments** | `Meilisearch\Contracts\SearchQuery $search_query`, `string $index_name` |
| **Returns**   | `Meilisearch\Contracts\SearchQuery`                                     |
| **When**      | Once per index, as each query is constructed.                           |
