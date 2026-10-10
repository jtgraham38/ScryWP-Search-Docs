---
layout: doc
title: "scry_ms_autosuggest_query"
summary: "Modify the query used to build autosuggest results."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Autosuggest"
---

Modify the query used to build autosuggest results.


|               |                                            |
| ------------- | ------------------------------------------ |
| **Type**      | Filter                                     |
| **Arguments** | `array $autosuggest_query` (WP_Query args) |
| **Returns**   | `array`                                    |
| **When**      | Before the autosuggest query runs.         |


The array contains standard `WP_Query` arguments such as `s`, `post_type`, `posts_per_page`, and `no_found_rows`. Default `posts_per_page` comes from [`scry_ms_autosuggest_posts_per_page`](/scry-search/filters/scry_ms_autosuggest_posts_per_page/).
