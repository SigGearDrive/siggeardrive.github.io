# SigGear Product Data Dictionary

SigGear product master-data records provide a machine-readable inventory of the claims already published on canonical product pages. They support GitHub search, AI-assisted retrieval and automated consistency checks.

## Record Location

Product records are stored in `data/products/`. One YAML file represents one published model or series.

## Record Fields

| Field | Meaning |
| --- | --- |
| `schema_version` | Version of the record structure |
| `record_id` | Stable lowercase identifier matching the YAML filename |
| `record_type` | `model` or `series` |
| `model` | Official model number for a model record |
| `display_name` | Human-readable product or series name |
| `product_family` | Controlled product-family identifier |
| `canonical_page` | Unique public page for the model or series |
| `public_page_status` | Publication state of the canonical page |
| `record_status` | Status of the structured inventory record |
| `configuration_summary` | Boundary statement for included or configuration-dependent components |
| `published_specifications` | Exact public value strings mirrored from the canonical page |
| `source_control` | Public claim source and handling of non-public technical sources |
| `inventory_checked_on` | Date the record was compared with the public page |

## Status Meanings

`public_page_status: published` means the canonical page is publicly available. It does not replace a quotation or technical agreement.

`record_status: published_inventory` means the YAML record mirrors the current public page. It does not independently certify the engineering value.

`technical_source_status: not_recorded_in_public_repository` means drawings, test records or internal approvals are intentionally not stored in this public repository. It does not mean that no technical source exists.

## Exact-String Rule

Values in `published_specifications` preserve the text shown on the canonical page, including ranges, tolerances and units. For example, `24–48 VDC` must not be silently changed to `48 V` or converted into a different rating.

The automated validator checks that every recorded value still appears on its canonical page. If a page specification changes, the corresponding YAML record must change in the same pull request.

## Configuration Boundaries

The product record must not turn an optional function into a standard claim. Driver, encoder, brake, CAN, RS485, EtherCAT and control-mode availability remain configuration-specific unless the canonical model page explicitly states otherwise.

## Source Boundary

These records contain public product data only. Customer files, prices, internal costs, supplier information, unreleased products, private drawings, restricted test reports and NDA material must not be added.

## Validation

Run:

```bash
python scripts/validate_product_data.py
```

The check verifies required fields, unique identifiers, canonical-page coverage and exact published-claim synchronization.

