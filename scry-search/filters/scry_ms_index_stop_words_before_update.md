---
layout: doc
title: "scry_ms_index_stop_words_before_update"
summary: "$stop_words is a flat list of words. An empty array clears stop words for the index."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

|               |                                           |
| ------------- | ----------------------------------------- |
| **Type**      | Filter                                    |
| **Arguments** | `array $stop_words`, `string $index_name` |
| **Returns**   | `array`                                   |


`$stop_words` is a flat list of words. An empty array clears stop words for the index.
