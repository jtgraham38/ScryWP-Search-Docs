# Scry Search Ajax — Hooks, REST API & Frontend

Plugin hook prefix: `scry_ms_aj_` (from config `hook_prefix`).  
Main plugin hook prefix: `scry_ms_` (from config `main_plugin_hook_prefix`).

---

## REST API

### `POST /wp-json/scry-search-ajax/v1/search`

Federated Meilisearch search used by the `[scry-search-ajax]` shortcode.

| | |
|---|---|
| **Namespace** | `scry-search-ajax/v1` |
| **Route** | `/search` |
| **Methods** | `POST` |
| **Permission** | Public (`__return_true`) |

#### Request parameters

| Param | Type | Required | Description |
|---|---|---|---|
| `s` | string | yes | Search query string |
| `post_type` | string \| string[] | yes | Post type(s) to search. Use `"any"` (or omit meaningfully) to fall back to the main plugin’s indexed post types option. A single string is wrapped into an array. |
| `federation` | object | yes | Federation / pagination settings (see below) |

##### `federation` object

| Key | Type | Required | Notes |
|---|---|---|---|
| `limit` | number | yes | Positive integer; hits returned |
| `offset` | number | yes | Non-negative integer |
| `page` | number | no | Non-negative integer (UI pagination helper; SDK federation uses limit/offset) |
| `hitsPerPage` | number | no | Positive integer |
| `facetsByIndex` | string[] | no | Defaults to `[]` if omitted |
| `mergeFacets` | object | no | Optional `maxValuesPerFacet` (non-negative int) |
| `distinct` | string | no | |
| `showPerformanceDetails` | bool | no | |
| `personalize` | object | no | Optional `userContext` string |

#### Response (`200`)

```json
{
  "data": { /* raw Meilisearch multiSearch / federated payload */ },
  "rendered": "<html>…</html>"
}
```

- `data` — Meilisearch federated search result (includes `hits`, `estimatedTotalHits`, `processingTimeMs`, etc.).
- `rendered` — HTML from `features/api/elements/rendered_ajax.php`, filterable via `scry_ms_aj_ajax_search_results_rendered`.

---

## Filters (this plugin)

These are applied with the `scry_ms_aj_` prefix.

### `scry_ms_aj_ajax_localized`

Filters the data passed to `wp_localize_script` for the front-end shortcode script (`scrySearchAjax`).

| Arg | Type | Description |
|---|---|---|
| `$localized_data` | array | Script localization payload (endpoint URL, selectors, pagination defaults, etc.) |

**Returns:** `array`

---

### `scry_ms_aj_ajax_search_parameters`

Filters raw search parameters after they are read from the REST request, before the Meilisearch client runs.

| Arg | Type | Description |
|---|---|---|
| `$params` | array | `[ $search_term, $post_types, $federation ]` |

**Returns:** `array` — same three-element shape; destructured back into `$search_term`, `$post_types`, `$federation`.

---

### `scry_ms_aj_ajax_search_index_names`

Filters the post-type → index-name map used for the request.

| Arg | Type | Description |
|---|---|---|
| `$index_names` | array | Map of `post_type => index_uid` |
| `$post_types` | array | Requested post types |

**Returns:** `array`

---

### `scry_ms_aj_ajax_search_query`

Filters each per-index `Meilisearch\Contracts\SearchQuery` before it is added to the multi-search batch.

| Arg | Type | Description |
|---|---|---|
| `$search_request` | `SearchQuery` | Query for one index |
| `$post_type` | string | Post type for this query |
| `$index_name` | string | Index UID |

**Returns:** `SearchQuery`

---

### `scry_ms_aj_ajax_search_federation`

Filters the `Meilisearch\Contracts\MultiSearchFederation` object (limit/offset, and any further federation options you attach).

| Arg | Type | Description |
|---|---|---|
| `$federation_options` | `MultiSearchFederation` | Federation options sent to `multiSearch` |
| `$post_types` | array | Requested post types |
| `$federation` | array | Sanitized federation request array |

**Returns:** `MultiSearchFederation`

---

### `scry_ms_aj_ajax_search_raw_results`

Filters the raw Meilisearch `multiSearch` response before hits are enriched from WordPress.

| Arg | Type | Description |
|---|---|---|
| `$search_results` | array | Raw Meilisearch federated response |
| `$post_types` | array | Requested post types |
| `$federation` | array | Sanitized federation request array |

**Returns:** `array`

---

### `scry_ms_aj_ajax_search_final_results`

Filters shaped / enriched hit results before HTML rendering.

| Arg | Type | Description |
|---|---|---|
| `$results` | mixed | Final results passed into the render template |
| `$search_query` | mixed | Search context |
| `$request` | `WP_REST_Request` | Incoming REST request |

**Returns:** mixed (same shape expected by the render template)

---

### `scry_ms_aj_ajax_search_results_rendered`

Filters the HTML string produced by `rendered_ajax.php` before it is returned in the REST response.

| Arg | Type | Description |
|---|---|---|
| `$rendered_results` | string | HTML markup |
| `$results` | mixed | Results used for rendering |
| `$search_query` | mixed | Search context |
| `$request` | `WP_REST_Request` | Incoming REST request |

**Returns:** `string`

---

## Shared / main-plugin hooks used by this plugin

These use the main plugin prefix `scry_ms_`. This plugin either **applies** them (so other code can filter shared behavior) or **listens** to them (integration with the main upgrades UI).

### Applied (filter)

#### `scry_ms_meilisearch_client`

Lets other plugins wrap or replace the Meilisearch PHP client after it is constructed.

| Arg | Type | Description |
|---|---|---|
| `$client` | `Meilisearch\Client` | Built client |
| `$key_type` | string | Key role used to build the client (e.g. `search`, `admin`) |

**Returns:** client instance

#### `scry_ms_index_names`

Filters the map of indexed post types to Meilisearch index UIDs (same hook the main plugin uses so index naming stays consistent).

| Arg | Type | Description |
|---|---|---|
| `$index_names` | array | Map of `post_type => index_uid` |

**Returns:** `array`

---

### Consumed (listen)

#### `scry_ms_premium_upgrades_display` *(filter)*

Used to mark the Ajax upgrade card as `active` when this plugin is installed.

| Arg | Type | Description |
|---|---|---|
| `$upgrades` | array | Upgrade cards from the main plugin |

**Returns:** `array`

#### `scry_ms_premium_upgrade_settings_ui` *(action)*

Renders the shortcode generator UI inside the Ajax upgrade settings modal when the upgrade slug matches `scry-search-ajax`.

| Arg | Type | Description |
|---|---|---|
| `$upgrade` | array | Upgrade entry (must include matching `slug`) |

---

## Frontend: `window.scrySearch` upgrade

**Script:** [`features/shortcode/assets/js/ajax.js`](features/shortcode/assets/js/ajax.js)  
**Depends on:** base plugin handle `scry_ms_window-script` (and optionally `scry-search-facets`)  
**Localized object:** `scrySearchAjax` (filterable via [`scry_ms_aj_ajax_localized`](#scry_ms_aj_ajax_localized))

This add-on builds on the base Scry Search window runtime. Full base API docs live in the main plugin; the pieces used here are summarized below.

### Base runtime (from main plugin)

| Member | Description |
|---|---|
| `window.scrySearch` | Global runtime |
| `window.scrySearch.searchForms` | Registered `ScrySearch_SearchForm` instances |
| `window.scrySearch.upgrades` | Map of registered premium upgrades |
| `window.scrySearch.registerUpgrade(name, version)` | Reserve `upgrades[name]` (`name`, `version`, `data`) |
| `window.scrySearch.getSearchFormsByClass(className)` | Forms whose `<form>` has the given CSS class |
| `searchForm.submitAjax()` | Debounced AJAX submit; returns a `Promise` of the parsed JSON response |
| `searchForm.addPreSubmitAjaxAction(fn, order)` | Run before AJAX submit — `fn(searchForm)` |
| `searchForm.addPostSubmitAjaxAction(fn, order)` | Run after AJAX response — `fn(searchForm, data)` |
| `searchForm.data` | Per-form bag for upgrade state (e.g. `data.core`, `data.ajax`, `data.filters`) |
| `searchForm.ajaxEndpoint` | REST URL used by `submitAjax()` |

`scrySearchReady` is dispatched on **`document`** (not `window`). Listen there before touching the API.

### Registration

```js
document.addEventListener('scrySearchReady', function () {
    window.scrySearch.registerUpgrade('ajax', '1.0.0');
    const ajaxUpgrade = window.scrySearch.upgrades.ajax;

    const ajaxSearchForms = window.scrySearch.getSearchFormsByClass(scrySearchAjax.classSelector);
    ajaxSearchForms.forEach(function (ajaxSearchForm) {
        new ScrySearchAjax_SearchForm(ajaxSearchForm);
    });

    ajaxUpgrade.data.ajaxSearchFormInstances = ajaxSearchForms;
});
```

After init:

- `window.scrySearch.upgrades.ajax` — upgrade namespace (`name: 'ajax'`, `version: '1.0.0'`)
- `upgrades.ajax.data.ajaxSearchFormInstances` — the underlying `ScrySearch_SearchForm` instances that were wrapped (default class: `scry_ms_aj_search-form`)

Each matching form is also wrapped in a `ScrySearchAjax_SearchForm` controller (not stored separately on the upgrade today — hang off the form’s `data` bag or keep your own refs if you need the wrapper).

### Localized `scrySearchAjax`

| Key | Default | Description |
|---|---|---|
| `search_term_param` | `'s'` | Search input name |
| `classSelector` | `'scry_ms_aj_search-form'` | Class used with `getSearchFormsByClass` |
| `ajaxSubmitEndpoint` | REST search URL | Assigned to `searchForm.ajaxEndpoint` |
| `resultsSectionElementQuerySelector` | `'.scry_ms_aj_results'` | Scrollable results panel |
| `resultsContainerElementQuerySelector` | `'.scry_ms_aj_results-container'` | Hits markup target |
| `statReportElementQuerySelector` | `'.scry_ms_aj_stat-report'` | “X results…” line |
| `loaderElementQuerySelector` | `'.scry_ms_aj_loader'` | Centered overlay spinner |
| `infiniteLoaderElementQuerySelector` | `'.scry_ms_aj_infinite-loader'` | Bottom spinner for infinite scroll |
| `paginationElementQuerySelector` | `'.scry_ms_aj_pagination'` | Paged controls `<nav>` |
| `paginationPagesQuerySelector` | `'.scry_ms_aj_pagination-pages'` | Numbered page buttons host |
| `pageSizeSelectQuerySelector` | `'[data-scry-aj-page-size]'` | Results-per-page `<select>` |
| `infiniteSentinelQuerySelector` | `'.scry_ms_aj_infinite-sentinel'` | Infinite-scroll sentinel |
| `hideElementClass` | `'scry_ms_aj_hidden'` | Utility class toggled on loaders |
| `nonePaginationLimit` | `1000` | `federation.limit` when `pagination="none"` |

### `ScrySearchAjax_SearchForm`

Controller constructed per ajax shortcode form. Notable instance state:

| Member | Description |
|---|---|
| `searchForm` | Wrapped base `ScrySearch_SearchForm` |
| `formElement` | The `<form>` |
| `wrapperElement` | Shortcode root (reads `data-pagination`, `data-page-size`) |
| `paginationMode` | `'none'` \| `'paged'` \| `'infinite'` |
| `pageSize` | Hits per page |
| `federation` | `{ limit, offset, page, hitsPerPage, facetsByIndex, mergeFacets }` written as hidden inputs on submit |
| `keepPage` / `appendResults` | Flags for pagination vs fresh search |
| `totalHits` / `totalPages` | From last response’s `estimatedTotalHits` |
| `loadingMore` | Guards concurrent infinite-scroll fetches |

Important methods:

| Method | Description |
|---|---|
| `goToPage(page, appendResults)` | Sets `keepPage`, optional append, syncs federation, calls `submitAjax()` |
| `maybeLoadNextInfinitePage()` | Loads next page when the results panel is near its bottom |
| `syncFederationFromPage()` | Derives `limit` / `offset` from `page` + `pageSize` |
| `writeFederationToForm()` | Appends `federation[…]` hidden inputs before AJAX |
| `displaySearchResults(searchForm, results)` | Replaces or appends `results.rendered` |
| `displayStatReport(searchForm, results)` | Updates the stats line (range text when paginated) |

On construct it also:

1. Sets `searchForm.data.core.shouldRenderAutosuggest = false` (disables base autosuggest UI for this form).
2. Points `searchForm.ajaxEndpoint` at `scrySearchAjax.ajaxSubmitEndpoint`.
3. Registers the pre/post AJAX actions below.
4. Binds paged controls and infinite scroll when applicable.
5. If facets are attached (`searchForm.data.filters.filtersForms`), listens for `scrySearchFiltersFacetChange` and re-runs `submitAjax()` when the query is non-empty.

### Pre / post AJAX actions registered

| Pipeline | Order | Handler | Role |
|---|---|---|---|
| pre | `1` | `preparePaginationForSubmit` | Reset to page 1 unless `keepPage` |
| pre | `2` | `writeFederationToForm` | Inject `federation[…]` hidden fields |
| pre | `2` | `removeIsAutosuggestInput` | Strip base `is_autosuggest` input |
| pre | `2` | `showLoader` | Centered loader, or bottom infinite loader when appending |
| post | `10` | `removeFederationInputFields` | Clean federation hidden inputs |
| post | `10` | `hideLoader` | Hide both loaders |
| post | `50` | `displayStatReport` | Stats / “Showing X–Y of Z” |
| post | `60` | `updatePaginationUi` | Totals + paged button state |
| post | `100` | `displaySearchResults` | Paint / append HTML |

Lower `order` runs first. Custom code can insert around these with its own `order` values.

### Extending from custom JS

```js
document.addEventListener('scrySearchReady', function () {
    const upgrade = window.scrySearch.upgrades.ajax;
    if (!upgrade) {
        return;
    }

    // Forms this add-on wrapped (base ScrySearch_SearchForm instances)
    console.log(upgrade.data.ajaxSearchFormInstances);

    window.scrySearch.getSearchFormsByClass(scrySearchAjax.classSelector).forEach(function (form) {
        form.addPostSubmitAjaxAction(function (searchForm, data) {
            console.log('Ajax hits:', data?.data?.hits);
        }, 110); // after displaySearchResults (100)
    });
});
```

Enqueue after `scry-search-ajax`, or listen on `scrySearchReady` and run after this script has registered the upgrade.

**Note:** Prefer `searchForm.submitAjax()` (or `goToPage` via a held `ScrySearchAjax_SearchForm` reference). Native `HTMLFormElement.submit()` bypasses the submit event and skips the AJAX / action pipeline.
