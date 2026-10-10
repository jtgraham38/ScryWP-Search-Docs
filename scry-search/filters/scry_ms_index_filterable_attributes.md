---
layout: doc
title: "scry_ms_index_filterable_attributes"
summary: "Change the default filterable attributes list used when configuring new indexes."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Change the **default** filterable attributes list used when configuring new indexes.


|               |                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                                   |
| **Arguments** | `array $filterable_attributes`                                                           |
| **Returns**   | `array` — attribute path list                                                            |
| **When**      | When default filterable attributes are resolved.                                         |


Defaults include fields such as `post_date_unix`, `post_type`, `post_status`, `post_author`, and taxonomy ID paths like `taxonomies.category.id`.
