---
layout: doc
title: "scry_ms_multi_search_index_names"
summary: "Choose which indexes a search runs against."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Choose which indexes a search runs against.


|               |                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------ |
| **Type**      | Filter                                                                                           |
| **Arguments** | `array $index_names_to_search` (map of `post_type => index name`), `array $post_types_to_search` |
| **Returns**   | `array` — the index map                                                                          |
| **When**      | After the target indexes are resolved, before queries are built.                                 |
