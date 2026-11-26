# SEO E-E-A-T Content Strategist

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
[![Validate](https://img.shields.io/badge/CI-validate%20skill-success.svg)](.github/workflows/validate.yml)

An installable **Agent Skill** that turns a general-purpose assistant into a
disciplined SEO content strategist for regulated, reputation-sensitive
niches — healthcare, aesthetics, wellness, and any field where a wrong claim
carries real-world risk.

It plans, researches, drafts, and audits **people-first content** against
Google's **E-E-A-T** framework, and it refuses to fabricate the things that
make AI content dangerous: citations, credentials, patient stories,
testimonials, and first-hand experience.

---

## Table of contents

- [What it does](#what-it-does)
- [Why this skill is different](#why-this-skill-is-different)
- [Repository structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How it works](#how-it-works)
- [Quality gates](#quality-gates)
- [Customization](#customization)
- [Safety and disclaimers](#safety-and-disclaimers)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## What it does

Given a topic, brand, and market, the skill produces a complete,
audit-ready content package:

1. **SEO brief** — keyword map, search intent, audience, angle, CTA.
2. **Evidence ledger** — every material claim mapped to a verified source
   with scope and limitations.
3. **Article outline** — H1/H2/H3 structure built around real questions.
4. **Full draft** — metadata, body, FAQ, and references.
5. **E-E-A-T audit** — 0–2 score across ten categories, with weaknesses.
6. **Publication blockers** — missing facts, assets, consent, or clinician
   review.
7. **Internal link suggestions** — verified URLs only, or clearly labelled
   suggestions.

It also audits existing pages and reviews clinic marketing copy for
accuracy and compliance risk.

## Why this skill is different

Most "SEO writer" prompts optimize for output volume. This one optimizes
for **defensibility**.

| Common failure | This skill's rule |
| --- | --- |
| Invents statistics and studies | Never fabricate references; mark `[NEEDS SOURCE VERIFICATION]` |
| Assigns a doctor as reviewer | Reviewer notes only after real review; otherwise `NOT MEDICALLY APPROVED` |
| Guarantees results | No guarantee, permanence, or "safe for everyone" claims |
| Keyword-stuffs headings | Sections must answer real questions or they are cut |
| Hides risks to convert | Risks, limitations, and uncertainty are mandatory |
| Fakes authority | No awards, partnerships, or credentials without proof |
| Treats E-E-A-T as a score to game | E-E-A-T is a quality framework; trust is central |

## Repository structure

```text
seo-eeat-content-strategist/
├── SKILL.md                              # The skill (frontmatter + instructions)
├── README.md                             # This file
├── LICENSE                               # MIT
├── CONTRIBUTING.md
├── CHANGELOG.md
├── references/                           # Loaded on demand (progressive disclosure)
│   ├── audit-rubric.md                   # Expanded 0–2 scoring guide
│   ├── evidence-ledger-template.md       # Claim verification template
│   └── medical-safety-checklist.md       # Domain safety rules + adaptation guide
├── assets/
│   └── article-brief-template.md         # Fill-in brief worksheet
├── examples/
│   └── example-output.md                 # Condensed end-to-end example
├── scripts/
│   └── validate_skill.py                 # Frontmatter + link validator (stdlib only)
└── .github/
    ├── workflows/validate.yml            # CI validation
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

The skill follows the **Agent Skills** convention: a `SKILL.md` with YAML
frontmatter, optional `references/`, `assets/`, and `scripts/` folders, and
progressive disclosure so detailed material loads only when needed.

## Installation

### Option 1 — Skills CLI (recommended)

```bash
npx skills add <your-github-user>/seo-eeat-content-strategist
```

The CLI detects supported agents and installs the skill into the right
directory. Add `--global` to install for every project.

### Option 2 — Claude Code (manual)

Clone the repository into your personal or project skills directory:

```bash
# Personal: available in every project
git clone https://github.com/<your-github-user>/seo-eeat-content-strategist.git \
  ~/.claude/skills/seo-eeat-content-strategist

# Or project-scoped
git clone https://github.com/<your-github-user>/seo-eeat-content-strategist.git \
  .claude/skills/seo-eeat-content-strategist
```

The folder name **must** match the `name` in the frontmatter
(`seo-eeat-content-strategist`).

### Option 3 — Claude.ai / API

- **Claude.ai:** package the folder as a `.zip` and upload it as a skill in
  Settings → Capabilities → Skills.
- **API:** upload the skill through the Skills API and reference it by ID.

### Option 4 — Any other agent (Cursor, Windsurf, Codex, custom)

Copy `SKILL.md` (and the `references/`, `assets/` folders) into your agent's
instructions or knowledge directory. The only hard requirement is that the
agent reads `SKILL.md` when a matching task appears.

### Verify the installation

```bash
python3 scripts/validate_skill.py .
```

Expected output: `OK /path/to/seo-eeat-content-strategist`.

## Usage

### Trigger it

Mention the skill by name, or describe a matching task and let the agent
select it:

```text
Use the seo-eeat-content-strategist skill to plan and draft an article about
laser hair removal for a clinic in Bali. Target keyword: "laser hair removal
bali". Audience: adults comparing clinics. Conversion goal: consultation
booking.
```

### Example prompts

| Goal | Prompt |
| --- | --- |
| Full package | "Create a complete E-E-A-T article package for `<treatment>` targeting `<keyword>` for `<brand>` in `<location>`." |
| Brief only | "Build me the SEO brief and outline only. Do not draft yet." |
| Audit | "Audit `draft.md` against the E-E-A-T rubric and list publication blockers." |
| Keyword map | "Map the search intent and supporting questions for `<topic>`." |
| Safety review | "Review this clinic landing copy for medical claim risk and misleading language." |

### What you get back

The default output follows the seven-section contract above and marks every
unverified field:

- `[NEEDS CLIENT INPUT]` — a fact only the client can supply.
- `[NEEDS SOURCE VERIFICATION]` — a claim awaiting a checked source.
- `NOT MEDICALLY APPROVED` — missing required clinician review.

## How it works

The skill runs an eight-stage workflow and does not skip ahead:

1. **Understand the brief** — collect essentials or state assumptions.
2. **Search intent and keyword strategy** — build a keyword map.
3. **Evidence and source research** — verify sources, build a ledger.
4. **Build the article brief** — title, slug, meta, outline, links, media.
5. **Write the article** — natural language, disclosed limits, no hype.
6. **Demonstrate E-E-A-T honestly** — experience, expertise, authority,
   trust, each backed by evidence or disclosed as missing.
7. **On-page SEO** — headings, metadata, alt text, structured data.
8. **Final quality and safety audit** — score and hard stops.

Detailed templates live in [`references/`](references) and are loaded only
when the relevant stage runs.

## Quality gates

Each audit category scores `0`, `1`, or `2`, for a maximum of **20**:

| Score | Verdict |
| --- | --- |
| 18–20 | Strong draft, subject to human approval |
| 14–17 | Revise identified weaknesses |
| 10–13 | Substantial revision required |
| 0–9 | Do not recommend publication |

These **hard stops override any score**:

- Fabricated source, credential, testimonial, case study, or experience.
- Unsupported high-impact medical claim.
- Missing required clinician review.
- Privacy or consent violation involving patient material.
- A guarantee, permanence claim, or "suitable for everyone" claim.
- Structured data that misrepresents the visible page.

A high score never means Google will rank the page. See
[`references/audit-rubric.md`](references/audit-rubric.md).

## Customization

### Use it for another industry

1. Open [`references/medical-safety-checklist.md`](references/medical-safety-checklist.md).
2. Replace the clinical-claim rules with the regulated-claim rules for your
   domain (finance, legal, supplements, etc.).
3. Update the reviewer requirement to the correct qualified professional.
4. Keep the evidence ledger and hard stops unchanged — they are
   domain-neutral.

### Brand profile

The skill ships with an aesthetic-clinic profile. To rebrand:

- Update the brand and market references in `SKILL.md`.
- Replace the example in `examples/example-output.md`.
- Add brand-specific forbidden claims to the safety checklist.

### Tuning the rubric

Edit `references/audit-rubric.md` to change scoring anchors or add
categories. Keep the total at 20 or update the verdict thresholds in both
`SKILL.md` and the rubric so they stay in sync.

## Safety and disclaimers

This skill is an editorial aid, **not** medical, legal, or advertising
advice. It does not replace review by a qualified clinician or compliance
professional.

- Outputs may contain errors and must be verified by a human before
  publication.
- The skill cannot guarantee search rankings, traffic, or conversions.
- The authors accept no liability for content published using this skill.

See [`LICENSE`](LICENSE) for the full warranty disclaimer.

## Development

```bash
# Validate the skill package
python3 scripts/validate_skill.py .

# Lint markdown (optional)
npx markdownlint-cli2 "**/*.md"
```

CI runs the validator on every push and pull request.

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.
In short:

1. Fork and branch.
2. Keep `SKILL.md` lean; move detail into `references/`.
3. Run the validator and linter.
4. Open a pull request using the template.

## License

[MIT](LICENSE) © Contributors
