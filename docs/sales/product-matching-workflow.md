# SigGear Product Matching Workflow

Use this workflow to create a preliminary shortlist. Do not describe a product as a perfect match until the complete requirement and ordered configuration have been reviewed.

## Step 1: Identify the Required Architecture

| Customer need | Starting product family |
| --- | --- |
| Motor, reducer, encoder and driver in one compact robot joint | [Robot joint actuators](../products/robot-joint-actuators/index.md) |
| Compact high-torque joint using cycloidal transmission | [Cycloidal joint modules](../products/cycloidal-joint-modules/index.md) |
| Separate precision reducer for integration with a motor | [Planetary gearboxes](../products/planetary-gearboxes/index.md) |
| Miniature motor and gearbox assembly | [Micro gear motors](../products/micro-gear-motors/index.md) |
| Flat motor or short-axial joint drive | [Flat BLDC motors and joint drives](../products/flat-bldc-motors/index.md) |
| Compact wheel or hub drive | [Hub gear motors](../products/hub-gear-motors/index.md) |

## Step 2: Screen Torque and Speed

Compare continuous torque with rated torque. Compare the customer's required peak torque together with peak duration, current limit, duty cycle and cooling.

Never use peak torque as the only selection value. A candidate must satisfy the complete torque-speed cycle.

## Step 3: Screen Mechanical Integration

Check:

- Outer diameter, thickness, length and mass
- Reduction ratio
- Mounting interface and shaft
- Radial, axial and overturning loads
- Backlash, accuracy and repeatability
- Shock, impact and structural conditions

External loads must be reviewed separately from output torque. Significant cantilevered or tendon loads may require additional bearing support.

## Step 4: Screen Electrical and Control Requirements

Confirm:

- Operating voltage and current limits
- Driver inclusion
- Encoder or Hall-sensor configuration
- Position, velocity and torque-control requirements
- CAN, RS485, EtherCAT or other interface
- Protocol, baud rate, command set and feedback data
- Brake, holding and power-off behavior

An interface name alone does not confirm protocol compatibility.

## Step 5: Screen Environment and Validation Needs

Check duty cycle, ambient temperature, cooling, ingress protection, noise, vibration, service life and required test evidence. Do not transfer a product-level IP rating to the complete customer machine.

## Step 6: Screen Project Readiness

Confirm prototype quantity, annual forecast, project stage, selection date, required documents and delivery destination. These inputs affect configuration, engineering review, quotation and freight evaluation.

## Matching Outcomes

### Standard Candidate

A canonical public model is a reasonable starting point and no unconfirmed modification is required. The quotation must still state the exact configuration.

### Configured Standard Product

The mechanical model may be standard, but driver, encoder, cable, connector, communication or firmware must be selected and confirmed.

### Custom Engineering Project

The customer requires a changed ratio, shaft, interface, housing, electronics or performance target. Engineering feasibility, development scope, cost and lead time require separate review.

### No Published Match

State this clearly. Do not force-fit the closest model or invent an unreleased solution.

## Final Check

Before recommending a model, read its canonical product page and the [sales usage and review status](../knowledge-base/sales-usage-and-review-status.md). If the requirement conflicts with a prohibited shortcut, stop and request engineering review.

