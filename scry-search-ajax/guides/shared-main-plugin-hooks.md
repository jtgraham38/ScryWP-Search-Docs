---
layout: doc
title: "Shared main-plugin hooks"
heading: "Shared main-plugin hooks"
summary: "These use the main plugin prefix scry_ms_. This plugin either applies them (so other code can filter shared behavior) or listens to them (integration with the main upgrades UI)."
plugin: scry-search-ajax
plugin_name: "Scry Search Ajax"
plugin_url: "/scry-search-ajax/"
doc_type: guide
doc_type_label: "Guide"
type_url: "/scry-search-ajax/guides/"
category: "Integration"
---

These use the main plugin prefix `scry_ms_`. This plugin either **applies** them (so other code can filter shared behavior) or **listens** to them (integration with the main upgrades UI).

### Applied (filter)

#### `scry_ms_meilisearch_client`

Lets other plugins wrap or replace the Meilisearch PHP client after it is constructed.

| Arg | Type | Description |
|---|---|---|
| `$client` | `Meilisearch\Client` | Built client |
| `$key_type` | string | Key role used to build the client (e.g. `search`, `admin`) |

**Returns:** client instance

#### `scry_ms_index_names`

Filters the map of indexed post types to Meilisearch index UIDs (same hook the main plugin uses so index naming stays consistent).

| Arg | Type | Description |
|---|---|---|
| `$index_names` | array | Map of `post_type => index_uid` |

**Returns:** `array`

---

### Consumed (listen)

#### `scry_ms_premium_upgrades_display` *(filter)*

Used to mark the Ajax upgrade card as `active` when this plugin is installed.

| Arg | Type | Description |
|---|---|---|
| `$upgrades` | array | Upgrade cards from the main plugin |

**Returns:** `array`

#### `scry_ms_premium_upgrade_settings_ui` *(action)*

Renders the shortcode generator UI inside the Ajax upgrade settings modal when the upgrade slug matches `scry-search-ajax`.

| Arg | Type | Description |
|---|---|---|
| `$upgrade` | array | Upgrade entry (must include matching `slug`) |

---
