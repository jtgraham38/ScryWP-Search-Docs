---
layout: doc
title: "scry_ms_should_delete"
summary: "Decide whether a document should be removed from Meilisearch when a post is trashed or permanently deleted."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Decide whether a document should be removed from Meilisearch when a post is trashed or permanently deleted.


|               |                                                              |
| ------------- | ------------------------------------------------------------ |
| **Type**      | Filter                                                       |
| **Arguments** | `bool $should_delete`, `int $post_id`, `string $index_name` |
| **Returns**   | `bool` — `true` to delete, `false` to keep the document      |
| **When**      | Before `deleteDocument` runs for trash or permanent delete.  |
