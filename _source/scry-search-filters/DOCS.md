# Scry Search Filters — Developer Hooks

Public extension points for **Scry Search: Meilisearch Filtered Search**. All add-on hooks use the `scry_ms_fa_` prefix.

Use these from a theme or companion plugin. Shared helper: `[includes/hooks-helpers.php](includes/hooks-helpers.php)` (`scry_ms_fa_get_excluded_taxonomies()`).

Front-end filters are primarily the `**[scry-search-facets]` shortcode**. It injects selected facets into Scry Search forms via the base plugin’s `window.scrySearch` runtime (see [Frontend: `window.scrySearch` upgrade](#frontend-windowscrysearch-upgrade)).

---

## Quick reference


| Hook                                                                                                      | Type   | File                             |
| --------------------------------------------------------------------------------------------------------- | ------ | -------------------------------- |
| `[scry_ms_fa_search_filters](#scry_ms_fa_search_filters)`                                                 | Filter | `features/search/feature.php`    |
| `[scry_ms_fa_filters_localized](#scry_ms_fa_filters_localized)`                                           | Filter | `features/shortcode/feature.php` |
| `[scry_ms_fa_excluded_taxonomies](#scry_ms_fa_excluded_taxonomies)`                                       | Filter | `includes/hooks-helpers.php`     |
| `[scry_ms_fa_analytics_filters_payload](#scry_ms_fa_analytics_filters_payload)`                           | Filter | `features/analytics/feature.php` |
| `[scry_ms_fa_analytics_recent_searches_filters_html](#scry_ms_fa_analytics_recent_searches_filters_html)` | Filter | `features/analytics/feature.php` |


---

## Shortcode: `[scry-search-facets]`

**Location:** `ScrySearch_Filters_ShortcodeFeature` in `[features/shortcode/feature.php](features/shortcode/feature.php)`  
**Template:** `[features/shortcode/elements/filters.php](features/shortcode/elements/filters.php)`  
**Script:** `[features/shortcode/assets/js/filters.js](features/shortcode/assets/js/filters.js)`

Renders a facet form that syncs into one or more Scry Search forms on submit. Place it on the same page as a Scry Search form.

### Admin generator

A shortcode generator lives in the base plugin’s **Facets** premium-upgrade settings modal (`scry_ms_premium_upgrade_settings_ui`, slug `scry-search-facets`). Use the **Appearance** and **Groups** tabs, then copy the shortcode.

Catalog data (indexed post types + taxonomies/terms) respects `[scry_ms_fa_excluded_taxonomies](#scry_ms_fa_excluded_taxonomies)`.

### Attributes


| Attribute       | Default      | Description                                                                                                                                                           |
| --------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `groups`        | *(required)* | JSON object of facet groups (see below). Empty / invalid JSON → shortcode outputs nothing.                                                                            |
| `selector`      | `''`         | CSS selector that must match the search form’s **`<form>` tag** (see [Connecting to a specific search form](#connecting-to-a-specific-search-form)). Empty → all forms on `window.scrySearch.searchForms`. Stored as `data-scry-fi-selector`. |
| `layout`        | `column`     | `column`, `row`, or `grid`                                                                                                                                            |
| `bg_color`      | `#ffffff`    | Group background (hex)                                                                                                                                                |
| `text_color`    | `#111111`    | Text color (hex)                                                                                                                                                      |
| `border_color`  | `#dddddd`    | Group border color (hex)                                                                                                                                              |
| `border_width`  | `1px`        | CSS length (`px` / `em` / `rem` / `%`)                                                                                                                                |
| `border_radius` | `4px`        | CSS length                                                                                                                                                            |
| `group_spacing` | `16px`       | Gap between groups                                                                                                                                                    |
| `group_padding` | `12px`       | Padding inside each group                                                                                                                                             |
| `checked_color` | `#2271b1`    | Checkbox accent color (hex)                                                                                                                                           |


### Escaping square brackets

WordPress ends shortcodes at the first `]`, and also stripslashes attribute values. For **every** `[` / `]` in `groups` or `selector` (JSON syntax and string values), write `u005b` / `u005d` instead of literal brackets (don't you love WordPress 😅):

```
[scry-search-facets groups='{"general":{"label":"General","facets":{"publishDate":{"label":"Publish Date","name":"scry-searchu005bfacetsu005du005bgeneralu005du005bpost_date_unixu005d","type":"daterange"}}}}']
```

The shortcode restores `u005b` → `[` and `u005d` → `]` before `json_decode`. The admin generator does this escaping for you.

From PHP, when building `groups` yourself, escape **all** brackets the same way the admin generator does:

```php
$attr = str_replace( array( '[', ']' ), array( 'u005b', 'u005d' ), wp_json_encode( $groups ) );
// e.g. [scry-search-facets groups='…escaped json…']
```

### `groups` JSON shape

Top-level keys are group IDs. Each group has `label` and `facets`. Facet keys are **input values** (e.g. term slug); `name` is the shared request field path.

```json
{
  "general": {
    "label": "General",
    "facets": {
      "type": {
        "label": "Post Type",
        "name": "post_type",
        "type": "select",
        "options": [
          { "label": "Any", "value": "any" },
          { "label": "Post", "value": "post" }
        ]
      },
      "publishDate": {
        "label": "Publish Date",
        "name": "scry-search[facets][general][post_date_unix]",
        "type": "daterange"
      }
    }
  },
  "category": {
    "label": "Categories",
    "facets": {
      "news": {
        "label": "News",
        "name": "scry-search[facets][taxonomies][category][]",
        "type": "checkbox"
      }
    }
  }
}
```

#### Facet `type` values


| `type`      | Behavior                                                                                                                   |
| ----------- | -------------------------------------------------------------------------------------------------------------------------- |
| `checkbox`  | Checkbox; `name` is the field; **value** is the facet key (e.g. term slug). Prefer `name` ending in `[]` for multi-select. |
| `select`    | `<select>`; requires `options`: `{ label, value }[]`.                                                                      |
| `daterange` | Two date inputs: `{name}[from]` and `{name}[to]`.                                                                          |
| `range`     | Dual range slider: `{name}[from]` and `{name}[to]`, plus `min` / `max` / `step` on the facet. For post meta, also submit `{name}[type]=range` (the generator does this). |
| `hidden`    | Always-on hidden input. Optional `value` (defaults to the facet key).                                                      |


Legacy string facets (`"facet_key": "Label"`) are still accepted; they render as checkboxes with `name` = key.

### Request parameter format

Filters are submitted under `scry-search[facets]` (not the older `scry-search[filters][facets]` path):

```
scry-search[facets][taxonomies][category][]        # term slugs
scry-search[facets][general][post_date_unix][from] # YYYY-MM-DD
scry-search[facets][general][post_date_unix][to]
scry-search[facets][meta][_price][from]            # numeric range bound
scry-search[facets][meta][_price][to]
scry-search[facets][meta][_price][type]            # must be "range" for built-in meta handling
post_type                                          # optional top-level select / hidden CPT lock
```

The search feature builds Meilisearch expressions only when the attribute is filterable on that index (e.g. `taxonomies.category.id`, `post_date_unix`, `post_meta._price`). If a field is not filterable on an index, documents from that index are **not** excluded by that facet.

See [Built-in filter construction](#built-in-filter-construction) for how each request key becomes a Meilisearch expression.

### Connecting to a specific search form

By default (empty `selector`), a facets shortcode attaches to **every** Scry Search form on the page. To bind it to one form (or a subset), set `selector` to a CSS selector that matches that form’s **`<form>` element**.

Matching uses `searchForm.formElement.matches(selector)`. The selector must therefore target the `<form>` tag itself — not a wrapper `div`, not an input inside the form. Selectors that only match a child (e.g. `#wp-block-search__input-3`) will not attach.

| Goal | Example `selector` |
| ---- | ------------------ |
| Form with a class | `form.qwerty_search` |
| Form with an id | `#my-search-form` (on the `<form>`) |
| Core Search block (select via an inner input) | `form:has(#wp-block-search__input-3)` |
| All forms (default) | omit `selector` or leave it empty |

```
[scry-search-facets selector="form.qwerty_search" groups='…']
```

In the admin shortcode generator (**Appearance** tab → **Search form selector**), enter the same CSS selector. Square brackets in the value are escaped automatically.

If nothing matches, the facets widget still renders but never injects fields into a search submit.

**Caution — multiple facet widgets on one page:** Each facets shortcode injects its fields into every search form it attaches to. If two (or more) facet interfaces both target the same search form — or both use an empty `selector` — they will all inject on submit. Hidden inputs that share the same `name` can overwrite each other, so facets from one widget may clobber another. Scope each facet interface with a distinct `selector` that matches only the search bar it belongs to.

### How it wires to search forms

1. Front-end script depends on the base plugin handle `scry_ms_window-script`.
2. On `scrySearchReady`, it registers the `filters` upgrade and wraps each matching widget in `ScrySearchFilters_FilterForm`.
3. Each widget’s `selector` (if set) filters which registered search forms it attaches to — see [Connecting to a specific search form](#connecting-to-a-specific-search-form).
4. On form pre-submit, filter field values are copied into the search form as hidden inputs (see [Frontend upgrade](#frontend-windowscrysearch-upgrade)).

---

## Frontend: `window.scrySearch` upgrade

**Script:** `[features/shortcode/assets/js/filters.js](features/shortcode/assets/js/filters.js)`  
**Localized object:** `scrySearchFilters` (filterable via `[scry_ms_fa_filters_localized](#scry_ms_fa_filters_localized)`)

The base Scry Search plugin exposes a global runtime, typically:

- `window.scrySearch` — main API
- `window.scrySearch.searchForms` — registered search form instances
- `window.scrySearch.upgrades` — map of registered premium upgrades
- `window.scrySearch.registerUpgrade( slug, version )` — register an upgrade

`scrySearchReady` is dispatched on `**document`** (not `window`). This add-on listens there before touching the API.

### Registration

```js
document.addEventListener('scrySearchReady', function () {
    window.scrySearch.registerUpgrade('filters', '1.0.0');
    const filtersUpgrade = window.scrySearch.upgrades.filters;
    // …
});
```

After init, `filtersUpgrade.data.filterFormInstances` holds one `ScrySearchFilters_FilterForm` per element matching `scrySearchFilters.selector` (default `form.scry-search-facets`).

### Per-widget targeting

Each shortcode form may set `data-scry-fi-selector`. The widget’s `ScrySearchFilters_FilterForm`:

- If the attribute is empty → attaches to **every** entry in `window.scrySearch.searchForms`
- Otherwise → attaches only when `searchForm.formElement.matches(selector)`

The selector is tested against the **`<form>` element** (`formElement`), not a parent wrapper or child control. Use a selector that matches that tag (e.g. `form.my-search`, `#search-form`, `form:has(.wp-block-search__input)`). See [Connecting to a specific search form](#connecting-to-a-specific-search-form).

### Pre-submit injection

For each linked search form the widget:

1. Ensures `searchForm.data.filters = { hiddeninputs: [] }`
2. Registers `searchForm.addPreSubmitAction(…)` which:
  - Removes previously injected hidden inputs
  - Reads `FormData` from the filters widget (keeps duplicate names — do not use `Object.fromEntries`)
  - Appends one hidden `<input>` per non-empty entry onto the search form
3. Also registers `addPreSubmitAjaxAction(…)` (AJAX path; still evolving)

**Important:** Filters run only when Scry Search’s pre-submit hooks fire (normal `submit` or `submitAjax()`). Calling native `HTMLFormElement.submit()` bypasses the `submit` event and **skips** filter injection. Prefer `form.requestSubmit()`, a submit button, or the wrapped `ScrySearch_SearchForm.submit()` API.

### Extending from custom JS

```js
document.addEventListener('scrySearchReady', function () {
    const upgrade = window.scrySearch.upgrades.filters;
    if (!upgrade) {
        return;
    }
    // Inspect or decorate instances after the filters script has run
    // (enqueue after `scry-search-facets`, or listen later / use a higher-order hook).
    console.log(upgrade.data.filterFormInstances);
});
```

To change which DOM nodes become widgets, filter the localized selector (PHP) rather than hard-coding classes in JS.

---

## Search

### `scry_ms_fa_search_filters`

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

After this filter runs, non-empty expressions are joined with `AND` and applied via `$search_query->setFilter([ $filters_string ])`.

### Built-in filter construction

**Location:** `ScrySearch_Filters_SearchFeature::add_filters_to_search_query()` in `[features/search/feature.php](features/search/feature.php)`  
**Hooked to:** base plugin `scry_ms_multi_search_query` (per index).

Request params come from `$_GET` on normal submits, or the decoded JSON body on AJAX `POST`. Filterable attributes are loaded from the target index; each built-in expression is skipped when its attribute is not filterable there (federation-safe).

#### Taxonomies — `scry-search[facets][taxonomies]`

For each taxonomy slug → list of term **slugs**:

1. Resolve terms with `get_terms( [ 'taxonomy' => $taxonomy, 'slug' => $slugs ] )` (unknown taxonomies / empty results are skipped).
2. Map to term IDs.
3. Require `taxonomies.{taxonomy}.id` to be filterable on the index.
4. Emit **one equality per term ID**, AND-joined with everything else:
   `(taxonomies.category.id = 12)` AND `(taxonomies.category.id = 34)` …

So multiple selected terms under the same taxonomy mean “must have **all** of these terms,” not OR.

#### Post meta — `scry-search[facets][meta]`

The shortcode range facet submits `{name}[from]`, `{name}[to]`, and a hidden `{name}[type]=range`. The search feature reads the **`meta`** request key (not `post_meta`), so the facet `name` must be `scry-search[facets][meta][{meta_key}]`.

For each meta key → value object:

```
scry-search[facets][meta][{meta_key}][type]   # currently only "range"
scry-search[facets][meta][{meta_key}][from]
scry-search[facets][meta][{meta_key}][to]
```

| `type`  | Meilisearch attribute     | Expression |
| ------- | ------------------------- | ---------- |
| `range` | `post_meta.{meta_key}`    | `(post_meta.{meta_key} >= {from} AND post_meta.{meta_key} <= {to})` when that attribute is filterable |

Example request → filter:

```
scry-search[facets][meta][_price][type]=range
scry-search[facets][meta][_price][from]=245
scry-search[facets][meta][_price][to]=790
```

→ `(post_meta._price >= 245 AND post_meta._price <= 790)` (if `post_meta._price` is filterable).

**Numeric indexing note:** WordPress meta is often indexed as strings (e.g. `"75"`). String comparison is lexicographic, so a value like `"75"` can incorrectly match a numeric-looking range such as `245`–`790`. Cast meta to numbers in `scry_ms_index_prepare_document` and reindex before relying on range filters. Also cast `from` / `to` when building custom expressions via `scry_ms_fa_search_filters`.

#### Publish date — `scry-search[facets][general][post_date_unix]`

`from` / `to` as `YYYY-MM-DD` → unix timestamps on filterable `post_date_unix` (`>=` / `<=` / both).

#### Extending

Append or rewrite expressions in `[scry_ms_fa_search_filters](#scry_ms_fa_search_filters)` before they are joined and applied.

---

## Shortcode script localization

### `scry_ms_fa_filters_localized`

Filters the array passed to `wp_localize_script` as `scrySearchFilters` for the front-end filters script.

**Location:** `ScrySearch_Filters_ShortcodeFeature::filters_scripts()` in `[features/shortcode/feature.php](features/shortcode/feature.php)`

```php
add_filter( 'scry_ms_fa_filters_localized', function( $data ) {
    // Match widgets that use a custom class instead of form.scry-search-facets.
    $data['selector'] = '.my-site-filters, form.scry-search-facets';
    return $data;
} );
```


| Parameter         | Type    | Description                                                 |
| ----------------- | ------- | ----------------------------------------------------------- |
| `$localized_data` | `array` | Default includes `selector` => `'form.scry-search-facets'` |


**Returns:** `array` localized for `scrySearchFilters` in JS.

---

## Excluded taxonomies

### `scry_ms_fa_excluded_taxonomies`

Filters taxonomy slugs excluded from the shortcode generator catalog (and any other call sites that use the helper).

Prefer reading the list through `scry_ms_fa_get_excluded_taxonomies( $defaults )` so the filter always runs.

**Location:** `[includes/hooks-helpers.php](includes/hooks-helpers.php)`  
**Call site (current):** shortcode generator catalog in `[features/shortcode/feature.php](features/shortcode/feature.php)`

```php
add_filter( 'scry_ms_fa_excluded_taxonomies', function( $excluded ) {
    $excluded[] = 'product_visibility';
    return array_values( array_diff( $excluded, array( 'post_format' ) ) ); // re-enable one
} );
```


| Parameter              | Type    | Description                      |
| ---------------------- | ------- | -------------------------------- |
| `$excluded_taxonomies` | `array` | Default slugs from plugin config |


**Returns:** `array` of taxonomy slug strings.

**Helper:**

```php
$excluded = scry_ms_fa_get_excluded_taxonomies(
    array( 'post_format', 'nav_menu', 'link_category', 'wp_theme', 'wp_template_part_area' )
);
```

---

## Analytics

### `scry_ms_fa_analytics_filters_payload`

Filters the analytics extras payload attached as `scry_search_filters` on the base plugin analytics event.

Return an empty array to omit the key entirely.

Default payload shape when filters were applied:

```php
array(
    'general' => array(
        'type' => 'post', // or list of slugs; from facets general.type or top-level post_type
        'publishDate' => array( 'from' => '2024-01-01', 'to' => '2024-06-01' ),
    ),
    'taxonomies' => array(
        'category' => array(
            array( 'id' => 12, 'name' => 'News', 'slug' => 'news' ),
        ),
    ),
)
```

**Location:** `ScrySearch_Filters_AnalyticsFeature::build_analytics_filters_payload()` in `[features/analytics/feature.php](features/analytics/feature.php)`

```php
add_filter( 'scry_ms_fa_analytics_filters_payload', function( $payload, $facets ) {
    if ( ! empty( $facets['custom'] ) ) {
        $payload['custom'] = $facets['custom'];
    }
    return $payload;
}, 10, 2 );
```


| Parameter  | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| `$payload` | `array` | Built analytics filters payload            |
| `$facets`  | `array` | Raw `scry-search[facets]` from the request |


**Returns:** `array` payload. Non-arrays become `[]` (key omitted when empty).

Supports both the current slug-based taxonomy map and a legacy term-ID list under `taxonomies`.

---

### `scry_ms_fa_analytics_recent_searches_filters_html`

Filters the HTML for the **Filters** column in the base plugin Recent Searches table.

**Location:** `ScrySearch_Filters_AnalyticsFeature::render_recent_searches_column()` in `[features/analytics/feature.php](features/analytics/feature.php)`

```php
add_filter( 'scry_ms_fa_analytics_recent_searches_filters_html', function( $html, $filters, $item ) {
    // $filters is the stored scry_search_filters payload from search_metadata.
    return $html;
}, 10, 3 );
```


| Parameter  | Type     | Description                                            |
| ---------- | -------- | ------------------------------------------------------ |
| `$html`    | `string` | Default expandable dropdown cell markup                |
| `$filters` | `array`  | `scry_search_filters` from the row’s `search_metadata` |
| `$item`    | `array`  | Full analytics table row                               |


**Returns:** `string` HTML. Non-strings become `&mdash;`.

---

## Typical customization flow

### Shortcode / front end

1. Generate or hand-author `[scry-search-facets]` with escaped `groups` JSON
2. Optionally set `selector` so only specific Scry Search forms receive filters
3. Change the widget query selector globally via `scry_ms_fa_filters_localized`
4. Ensure Meilisearch indexes have the needed filterable attributes (e.g. `taxonomies.category.id`, `post_date_unix`, `post_meta._price`)
5. For meta ranges, index numeric values (not strings) and reindex — see [Built-in filter construction](#built-in-filter-construction)

### Custom Meilisearch filters

1. Submit extra fields from your own UI (or extend `groups`) under a consistent request shape
2. Translate them in `scry_ms_fa_search_filters` (taxonomies / meta / date are already built-in)
3. Mirror anything worth reporting in `scry_ms_fa_analytics_filters_payload`

### Generator catalog

1. Adjust excluded taxonomies with `scry_ms_fa_excluded_taxonomies` so the admin Groups tab matches your site

---

## Notes

- These are hooks fired *by* this add-on. The plugin also *consumes* base Scry Search hooks prefixed `scry_ms_` (see `[README.md](README.md)`) — e.g. `scry_ms_multi_search_query`, `scry_ms_analytics_event_to_insert`, `scry_ms_premium_upgrade_settings_ui`, `scry_ms_premium_upgrades_display`.
- The Gutenberg **Search Facets** block and related index-admin hooks are not currently registered in `[scry_search_facets.php](scry_search_facets.php)`; the shortcode + search + analytics path is the supported surface.
- Code that still exists but is not wired (e.g. federation facet helpers, index-document filters) should not be treated as public API until re-enabled.
- Dependency guard and premium-upgrade settings chrome (beyond the shortcode generator) are not public customization surfaces.

