---
layout: doc
title: "scry_ms_index_filterable_attributes_before_update"
summary: "$filterable_attributes is a flat list of attribute paths. An empty array clears filterable attributes for the index."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

|               |                                                       |
| ------------- | ----------------------------------------------------- |
| **Type**      | Filter                                                |
| **Arguments** | `array $filterable_attributes`, `string $index_name`  |
| **Returns**   | `array`                                               |


`$filterable_attributes` is a flat list of attribute paths. An empty array clears filterable attributes for the index.
