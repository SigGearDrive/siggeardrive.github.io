# SigGear Product Documentation

Official public product documentation and technical marketing site for Guangdong SigGear Drive Intelligent Technology Co., Ltd.

## Publishing rules

- Product pages are the primary source of public product specifications.
- Every model has one canonical product page.
- Unverified values are not published as confirmed specifications.
- CAD models, detailed drawings, noise-test records, and service-life data are supplied after application review and inquiry.
- Public contact: wangwanrong@siggear.com

## Knowledge-base maintenance

- Start with the [knowledge-base index](docs/knowledge-base/index.md) for product lookup, terminology, FAQs and documentation rules.
- Submit product-data changes with the Product Data Update issue template.
- Every technical claim must identify an approved source and configuration scope before publication.
- Run `python scripts/validate_docs.py` and `mkdocs build --strict` before merging documentation changes.
- Run `python scripts/validate_product_data.py` and `python scripts/validate_sales_policy.py` when product records or sales rules change.
- Use the [sales and inquiry guides](docs/sales/index.md) for public-safe qualification, matching and response workflows.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for the review and publishing workflow.
