---
layout: doc
title: "scry_ms_index_synonyms_before_update"
summary: "$synonyms is a map of base term => array of synonym terms. An empty array clears synonyms for the index."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

|               |                                         |
| ------------- | --------------------------------------- |
| **Type**      | Filter                                  |
| **Arguments** | `array $synonyms`, `string $index_name` |
| **Returns**   | `array`                                 |


`$synonyms` is a map of `base term => array of synonym terms`. An empty array clears synonyms for the index.
