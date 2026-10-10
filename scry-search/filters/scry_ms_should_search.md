---
layout: doc
title: "scry_ms_should_search"
summary: "Opt a WP_Query out of Meilisearch interception (falls through to native WordPress search)."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Opt a `WP_Query` out of Meilisearch interception (falls through to native WordPress search).


|               |                                                                     |
| ------------- | ------------------------------------------------------------------- |
| **Type**      | Filter                                                              |
| **Arguments** | `bool $should_search`, `WP_Query $query`                            |
| **Returns**   | `bool` — `true` to use Meilisearch, `false` for native WP search    |
| **When**      | After the query is confirmed to be a search, before indexes are resolved. |


```php
add_filter( 'scry_ms_should_search', function ( $should_search, $query ) {
    if ( is_admin() ) {
        return false;
    }
    return $should_search;
}, 10, 2 );
```
