---
layout: doc
title: "Extending from custom JS"
heading: "Extending from custom JS"
summary: "Hook your own post-AJAX actions after the Ajax upgrade has registered."
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
