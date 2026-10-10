---
layout: doc
title: "Submit action pipeline"
heading: "Submit action pipeline"
summary: "Ordered pre/post actions for normal and AJAX submits."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

Each form maintains four ordered lists of actions:

- `**preSubmitActions`** — run before a normal (page‑navigating) submit.
- `**postSubmitActions**` — run after a normal submit (often won't run, since the page navigates away).
- `**preSubmitAjaxActions**` — run before an AJAX submit.
- `**postSubmitAjaxActions**` — run after an AJAX submit, once the response is available.

Actions run in ascending `order` (lowest first). Use `order` to position your action relative to others (e.g. built‑in autosuggest actions).

**Callback signatures:**

- Pre actions and normal post actions receive the form: `function (searchForm) { … }`
- Post‑**AJAX** actions also receive the response data: `function (searchForm, data) { … }`

> `data` is the parsed JSON response from the AJAX submit. (Both arguments are always passed for post‑AJAX actions, so falsy values like `0`, `""`, or `null` are preserved rather than dropped.)

The same callback (by function reference) won't be added twice to the same list.

#### Example: react to AJAX search results

```js
document.addEventListener('scrySearchReady', function () {
    window.scrySearch.getSearchForms().forEach(function (form) {
        // Run before the AJAX request fires.
        form.addPreSubmitAjaxAction(function (searchForm) {
            searchForm.formElement.classList.add('is-searching');
        }, 10);

        // Run after the response comes back.
        form.addPostSubmitAjaxAction(function (searchForm, data) {
            searchForm.formElement.classList.remove('is-searching');
            console.log('Results:', data);
        }, 10);
    });
});
```

#### Example: target only forms with a specific class

```js
document.addEventListener('scrySearchReady', function () {
    window.scrySearch.getSearchFormsByClass('my-search').forEach(function (form) {
        form.addPreSubmitAction(function (searchForm) {
            // e.g. add a hidden input before a normal submit
        }, 5);
    });
});
```

#### Triggering an AJAX search yourself

`submitAjax()` is debounced (`windowLocalized.debounceMs`, default 250) and returns a promise, so you can call it directly and await the result:

```js
const [form] = window.scrySearch.getSearchForms();
const data = await form.submitAjax();
```
