---
layout: doc
title: "scry_ms_index_update_settings"
summary: "Fires after index settings have been successfully applied to Meilisearch."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Fires after index settings have been successfully applied to Meilisearch.


|               |                                            |
| ------------- | ------------------------------------------ |
| **Type**      | Action                                     |
| **Arguments** | `object $index` (Meilisearch index handle) |
| **When**      | After a settings save completes.           |
