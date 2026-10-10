---
layout: doc
title: "scry_ms_after_delete_document"
summary: "Fires after a document is successfully deleted from Meilisearch."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Fires after a document is successfully deleted from Meilisearch.


|               |                                                                  |
| ------------- | ---------------------------------------------------------------- |
| **Type**      | Action                                                           |
| **Arguments** | `int $post_id`, `string $index_name`                             |
| **When**      | After a successful `deleteDocument` (trash or permanent delete). |
