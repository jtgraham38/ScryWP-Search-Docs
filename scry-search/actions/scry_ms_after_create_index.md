---
layout: doc
title: "scry_ms_after_create_index"
summary: "Fires immediately after a new index is created."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Fires immediately after a new index is created.


|               |                                            |
| ------------- | ------------------------------------------ |
| **Type**      | Action                                     |
| **Arguments** | `object $index` (Meilisearch index handle) |
| **When**      | Right after a missing index is created.    |


Use it to apply additional index configuration on creation.
