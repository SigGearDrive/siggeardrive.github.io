# SigGear Knowledge Base Update and Review Workflow

Use this workflow for new models, specification changes, new application pages, corrected claims and documentation maintenance.

## Content Status

| Status | Meaning |
| --- | --- |
| Proposed | A change request exists but source material has not been confirmed |
| Technical review | Engineering or product owner is checking model, configuration, values and evidence |
| Content review | Technical facts are fixed; English, structure, links and terminology are being checked |
| Publish ready | Required reviews and automated checks are complete |
| Published | The change is merged to `main` and deployed |
| Superseded | A newer controlled page or revision replaces the old information |

## Roles

| Role | Responsibility |
| --- | --- |
| Requester | Describes the change and supplies the source file or exact source reference |
| Technical reviewer | Confirms the model, configuration, values, units, test conditions and claim scope |
| Content reviewer | Checks English, terminology, search terms, navigation, cross-links and confidentiality |
| Maintainer | Confirms automated checks, merges the pull request and verifies deployment |

One person may perform more than one role, but technical review must be explicit for model-specific claims.

## Update Procedure

1. Open a Product Data Update issue.
2. Identify the model, product family, requested change and affected pages.
3. Cite the controlled source, including document name, revision and date when available.
4. Confirm that the source is approved for public use.
5. Update the canonical product page first.
6. Update every summary table, application page, FAQ or index that repeats the changed information.
7. Use the model spelling, terminology and units in the [glossary](glossary.md).
8. Run the documentation validator and strict MkDocs build.
9. Obtain technical and content review in the pull request.
10. Merge to `main` and verify the deployed page and search result.

## New Product Page Minimum Content

A new model page should include:

- Exact model name and product type
- Product overview without unsupported superlatives
- Included and optional configuration boundaries
- Key specifications with units
- Rated and peak conditions where applicable
- Mechanical, electrical, encoder, driver and communication sections as applicable
- External-load and thermal limitations where supported
- Product images with descriptive alternative text
- Application guidance
- Inquiry information and links to related pages

Missing data must be omitted or clearly marked as requiring confirmation. Do not estimate it from a similar model.

## Search and Retrieval Checklist

- Use the official model number in the H1 heading and body.
- Include common product-family and application terms naturally.
- Link the model from the [product model index](product-model-index.md).
- Add the page to `mkdocs.yml` navigation.
- Link to related product, application and selection pages.
- Avoid duplicate pages targeting the same model and intent.

## Required Checks

Run locally before review:

```bash
python scripts/validate_docs.py
mkdocs build --strict
```

The pull-request workflow repeats these checks automatically.

## Urgent Corrections

For a safety-relevant, materially misleading or confidential disclosure:

1. Remove or correct the public statement as the immediate priority.
2. Record the reason and affected pages.
3. Complete technical review before adding a replacement claim.
4. Check cached summaries and other pages for the same statement.

