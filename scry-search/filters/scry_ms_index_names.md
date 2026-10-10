---
layout: doc
title: "scry_ms_index_names"
summary: "Customize the map of post types to Meilisearch index UIDs."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Customize the map of post types to Meilisearch index UIDs.


|               |                                                                           |
| ------------- | ------------------------------------------------------------------------- |
| **Type**      | Filter                                                                    |
| **Arguments** | `array $index_names` (map of `post_type => index_uid`)                    |
| **Returns**   | `array` — the index name map                                              |
| **When**      | Whenever the plugin resolves which indexes exist for configured post types. |


```php
add_filter( 'scry_ms_index_names', function ( $index_names ) {
    $index_names['product'] = 'shared_products_index';
    return $index_names;
} );
```
