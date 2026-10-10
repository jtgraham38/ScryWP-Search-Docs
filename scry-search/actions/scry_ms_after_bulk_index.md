---
layout: doc
title: "scry_ms_after_bulk_index"
summary: "Fires after a bulk reindex successfully submits documents to Meilisearch."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: action
doc_type_label: "PHP action"
type_url: "/scry-search/actions/"
category: "Lifecycle"
---

Fires after a bulk reindex successfully submits documents to Meilisearch.


|               |                                                                                   |
| ------------- | --------------------------------------------------------------------------------- |
| **Type**      | Action                                                                            |
| **Arguments** | `string $post_type`, `string $index_name`, `int $count`, `mixed $task`             |
| **When**      | After `updateDocuments` succeeds in the bulk index AJAX handler (once per batch). |


`$task` is the Meilisearch task payload returned by the client (may include `taskUid`).
