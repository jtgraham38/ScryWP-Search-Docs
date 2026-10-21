---
layout: doc
title: "window.scrySearch filters upgrade"
heading: "window.scrySearch filters upgrade"
summary: "Script: features/shortcode/assets/js/filters.js Localized object: scrySearchFilters (filterable via scry_ms_fa_filters_localized)"
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search-filters/javascript/"
category: "Runtime"
---

**Script:** `[features/shortcode/assets/js/filters.js](features/shortcode/assets/js/filters.js)`  
**Localized object:** `scrySearchFilters` (filterable via `[scry_ms_fa_filters_localized]({{ '/scry-search-filters/filters/scry_ms_fa_filters_localized/' | relative_url }})`)

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

The selector is tested against the **`<form>` element** (`formElement`), not a parent wrapper or child control. Use a selector that matches that tag (e.g. `form.my-search`, `#search-form`, `form:has(.wp-block-search__input)`). See [Connecting to a specific search form]({{ '/scry-search-filters/shortcodes/scry-search-facets/' | relative_url }}).

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
