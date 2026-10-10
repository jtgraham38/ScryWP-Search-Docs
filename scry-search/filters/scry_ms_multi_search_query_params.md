---
layout: doc
title: "scry_ms_multi_search_query_params"
summary: "Adjust high‑level query parameters."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Adjust high‑level query parameters.


|               |                                          |
| ------------- | ---------------------------------------- |
| **Type**      | Filter                                   |
| **Arguments** | `array $query_params`, `WP_Query $query` |
| **Returns**   | `array` — the query params               |
| **When**      | After the base params are assembled.     |


`$query_params` may include keys like `q` (search term), `limit`, and `offset`.
