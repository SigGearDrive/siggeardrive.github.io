# SigGear Product Master Data

This directory contains machine-readable records for public SigGear product pages.

## Principles

- One YAML record per canonical product model or series page.
- Public values are copied exactly, including units, ranges and tolerances.
- The canonical page and its record must be updated together.
- Records do not replace controlled drawings, test reports, quotations or technical agreements.
- Every record defines permitted preliminary sales use, required confirmations and prohibited shortcuts.
- Non-public technical sources remain in an approved private system.
- Customer data, prices, internal costs, credentials and unreleased product information are prohibited.

## Workflow

1. Update the canonical product page.
2. Update the matching record in `data/products/`.
3. Run `python scripts/validate_product_data.py`.
4. Obtain technical and content review before merge.

See `docs/knowledge-base/product-data-dictionary.md` for the field definitions.
