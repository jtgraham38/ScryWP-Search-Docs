---
layout: doc
title: "scry_ms_should_index"
summary: "Decide whether a post should be indexed."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Indexing & document shaping"
---

Decide whether a post should be indexed.


|               |                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                                   |
| **Arguments** | `bool $should_index`, `WP_Post $post`, `string $context` (`'save'` or `'bulk'`)          |
| **Returns**   | `bool` — `true` to index, `false` to skip                                                |
| **When**      | After built-in type / publish / password-protected checks, before the document is formatted (live save and bulk). |


Core already skips unpublished and password-protected posts on live save (password check feeds `$should_index` as `false` before this filter). Bulk reindex still goes through this filter with a default of `true` — skip there if needed.

```php
add_filter( 'scry_ms_should_index', function ( $should_index, $post, $context ) {
    if ( get_post_meta( $post->ID, '_exclude_from_search', true ) ) {
        return false;
    }
    return $should_index;
}, 10, 3 );
```
