# Contributing to the blyg

The blyg holds the SIG's session notes and running research log. It is published at
https://npc.here.now/protocolvision/blyg/ with the [Blygger protocol](https://blygger.org/) 0.2:
plain files plus an RSS feed that anyone can follow.

Anyone with write access to this repo can publish. **A commit is a publish.**

## Add something

    python3 tools/blyg_new.py thread session-2026-11-02 --author "Your Name"    # session notes, long pieces
    python3 tools/blyg_new.py fragment some-claim --author "Your Name"          # a short note or claim

Each command creates a file with a permanent `id`. Write Markdown under the front matter, then:

    git add blyg-src && git commit -m "Session notes: 2 November" && git push

The commit message becomes the version note in the item's public changelog, so keep it short and readable.
If you don't have write access, open a pull request; it is published when merged.

## Edit

Change the file and commit again. Each commit that changes the text becomes a new version (v2, v3, …).
Readers see the latest version; earlier text is not published unless it is pinned.
Uncommitted changes are drafts and are never published.

## Quote a fragment in a thread

Put `![[<fragment id>]]` on its own line. At publish time the fragment's current text is copied into the
thread, with a record of which version was quoted. The research log quotes the premises this way.

## Mark machine-written text

If a model wrote a passage, fence it and name the model in the front matter:

    generated_model: claude-opus-5-5
    ---
    ::: generated
    Text the model wrote.
    :::

The fences are removed on publish; the passage is marked as generated in the published HTML and JSON.
Imported session summaries from the Protocol Institute archive are marked this way (c3po wrote them).

## Withdraw or pin

- `withdrawn: true` in the front matter publishes a withdrawal. There is no delete, and it can be reversed.
- `pin: [2]` promises to keep version 2 available forever at `items/<id>/v2.json`. Pins can't be undone.

## Rules of thumb

- Don't rename or move files. The id lives in the file, but the version history follows the path.
- Keep fragments under about 1,000 characters.
- Don't name people outside the group without their consent. Session participants are listed by Discord handle.

## What happens after you push

GitHub Actions builds the site and the blyg, runs `tools/blyg_check.py` (the protocol conformance check),
and publishes if the check passes. Pull requests get the same build and check, without publishing.
To try it locally: `python3 tools/build_blyg.py && python3 tools/blyg_check.py`.
