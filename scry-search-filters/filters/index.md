---
layout: list
title: "PHP filters — Scry Search Filters"
summary: "All PHP filter hooks for Scry Search Filters."
plugin: scry-search-filters
plugin_name: "Scry Search Filters"
plugin_url: "/scry-search-filters/"
doc_type: filter
doc_type_label: "PHP filter"
list_kind: type
show_filter_search: true
---

<table class="list-table"><thead><tr><th>Name</th><th>Category</th><th>Summary</th></tr></thead><tbody>
<tr><td><a href="/scry-search-filters/filters/scry_ms_fa_analytics_filters_payload/"><code>scry_ms_fa_analytics_filters_payload</code></a></td><td>Analytics</td><td class="muted">Filters the analytics extras payload attached as scry_search_filters on the base plugin analytics event.</td></tr>
<tr><td><a href="/scry-search-filters/filters/scry_ms_fa_analytics_recent_searches_filters_html/"><code>scry_ms_fa_analytics_recent_searches_filters_html</code></a></td><td>Analytics</td><td class="muted">Filters the HTML for the Filters column in the base plugin Recent Searches table.</td></tr>
<tr><td><a href="/scry-search-filters/filters/scry_ms_fa_excluded_taxonomies/"><code>scry_ms_fa_excluded_taxonomies</code></a></td><td>Catalog</td><td class="muted">Filters taxonomy slugs excluded from the shortcode generator catalog (and any other call sites that use the helper).</td></tr>
<tr><td><a href="/scry-search-filters/filters/scry_ms_fa_filters_localized/"><code>scry_ms_fa_filters_localized</code></a></td><td>Shortcode</td><td class="muted">Filters the array passed to wp_localize_script as scrySearchFilters for the front-end filters script.</td></tr>
<tr><td><a href="/scry-search-filters/filters/scry_ms_fa_search_filters/"><code>scry_ms_fa_search_filters</code></a></td><td>Search</td><td class="muted">Filters Meilisearch filter expressions before they are joined with AND and passed to setFilter().</td></tr>
</tbody></table>
