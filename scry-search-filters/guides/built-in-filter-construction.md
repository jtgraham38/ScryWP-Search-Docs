---
layout: doc
title: "Built-in filter construction"
heading: "Built-in filter construction"
summary: "Location: ScrySearch_Filters_SearchFeature::add_filters_to_search_query() in features/search/feature.php Hooked to: base plugin scry_ms_multi_search_query (per index)."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search-filters/guides/"
category: "Search"
---

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

Append or rewrite expressions in `[scry_ms_fa_search_filters]({{ '/scry-search-filters/filters/scry_ms_fa_search_filters/' | relative_url }})` before they are joined and applied.
