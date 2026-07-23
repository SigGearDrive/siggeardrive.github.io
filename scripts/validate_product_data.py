#!/usr/bin/env python3
"""Validate machine-readable product records against canonical public pages."""

from __future__ import annotations

import sys
import re
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PRODUCT_DATA = ROOT / "data" / "products"
PRODUCT_DOCS = ROOT / "docs" / "products"

REQUIRED_FIELDS = {
    "schema_version",
    "record_id",
    "record_type",
    "display_name",
    "product_family",
    "canonical_page",
    "public_page_status",
    "record_status",
    "configuration_summary",
    "published_specifications",
    "source_control",
    "inventory_checked_on",
}

ALLOWED_RECORD_TYPES = {"model", "series"}
ALLOWED_PUBLIC_STATUSES = {"draft", "published", "retired"}
ALLOWED_RECORD_STATUSES = {"draft_inventory", "published_inventory", "superseded"}
ALLOWED_PRODUCT_FAMILIES = {
    "robot_joint_actuator",
    "cycloidal_joint_module",
    "planetary_gearbox",
    "hub_gear_motor",
}
RECORD_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CLAIM_KEY_RE = re.compile(r"^[a-z0-9]+(?:_[a-z0-9]+)*$")


def product_pages() -> set[Path]:
    return {
        path.resolve()
        for path in PRODUCT_DOCS.rglob("*.md")
        if path.name != "index.md"
    }


def load_record(path: Path, errors: list[str]) -> dict | None:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return None
    if not isinstance(data, dict):
        errors.append(f"{path.relative_to(ROOT)}: record must be a YAML mapping")
        return None
    return data


def validate_record(path: Path, data: dict, errors: list[str]) -> Path | None:
    label = path.relative_to(ROOT)
    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        errors.append(f"{label}: missing required fields: {', '.join(missing)}")

    record_id = data.get("record_id")
    if record_id != path.stem:
        errors.append(f"{label}: record_id must match filename stem")
    if not isinstance(record_id, str) or not RECORD_ID_RE.fullmatch(record_id):
        errors.append(f"{label}: record_id must use lowercase kebab-case")

    if data.get("schema_version") != 1:
        errors.append(f"{label}: schema_version must be 1")

    record_type = data.get("record_type")
    if record_type not in ALLOWED_RECORD_TYPES:
        errors.append(f"{label}: invalid record_type: {record_type}")
    if record_type == "model" and not data.get("model"):
        errors.append(f"{label}: model records require a model field")

    if data.get("public_page_status") not in ALLOWED_PUBLIC_STATUSES:
        errors.append(f"{label}: invalid public_page_status")
    if data.get("record_status") not in ALLOWED_RECORD_STATUSES:
        errors.append(f"{label}: invalid record_status")
    if data.get("product_family") not in ALLOWED_PRODUCT_FAMILIES:
        errors.append(f"{label}: invalid product_family")

    inventory_date = data.get("inventory_checked_on")
    try:
        date.fromisoformat(inventory_date)
    except (TypeError, ValueError):
        errors.append(f"{label}: inventory_checked_on must use YYYY-MM-DD")

    if not isinstance(data.get("configuration_summary"), str) or not data["configuration_summary"].strip():
        errors.append(f"{label}: configuration_summary must be a non-empty string")

    canonical_value = data.get("canonical_page")
    if not isinstance(canonical_value, str):
        errors.append(f"{label}: canonical_page must be a string")
        return None

    canonical = (ROOT / canonical_value).resolve()
    try:
        canonical.relative_to(PRODUCT_DOCS.resolve())
    except ValueError:
        errors.append(f"{label}: canonical_page must be inside docs/products")
        return None
    if not canonical.exists():
        errors.append(f"{label}: canonical_page does not exist: {canonical_value}")
        return canonical

    page_text = canonical.read_text(encoding="utf-8")
    identity = data.get("model") or data.get("display_name")
    if not isinstance(identity, str) or identity not in page_text:
        errors.append(f"{label}: product identity is missing from canonical page")

    claims = data.get("published_specifications")
    if not isinstance(claims, dict) or not claims:
        errors.append(f"{label}: published_specifications must be a non-empty mapping")
    else:
        for key, value in claims.items():
            if not isinstance(key, str) or not CLAIM_KEY_RE.fullmatch(key):
                errors.append(f"{label}: published specification keys must use snake_case: {key}")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}: published_specifications.{key} must be a non-empty string")
            elif value not in page_text:
                errors.append(
                    f"{label}: published_specifications.{key} value is not present on canonical page: {value}"
                )

    variants = data.get("published_variants", {})
    if not isinstance(variants, dict):
        errors.append(f"{label}: published_variants must be a mapping")
    else:
        for variant, value in variants.items():
            if str(variant) not in page_text or str(value) not in page_text:
                errors.append(f"{label}: published variant is not present on canonical page: {variant}: {value}")

    source_control = data.get("source_control")
    if not isinstance(source_control, dict):
        errors.append(f"{label}: source_control must be a mapping")
    else:
        if source_control.get("public_claim_source") != "canonical_page":
            errors.append(f"{label}: public_claim_source must be canonical_page")
        if source_control.get("technical_source_status") != "not_recorded_in_public_repository":
            errors.append(f"{label}: technical_source_status must preserve the public/private boundary")

    return canonical


def main() -> int:
    errors: list[str] = []
    record_paths = sorted(PRODUCT_DATA.glob("*.yml"))
    if not record_paths:
        errors.append("No product records found")

    record_ids: set[str] = set()
    models: set[str] = set()
    covered_pages: set[Path] = set()

    for path in record_paths:
        data = load_record(path, errors)
        if data is None:
            continue

        record_id = data.get("record_id")
        if isinstance(record_id, str):
            if record_id in record_ids:
                errors.append(f"{path.relative_to(ROOT)}: duplicate record_id: {record_id}")
            record_ids.add(record_id)

        model = data.get("model")
        if isinstance(model, str):
            if model in models:
                errors.append(f"{path.relative_to(ROOT)}: duplicate model: {model}")
            models.add(model)

        canonical = validate_record(path, data, errors)
        if canonical is not None:
            if canonical in covered_pages:
                errors.append(f"{path.relative_to(ROOT)}: canonical page is covered by more than one record")
            covered_pages.add(canonical)

    missing_records = sorted(product_pages() - covered_pages)
    for page in missing_records:
        errors.append(f"{page.relative_to(ROOT)}: canonical product page has no master-data record")

    extra_records = sorted(covered_pages - product_pages())
    for page in extra_records:
        errors.append(f"{page.relative_to(ROOT)}: master-data record targets a non-canonical page")

    if errors:
        print("Product data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Product data validation passed: {len(record_paths)} records cover "
        f"{len(covered_pages)} canonical product pages."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
