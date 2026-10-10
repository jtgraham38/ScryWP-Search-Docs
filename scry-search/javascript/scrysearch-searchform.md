---
layout: doc
title: "ScrySearch_SearchForm"
summary: "Per-form wrapper with submit/submitAjax and ordered pre/post action hooks."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: javascript
doc_type_label: "JavaScript API"
type_url: "/scry-search/javascript/"
category: "Runtime"
---

Each detected form is wrapped in a `ScrySearch_SearchForm` instance.


| Member                               | Type                   | Description                                                                                                                     |
| ------------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `formElement`                        | `HTMLFormElement`      | The underlying `<form>`.                                                                                                        |
| `searchInput`                        | `HTMLInputElement`     | The detected search input (`name="s"`).                                                                                         |
| `data`                               | `object`               | Arbitrary per‑form storage. Use it to stash state (e.g. `data.core` is used internally by autosuggest).                         |
| `submit()`                           | `() => void`           | Runs pre‑submit actions, performs a normal form submit, then runs post‑submit actions.                                          |
| `submitAjax()`                       | `() => Promise<any>`   | Runs pre‑AJAX actions, submits the form via AJAX, runs post‑AJAX actions, and resolves with the parsed response. **Debounced.** |
| `addPreSubmitAction(fn, order)`      | `(fn, number) => void` | Add an action before a normal submit.                                                                                           |
| `addPostSubmitAction(fn, order)`     | `(fn, number) => void` | Add an action after a normal submit.                                                                                            |
| `addPreSubmitAjaxAction(fn, order)`  | `(fn, number) => void` | Add an action before an AJAX submit.                                                                                            |
| `addPostSubmitAjaxAction(fn, order)` | `(fn, number) => void` | Add an action after an AJAX submit.                                                                                             |
