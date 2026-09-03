# katapult-plugins

A Claude Code plugin marketplace containing the **katapult-klogic** plugin, which turns plain-English Katapult Pro QC checks into paste-ready K-Logic JSON blocks.

## What's in here

```
katapult-plugins/                         # marketplace repo (this repo)
├── .claude-plugin/
│   └── marketplace.json                  # marketplace manifest (lists the plugin)
├── plugins/
│   └── katapult-klogic/                  # the plugin
│       ├── .claude-plugin/
│       │   └── plugin.json               # plugin manifest
│       ├── SKILL.md                      # the skill (single SKILL.md at plugin root)
│       ├── references/
│       │   ├── klogic-syntax.md
│       │   ├── operators.md
│       │   ├── paths.md
│       │   ├── photofirst-markers.md
│       │   ├── examples.md
│       │   └── datasets/
│       │       ├── nodes.md
│       │       ├── sections.md
│       │       ├── node-attributes.md
│       │       ├── node-attributes-full.md
│       │       ├── connection-attributes-full.md
│       │       ├── section-attributes-full.md
│       │       ├── job-attributes-full.md
│       │       └── photo-attributes-full.md
│       └── scripts/
│           └── build_attribute_catalog.py
└── README.md
```

The plugin uses the single-`SKILL.md`-at-root layout: because there's no `skills/` subdirectory and no `skills` field in `plugin.json`, Claude Code loads the root `SKILL.md` as one skill, named by its frontmatter `name` (`katapult-klogic`).

## Before you publish

Edit two placeholders:

- `.claude-plugin/marketplace.json` → set `owner.name` (currently `REPLACE_ME`).
- `plugins/katapult-klogic/.claude-plugin/plugin.json` → optionally add `author`, `repository`, `homepage`.

The plugin pins `"version": "0.1.0"`. With a version set, users only get updates when you bump it. If you'd rather have updates track every commit while you iterate, delete the `version` field and install from a git-hosted marketplace.

## Load it into a Claude Code session

**Option A — live, single session (best while iterating).** Reads the plugin directly from disk, so edits to the reference files show up without a reinstall:

```
claude --plugin-dir ./plugins/katapult-klogic
```

**Option B — install from this marketplace (persists across sessions).**

Local path:

```
/plugin marketplace add /absolute/path/to/katapult-plugins
/plugin install katapult-klogic@katapult-plugins
```

Or, once this repo is on GitHub:

```
/plugin marketplace add your-org/katapult-plugins
/plugin install katapult-klogic@katapult-plugins
```

If the install summary says `Run /reload-plugins to activate`, run `/reload-plugins`. A marketplace install copies the plugin into `~/.claude/plugins/`, so later edits to your source need `/plugin marketplace update katapult-plugins` + reinstall — which is why Option A is nicer during development.

## Validate before committing

```
claude plugin validate ./plugins/katapult-klogic
claude plugin validate .            # validates the marketplace
```

Add `--strict` to treat warnings (e.g. leftover unrecognized fields) as errors in CI.

## Using the skill

Once loaded, describe a QC check in plain English (e.g. "flag any section where a proposed slacked comm cable sits over an existing full-tension comm cable") and the skill produces a `KLOGIC:`-prefixed block to paste into the Katapult Pro Logic Editor. The `references/` files define block/operator/path shapes; the `references/datasets/` catalogs pin per-model attribute keys and values.
