---
layout: doc
title: "Form discovery"
heading: "Form discovery"
summary: "How the runtime finds <form> elements and wraps them as ScrySearch_SearchForm instances."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

On init, the runtime calls `discoverSearchForms(windowLocalized.searchFormSelectors)`:

1. Runs `document.querySelectorAll(selectors.join(', '))` for every selector in the array
2. Keeps only elements whose tag is `<form>`
3. Wraps each match in a `ScrySearch_SearchForm`

**Built‑in defaults** (from `features/window/feature.php`):

- `#adminbarsearch` — WordPress admin bar search
- `form[role="search"]` — theme/core forms with `role="search"` (includes the Gutenberg Search block form)

Selectors must resolve to **`<form>` elements**. A selector that only matches an `<input>` (for example `.wp-block-search__input`) will be discarded by the form-tag filter.

#### Add your own selectors (recommended)

Prefer the PHP filter so discovery works on every page load without custom JS:

```php
add_filter( 'scry_ms_window_localized', function ( $data ) {
    $data['searchFormSelectors'][] = 'form.my-custom-search';
    $data['searchFormSelectors'][] = '.header-search form';
    return $data;
} );
```

Mark the form in your theme:

```html
<form role="search" method="get" class="my-custom-search" action="/">
  <input type="search" name="s" />
</form>
```

#### Limit autosuggest to some discovered forms

Discovery and autosuggest targeting are separate:

1. **Discovery** — which forms become `ScrySearch_SearchForm` instances (`searchFormSelectors`)
2. **Autosuggest class** — under **Scry Search → Search Settings**, optional class name on the `<form>`

Leave the autosuggest class blank to attach typeahead to **all** discovered forms. Set it to a class like `my-site-search` (the class token only — not `form.my-site-search`) to attach only to forms that have that class.

```js
// What autosuggest does internally after scrySearchReady:
if (autoSuggestLocalized.classSelector) {
    searchForms = window.scrySearch.getSearchFormsByClass(autoSuggestLocalized.classSelector);
} else {
    searchForms = window.scrySearch.getSearchForms();
}
```
