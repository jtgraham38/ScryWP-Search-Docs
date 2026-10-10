---
layout: doc
title: "scry_ms_bulk_index_query_args"
summary: "Control the get_posts arguments used during a bulk reindex."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Control the `get_posts` arguments used during a bulk reindex.


|               |                                                                        |
| ------------- | ---------------------------------------------------------------------- |
| **Type**      | Filter                                                                 |
| **Arguments** | `array $args`, `string $post_type`, `string $index_name`               |
| **Returns**   | `array` — `get_posts` / `WP_Query` args                                |
| **When**      | Immediately before posts are fetched for a bulk index AJAX operation.  |


```php
add_filter( 'scry_ms_bulk_index_query_args', function ( $args, $post_type, $index_name ) {
    $args['posts_per_page'] = 500;
    return $args;
}, 10, 3 );
```
