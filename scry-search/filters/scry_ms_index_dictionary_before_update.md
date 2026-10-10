---
layout: doc
title: "scry_ms_index_dictionary_before_update"
summary: "$dictionary is a flat list of words that should not be split during tokenization. An empty array clears the dictionary for the index."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

|               |                                          |
| ------------- | ---------------------------------------- |
| **Type**      | Filter                                   |
| **Arguments** | `array $dictionary`, `string $index_name`|
| **Returns**   | `array`                                  |


`$dictionary` is a flat list of words that should not be split during tokenization. An empty array clears the dictionary for the index.
