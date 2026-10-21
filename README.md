# Scry Search Docs

Jekyll documentation site for **Scry Search** and premium upgrades (**Scry Search Filters**, **Scry Search Ajax**).

Branding follows [scrywp.com](https://scrywp.com/) (Figtree, purple primary `#a31bff`, blue info accent `#2e5eff`, light surface).

## Structure

```
scry-search/                 Core plugin
  guides/                    Concepts (naming, lifecycle, …)
  filters/                   One page per scry_ms_* filter
  actions/                   One page per scry_ms_* action
  javascript/                window.scrySearch runtime pages

scry-search-filters/         Filters upgrade
  guides/
  shortcodes/                [scry-search-facets]
  filters/                   scry_ms_fa_* filters
  javascript/                filters upgrade on window.scrySearch

scry-search-ajax/            Ajax upgrade
  guides/
  rest/                      POST /wp-json/scry-search-ajax/v1/search
  filters/                   scry_ms_aj_* filters
  actions/                   main-plugin actions this add-on consumes
  javascript/                ajax upgrade on window.scrySearch

reference/                   Flat list of every page
_source/                     Canonical DOCS.md copies used to regenerate
scripts/generate_docs.py     Regenerator
```

Future upgrades: add `_source/<plugin-slug>/DOCS.md`, extend the generator, and emit another top-level folder with the same type subfolders.

## Regenerate pages from DOCS.md

After updating a plugin’s `DOCS.md`, copy it into `_source/` and run:

```bash
cp ../scrywp_search/DOCS.md _source/scry-search/DOCS.md
cp ../ScryWP-Search-Filters/DOCS.md _source/scry-search-filters/DOCS.md
cp ../ScryWP-Search-Ajax/DOCS.md _source/scry-search-ajax/DOCS.md
python3 scripts/generate_docs.py
```

## Serve locally

```bash
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/`.
