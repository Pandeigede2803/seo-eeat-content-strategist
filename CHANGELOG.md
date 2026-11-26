# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Renamed the repository from `skill` to `seo-eeat-content-strategist` and
  pointed the install commands at the real owner, so `npx skills add` and
  `git clone` work as written.
- Added a positioning tagline and a repository badge to the README.

## [1.1.0] - 2026-11-26

### Added

- `README.md` with installation, usage, and customization guides.
- `references/` folder with audit rubric, evidence ledger template, and
  medical safety checklist.
- `assets/article-brief-template.md` worksheet.
- `examples/example-output.md` end-to-end sample.
- `scripts/validate_skill.py` frontmatter and link validator.
- GitHub Actions validation workflow and issue/PR templates.
- MIT license, contributing guide, and changelog.

### Changed

- Restructured the skill into the standard Agent Skills layout.
- Completed YAML frontmatter with `license` and `metadata`.
- Fixed broken markdown tables in the workflow and audit sections.
- Moved detailed scoring and safety material into `references/` for
  progressive disclosure.
- Expanded hard-stop rules and added a publication-blocker section.

## [1.0.0] - 2026-11-26

### Added

- Initial `SKILL.md` covering role, principles, eight-stage workflow, output
  format, and prohibited practices.
