---
layout: doc
title: "scry_ms_index_prepare_document"
summary: "Modify a single post's document just before it is sent to Meilisearch."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Modify a single post's document just before it is sent to Meilisearch.


|               |                                                                            |
| ------------- | -------------------------------------------------------------------------- |
| **Type**      | Filter                                                                     |
| **Arguments** | `array $document`, `WP_Post $post`                                         |
| **Returns**   | `array` — the (possibly modified) document                                 |
| **When**      | Each time a post is prepared for indexing (single save and bulk indexing). |


```php
add_filter( 'scry_ms_index_prepare_document', function ( $document, $post ) {
    $document['reading_time'] = my_estimate_reading_time( $document['post_content'] ?? '' );
    return $document;
}, 10, 2 );
```

A document is an associative array keyed by attribute name (for example `ID`, `post_title`, `post_content`, `post_excerpt`, `post_author`, `permalink`, `post_meta`, `categories`, and `tags`). Public taxonomy term names are included automatically (`category` → `categories`, `post_tag` → `tags`, other public taxonomies under their taxonomy slug). Add, remove, or rewrite keys as needed; whatever you return is what gets indexed.
