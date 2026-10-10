---
layout: doc
title: "scry_ms_multi_search_queries"
summary: "Modify the full set of per‑index queries before they are executed."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Modify the full set of per‑index queries before they are executed.


|               |                                                 |
| ------------- | ----------------------------------------------- |
| **Type**      | Filter                                          |
| **Arguments** | `array $search_queries` (list of `SearchQuery`) |
| **Returns**   | `array`                                         |
