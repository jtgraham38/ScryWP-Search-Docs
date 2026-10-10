---
layout: doc
title: "scry_ms_autosuggest_results"
summary: "Modify the structured result list used for autosuggest (before HTML is rendered)."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Autosuggest"
---

Modify the structured result list used for autosuggest (before HTML is rendered).


|               |                                                                                          |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                                   |
| **Arguments** | `array $results`, `WP_Query $search_query`, `WP_REST_Request $request`                   |
| **Returns**   | `array` — list of result objects                                                         |
| **When**      | After default result objects are built, before the HTML template runs.                   |


Each default result has `title`, `url`, `excerpt`, `post_type`, and `featured_image`. Add fields for themes/add-ons (prices, badges, etc.) as needed. The filtered array is what feeds `elements/rendered_autosuggest.php` and is returned as `data` in the REST response.

```php
add_filter( 'scry_ms_autosuggest_results', function ( $results, $search_query, $request ) {
    foreach ( $results as &$result ) {
        $result['badge'] = 'Featured';
    }
    return $results;
}, 10, 3 );
```
