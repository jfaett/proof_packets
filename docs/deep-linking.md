# Stable deep links and QR codes

Slides should link to a durable redirect, not a branch-specific GitHub URL.

## Contract

- Human-facing short link: https://approved.example/go/rhel-patching
- Repository target: use-cases/rhel-patching/README.md
- Optional audience routes: /discover, /demo, and /prove
- The redirect service owns analytics and destination changes.
- Headings referenced by anchors are treated as public interfaces.

shortlinks.yaml is the source of truth. scripts/generate_shortlinks.py validates it and emits a portable redirect map under artifacts/.

## QR guidance

- Encode the short URL, not the raw repository URL.
- Print the short URL below the QR code for accessibility.
- Use error correction suitable for projected slides.
- Test from a non-corporate device and network.
- Never encode a secret, expiring token, or internal customer identifier.

## Change policy

Paths may move only if the redirect remains valid. A removed target needs a successor or a clear retirement page. Review deep-link changes as breaking changes even when the Markdown text change looks small.
