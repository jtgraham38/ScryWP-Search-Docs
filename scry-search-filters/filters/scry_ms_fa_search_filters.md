---
layout: doc
title: "scry_ms_fa_search_filters"
summary: "Filters Meilisearch filter expressions before they are joined with AND and passed to setFilter()."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search-filters/filters/"
category: "Search"
---

Filters Meilisearch filter expressions before they are joined with `AND` and passed to `setFilter()`.

Each item should be a filter string, typically already wrapped in parentheses (e.g. `(taxonomies.category.id = 12)`).

**Location:** `ScrySearch_Filters_SearchFeature::add_filters_to_search_query()` in `[features/search/feature.php](features/search/feature.php)`

```php
add_filter( 'scry_ms_fa_search_filters', function( $filters, $index_name, $request_params ) {
    // Example: always require a minimum unix publish date when the request asks for it.
    if ( ! empty( $request_params['scry-search']['facets']['general']['post_date_unix']['from'] ) ) {
        // Built-in logic already handles post_date_unix; add custom fields here.
    }
    $filters[] = '(post_type = "post")'; // only if that attribute is filterable on the index
    return $filters;
}, 10, 3 );
```


| Parameter         | Type     | Description                                         |
| ----------------- | -------- | --------------------------------------------------- |
| `$filters`        | `array`  | Parenthesized Meilisearch filter expression strings |
| `$index_name`     | `string` | Target Meilisearch index name                       |
| `$request_params` | `array`  | Request params (`$_GET` or decoded POST JSON body)  |


**Returns:** `array` of filter strings. Non-arrays are coerced to `[]`.

Built-in expressions currently cover:

- `scry-search[facets][general][post_date_unix]` → `post_date_unix` range (when filterable)
- `scry-search[facets][taxonomies][{taxonomy}][]` → one `(taxonomies.{taxonomy}.id = {id})` per selected term slug (AND across terms; skipped when the attribute is not filterable)
