---
layout: doc
title: "scry_ms_after_index_document"
summary: "Fires after a single post document is successfully written to Meilisearch."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Fires after a single post document is successfully written to Meilisearch.


|               |                                                                        |
| ------------- | ---------------------------------------------------------------------- |
| **Type**      | Action                                                                 |
| **Arguments** | `int $post_id`, `string $index_name`, `array $document`                |
| **When**      | After a successful live `updateDocuments` in `index_post`.             |
