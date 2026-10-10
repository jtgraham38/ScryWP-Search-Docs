---
layout: doc
title: "scry_ms_multi_search_final_results"
summary: "Modify the final array of posts returned to WordPress."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Modify the final array of posts returned to WordPress.


|               |                                                                                      |
| ------------- | ------------------------------------------------------------------------------------ |
| **Type**      | Filter                                                                               |
| **Arguments** | `array $posts_array` (list of `WP_Post`)                                             |
| **Returns**   | `array`                                                                              |
| **When**      | After hits are resolved into post objects, before they are handed back to the query. |
