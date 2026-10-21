---
layout: doc
title: "Upgrade registration"
heading: "Upgrade registration"
summary: "How the ajax upgrade registers on scrySearchReady and wraps matching forms."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search-ajax/javascript/"
category: "Runtime"
---

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
