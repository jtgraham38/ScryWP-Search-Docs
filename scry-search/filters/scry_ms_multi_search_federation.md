---
layout: doc
title: "scry_ms_multi_search_federation"
summary: "Modify the federation options for the multi‑search request."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Modify the federation options for the multi‑search request.


|               |                                                           |
| ------------- | --------------------------------------------------------- |
| **Type**      | Filter                                                    |
| **Arguments** | `Meilisearch\Contracts\MultiSearchFederation $federation` |
| **Returns**   | `Meilisearch\Contracts\MultiSearchFederation`             |
| **When**      | After limit/offset are set, before the request runs.      |
