---
layout: doc
title: "scry_ms_index_typo_tolerance"
summary: "Change the default typo tolerance settings used when configuring new indexes."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Change the **default** typo tolerance settings used when configuring new indexes.


|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| **Type**      | Filter                                                          |
| **Arguments** | `array $typo_tolerance`                                         |
| **Returns**   | `array` — Meilisearch typo tolerance settings shape             |
| **When**      | When default typo tolerance settings are resolved.              |


Typical keys: `enabled`, `minWordSizeForTypos` (`oneTypo` / `twoTypos`), `disableOnWords`, `disableOnAttributes`, `disableOnNumbers`.
