---
layout: list
title: "PHP filters — Scry Search Ajax"
summary: "All PHP filter hooks for Scry Search Ajax."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: filter
doc_type_label: "PHP filter"
list_kind: type
show_filter_search: true
---

<table class="list-table"><thead><tr><th>Name</th><th>Category</th><th>Summary</th></tr></thead><tbody>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_localized/' | relative_url }}"><code>scry_ms_aj_ajax_localized</code></a></td><td>Ajax search</td><td class="muted">Filters the data passed to wp_localize_script for the front-end shortcode script (scrySearchAjax).</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_federation/' | relative_url }}"><code>scry_ms_aj_ajax_search_federation</code></a></td><td>Ajax search</td><td class="muted">Filters the Meilisearch\Contracts\MultiSearchFederation object (limit/offset, and any further federation options you attach).</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_final_results/' | relative_url }}"><code>scry_ms_aj_ajax_search_final_results</code></a></td><td>Ajax search</td><td class="muted">Filters shaped / enriched hit results before HTML rendering.</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_index_names/' | relative_url }}"><code>scry_ms_aj_ajax_search_index_names</code></a></td><td>Ajax search</td><td class="muted">Filters the post-type → index-name map used for the request.</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_parameters/' | relative_url }}"><code>scry_ms_aj_ajax_search_parameters</code></a></td><td>Ajax search</td><td class="muted">Filters raw search parameters after they are read from the REST request, before the Meilisearch client runs.</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_query/' | relative_url }}"><code>scry_ms_aj_ajax_search_query</code></a></td><td>Ajax search</td><td class="muted">Filters each per-index Meilisearch\Contracts\SearchQuery before it is added to the multi-search batch.</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_raw_results/' | relative_url }}"><code>scry_ms_aj_ajax_search_raw_results</code></a></td><td>Ajax search</td><td class="muted">Filters the raw Meilisearch multiSearch response before hits are enriched from WordPress.</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_aj_ajax_search_results_rendered/' | relative_url }}"><code>scry_ms_aj_ajax_search_results_rendered</code></a></td><td>Ajax search</td><td class="muted">Filters the HTML string produced by rendered_ajax.php before it is returned in the REST response.</td></tr>
<tr><td><a href="{{ '/scry-search-ajax/filters/scry_ms_premium_upgrades_display/' | relative_url }}"><code>scry_ms_premium_upgrades_display</code></a></td><td>Integration</td><td class="muted">Used to mark the Ajax upgrade card as active when this plugin is installed.</td></tr>
</tbody></table>
