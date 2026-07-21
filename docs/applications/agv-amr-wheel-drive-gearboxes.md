# AGV and AMR Wheel Drive Gearboxes and Motors

## Application Overview

AGVs, AMRs, mobile service robots and compact transport platforms require wheel-drive systems matched to vehicle mass, wheel diameter, target speed, acceleration, gradeability, floor conditions and operating cycle. Motor selection should be based on the complete traction requirement rather than rated torque alone.

SigGear supplies compact hub gear motors and planetary transmission products that can be evaluated for mobile-robot wheel drives. The standard SG-2877 and SG-2878 catalog configurations combine a BLDC motor, planetary reduction mechanism and Hall sensors. An external controller is required unless a controller is specifically included in the quotation.

## Main Selection Factors

### Vehicle Mass and Payload

Provide the vehicle mass, maximum payload and expected load distribution. The drive system must be evaluated for the fully loaded condition, including acceleration, turning and slope operation.

### Wheel Diameter and Required Speed

Wheel diameter directly affects the relationship between motor speed, vehicle speed and wheel torque. Provide the actual rolling diameter, target continuous speed and maximum speed.

### Driven-Wheel Quantity

State the number of driven wheels and the mechanical arrangement. Required torque per wheel depends on the vehicle layout, load distribution and traction conditions.

### Acceleration and Gradeability

Provide the required acceleration, maximum slope, slope length and whether the vehicle must start or stop on the slope. Gradeability must be reviewed together with vehicle mass, wheel radius, traction and controller-current limits.

### Floor and Traction Conditions

Describe the operating surface, including smooth indoor floors, ramps, expansion joints, thresholds or outdoor surfaces. Wheel material, rolling resistance and available traction affect the required drive torque.

### Continuous and Peak Torque

Continuous torque must cover sustained travel and repeated duty cycles. Peak torque must be reviewed together with acceleration time, obstacle conditions, slope duration, controller current, battery voltage, cooling and ambient temperature.

### Braking and Holding

Specify stopping distance, parking behavior, emergency-stop requirements and whether the vehicle must hold position on a slope. A mechanical brake must not be assumed to be included unless it is confirmed in the selected configuration and quotation.

### Controller, Feedback and Communication

The standard SG-2877 and SG-2878 catalog configurations use Hall sensors and require an external controller. Integrated drivers, absolute encoders, CAN, RS485, EtherCAT and position or torque closed-loop control are not standard claims unless specifically included in the quotation.

### Environment and Duty Cycle

Provide operating time, rest time, start-stop frequency, ambient temperature, contamination exposure and required ingress protection. The published SG-2877 and SG-2878 catalog pages list IP67, but the complete vehicle-side sealing and installation must be reviewed separately.

## Published SigGear Hub Gear Motors

The following models can be used as starting points for engineering review:

| Model | Rated voltage | Rated power | Rated speed | Rated torque | Peak torque | Weight |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [SG-2877](../products/hub-gear-motors/sg2877.md) | 24 VDC | 45 W | 130 rpm ±10% | 3 Nm | 10 Nm | 780 ±20 g |
| [SG-2878](../products/hub-gear-motors/sg2878.md) | 24 VDC | 75 W | 110 rpm ±10% | 6 Nm | 18 Nm | 1100 ±20 g |

Both models use a 99 mm outer diameter and a 9.75:1 planetary reduction ratio. Final selection depends on wheel diameter, vehicle mass, driven-wheel quantity, speed, acceleration, slope, duty cycle and controller limits.

## Standard Configuration Boundaries

The published SG-2877 and SG-2878 standard configurations include:

- BLDC motor
- Planetary reduction mechanism
- Hall sensors
- Output shaft and mounting structure shown in the approved drawing

Unless explicitly included in the quotation, do not assume:

- Integrated driver
- Absolute encoder
- CAN, RS485 or EtherCAT communication
- Position or torque closed-loop control
- Wheel, tire or vehicle-side mounting hardware
- Mechanical brake

## Prototype and Customization Review

Depending on project requirements and engineering feasibility, SigGear can evaluate:

- Output-shaft and mounting-interface customization
- Cable and connector customization
- Wheel-drive assembly requirements
- External controller matching
- Customer branding and labeling

Customization availability depends on technical feasibility, prototype quantity and expected production volume.

## Request a Wheel Drive Selection Review

Please send the vehicle mass, maximum payload, wheel diameter, driven-wheel quantity, target continuous and maximum speed, acceleration, maximum slope and slope duration, floor conditions, operating voltage, duty cycle, braking and holding requirements, controller requirements, prototype quantity and annual forecast.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Send AGV or AMR Drive Requirements](../contact.md){ .md-button .md-button--primary }
