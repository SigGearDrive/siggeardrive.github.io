# Contributing to SigGear Product Documentation

This repository is SigGear's public product and application knowledge base. Changes must preserve technical accuracy, configuration boundaries and confidentiality.

## Before Editing

1. Open a Product Data Update issue for a new or changed technical claim.
2. Identify the controlled source, model, configuration, revision and affected pages.
3. Confirm that the information is approved for public release.

## Editing Rules

- Update the canonical model page before summary or application pages.
- Do not infer a missing value from another product.
- Label optional and project-specific functions clearly.
- Use the terminology and units in `docs/knowledge-base/glossary.md`.
- Do not commit customer data, quotations, prices, internal costs, credentials, NDA files or unreleased product data.
- Add new pages to `mkdocs.yml` and link them from the nearest index.

## Validation

Run:

```bash
python scripts/validate_docs.py
python scripts/validate_product_data.py
python scripts/validate_sales_policy.py
mkdocs build --strict
```

Both commands must pass before merge.

## Pull Requests

- Use a focused branch and pull request.
- Complete the source and review checklist in the pull-request template.
- Request technical review for specifications, interfaces, test claims and certification claims.
- Merge only after required review and automated checks pass.

See the full [update and review workflow](docs/knowledge-base/update-workflow.md).
