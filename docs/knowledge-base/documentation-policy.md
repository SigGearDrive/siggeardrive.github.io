# SigGear Documentation Policy

This policy defines what can be published, how technical claims are supported and which page wins when information differs.

## Purpose

The documentation must be accurate enough for preliminary product selection, clear enough for international customers and structured enough for reliable human and AI retrieval. It must not expose confidential business or customer information.

## Source Hierarchy

Use the highest available source in this order:

1. Released model-specific specification or controlled engineering drawing
2. Approved model- and configuration-specific test report
3. Current certificate or third-party verification document within its stated scope
4. Written engineering confirmation identifying the exact model and configuration
5. Approved product catalog derived from the sources above

Sales messages, marketplace listings, competitor pages, customer statements and AI-generated text are not technical sources of truth.

## Claim Classes

| Class | Example | Publication requirement |
| --- | --- | --- |
| Model-specific specification | Torque, speed, ratio, dimensions, load rating | Exact model, unit, source and configuration scope verified |
| Configuration-dependent function | Driver, encoder, CAN, RS485, EtherCAT, brake | Included hardware and firmware scope stated; optional functions labeled |
| Test-based performance | Noise, temperature rise, efficiency, service life | Test method, sample configuration and conditions available |
| Certification claim | ISO, IATF, EMC or product conformity | Holder, scope, standard and applicable models checked |
| General engineering guidance | Selection factors and definitions | Written as guidance, not as a guaranteed product result |

## Canonical Page Rules

- Each published model or series has one canonical product page.
- Index, application and FAQ pages link to the canonical page instead of creating an independent specification source.
- Summary tables may repeat a small number of selection values, but they must link to the canonical page and be updated in the same pull request.
- A family-level statement must not be applied automatically to every model.
- Optional functions must be labeled `optional`, `project-specific` or `subject to configuration confirmation`.

## Conflict Handling

When two sources or pages disagree:

1. Stop publication of the disputed value.
2. Record the exact model, field, values and source revisions in a Product Data Update issue.
3. Ask the responsible engineering or product role to identify the current controlled source.
4. Update every affected summary and canonical page in one change.
5. Preserve the decision in the issue or pull request history.

Do not average conflicting values, choose the newest-looking file automatically or publish the more favorable claim.

## Public and Private Content Boundary

This public repository may contain approved product information, application guidance, selection guidance, public company facts and public contact information.

It must not contain:

- Customer names, addresses, messages, requirements or drawings without explicit publication approval
- Prices, discounts, payment terms, internal MOQ rules or internal quotation strategy
- Internal costs, margins, supplier identities or purchasing records
- Unreleased models, uncontrolled drawings or confidential test reports
- NDA-controlled files, credentials, API keys or private system links
- Personal telephone numbers or messaging accounts without explicit approval

## AI-Assisted Writing Rule

AI can organize, translate, summarize and check documentation, but it must not invent product values, fill missing specifications, infer compatibility or convert an optional feature into a standard claim. Every technical value still requires an approved human-verifiable source.

## Language Rule

The public documentation language is English. Use the model spelling, terminology and units defined in the [glossary](glossary.md). Write concise factual statements and distinguish confirmed specifications from selection guidance.

