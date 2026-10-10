---
layout: doc
title: "scry_ms_autosuggest_posts_per_page"
summary: "Change how many results autosuggest requests (default 5)."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Autosuggest"
---

Change how many results autosuggest requests (default `5`).


|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| **Type**      | Filter                                                          |
| **Arguments** | `int $posts_per_page` (default `5`)                             |
| **Returns**   | `int` — number of hits to request                               |
| **When**      | Before the autosuggest `WP_Query` args are built.               |


The value is cast to an integer; values below `1` fall back to `5`. It becomes `posts_per_page` on the query that Meilisearch intercepts (and thus the federated search `limit`). You can still override `posts_per_page` later via `scry_ms_autosuggest_query`.

```php
add_filter( 'scry_ms_autosuggest_posts_per_page', function ( $posts_per_page ) {
    return 10;
} );
```
