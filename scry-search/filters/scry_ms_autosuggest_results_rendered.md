---
layout: doc
title: "scry_ms_autosuggest_results_rendered"
summary: "Modify the HTML markup for the autosuggest dropdown after it is rendered from the PHP template."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Autosuggest"
---

Modify the HTML markup for the autosuggest dropdown after it is rendered from the PHP template.


|               |                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                                               |
| **Arguments** | `string $output`, `array $results`, `WP_Query $search_query`, `WP_REST_Request $request`             |
| **Returns**   | `string` — HTML for the dropdown                                                                     |
| **When**      | After `elements/rendered_autosuggest.php` runs, before the REST response is sent.                    |


Use this when you need to change the markup itself (wrap the list, inject extra rows, replace the template output). Prefer `scry_ms_autosuggest_results` when you only need to change the data. The REST response includes both `data` (the result array) and `rendered` (this HTML string).

```php
add_filter( 'scry_ms_autosuggest_results_rendered', function ( $output, $results, $search_query, $request ) {
    return '<div class="my-autosuggest-wrap">' . $output . '</div>';
}, 10, 4 );
```

Default markup matches the client-built structure: `.scry-search-autosuggest-results` → list → linked rows (optional thumb + title) → close button.
