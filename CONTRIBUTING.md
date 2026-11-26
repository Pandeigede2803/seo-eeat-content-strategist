# Contributing

Thanks for improving the SEO E-E-A-T Content Strategist skill.

## Before you start

- Open an issue for anything larger than a typo or small clarification.
- For safety-rule changes, explain the risk being addressed.
- Never weaken the anti-fabrication rules.

## Development workflow

1. Fork the repository and create a branch:

   ```bash
   git checkout -b feat/short-description
   ```

2. Make your change. Keep `SKILL.md` lean (under ~20 KB); move expanded
   material into `references/` or `assets/`.

3. Validate:

   ```bash
   python3 scripts/validate_skill.py .
   npx markdownlint-cli2 "**/*.md"
   ```

4. Commit with a conventional message:

   ```text
   feat: add supplement-industry safety profile
   fix: correct broken rubric link
   docs: clarify installation on Windows
   ```

5. Push and open a pull request using the template.

## Style guide

- Write in English, in the imperative mood for instructions.
- One sentence per line in markdown source (easier diffs).
- Use tables for structured rules; use prose for reasoning.
- Prefer "must" and "never" for safety rules.
- Avoid marketing adjectives in the skill itself.
- Keep examples illustrative and free of real patient claims.

## Adding a reference file

1. Create the file under `references/`.
2. Add one line to the reference table at the bottom of `SKILL.md`.
3. Explain when the agent should load it.

## Adding an industry profile

1. Copy the structure of `references/medical-safety-checklist.md`.
2. Name it `references/<industry>-safety-checklist.md`.
3. Document the clinician or professional reviewer requirement.
4. Add an example under `examples/`.

## Review checklist

- [ ] `SKILL.md` frontmatter is valid and `name` matches the folder.
- [ ] Description states what the skill does and when to use it.
- [ ] All relative links resolve.
- [ ] No fabricated examples, sources, or credentials.
- [ ] Safety rules remain intact or are strengthened.
- [ ] `CHANGELOG.md` updated for user-visible changes.

## Code of conduct

Be respectful and constructive. Harassment and discrimination are not
tolerated. Maintainers may remove contributions that compromise the
skill's safety guarantees.
