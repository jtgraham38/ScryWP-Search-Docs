---
layout: doc
title: "scry_ms_index_typo_tolerance_before_update"
summary: "$typo_tolerance uses the Meilisearch typo tolerance object shape (enabled, minWordSizeForTypos, disableOnWords, disableOnAttributes, disableOnNumbers)."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Index settings flow (per‑index configuration)"
---

|               |                                              |
| ------------- | -------------------------------------------- |
| **Type**      | Filter                                       |
| **Arguments** | `array $typo_tolerance`, `string $index_name`|
| **Returns**   | `array`                                      |


`$typo_tolerance` uses the Meilisearch typo tolerance object shape (`enabled`, `minWordSizeForTypos`, `disableOnWords`, `disableOnAttributes`, `disableOnNumbers`).
