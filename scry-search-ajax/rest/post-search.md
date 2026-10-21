---
layout: doc
title: "POST /wp-json/scry-search-ajax/v1/search"
summary: "Federated Meilisearch search used by the [scry-search-ajax] shortcode."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: rest
doc_type_label: "REST API"
type_url: "/scry-search-ajax/rest/"
category: "REST"
---

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
