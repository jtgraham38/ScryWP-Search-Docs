---
layout: doc
title: "scry_ms_meilisearch_client"
summary: "Replace or wrap the Meilisearch PHP client built by the shared factory."
plugin: scry-search
plugin_name: "Scry Search"
plugin_url: "/scry-search/"
doc_type: filter
doc_type_label: "PHP filter"
type_url: "/scry-search/filters/"
category: "Search query (front‑end search interception)"
---

Replace or wrap the Meilisearch PHP client built by the shared factory.


|               |                                                                                   |
| ------------- | --------------------------------------------------------------------------------- |
| **Type**      | Filter                                                                            |
| **Arguments** | `Meilisearch\Client $client`, `string $key_type` (`'admin'` or `'search'`)        |
| **Returns**   | `Meilisearch\Client`                                                              |
| **When**      | Every time a client is constructed via the client feature.                        |


Front-end and admin index search use `'search'` (falling back to the admin key when no search key is set). Indexing, settings, and tasks use `'admin'`.
