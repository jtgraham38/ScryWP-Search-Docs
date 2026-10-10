---
layout: doc
title: "scry_ms_bulk_index_batch_size"
summary: "Control how many posts are loaded per batch during bulk indexing."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Control how many posts are loaded per batch during bulk indexing.


|               |                                                                  |
| ------------- | ---------------------------------------------------------------- |
| **Type**      | Filter                                                           |
| **Arguments** | `int $batch_size`, `string $post_type`, `string $index_name`     |
| **Returns**   | `int` — posts per batch (values below `1` fall back to `100`)    |
| **When**      | Before the bulk index loop starts fetching post batches.         |


Default is `100`. Raise it for fewer round-trips on large catalogs; lower it if memory is tight.
