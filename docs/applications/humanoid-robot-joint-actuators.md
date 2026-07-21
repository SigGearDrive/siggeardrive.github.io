# Humanoid Robot Joint Actuators

## Application Overview

Humanoid robots require compact joint actuators for positions such as the shoulder, elbow, wrist, hip, knee and ankle. Each joint has a different load case, motion cycle, installation envelope and control requirement, so actuator selection must be based on the complete operating condition rather than torque alone.

SigGear supplies planetary and cycloidal joint-drive products for humanoid robot development. Available configurations may combine a BLDC motor, precision reducer, encoder and driver, depending on the selected model.

## Main Selection Factors

### Continuous and Peak Torque

Continuous torque must cover the sustained load and motion cycle. Peak torque must be evaluated together with the required duration, controller current limit, duty cycle, cooling and ambient conditions.

### Output Speed

Required joint speed depends on the robot motion profile, reduction ratio and motor operating range. Higher peak speed does not replace verification of continuous operating conditions.

### Size and Weight

Provide the maximum allowable outer diameter, axial thickness and mass for each joint position. Cable routing, bearings, mounting structures and covers must also be included in the available installation space.

### External Loads

Radial load, axial load, overturning moment and shock conditions affect the bearing and structural design. These loads must be reviewed separately from output torque.

### Position Feedback and Control

Encoder, driver and communication requirements vary by model and configuration. Confirm the required position, velocity and torque-control functions, as well as CAN, RS485 or other communication interfaces, during project review.

### Thermal and Duty-Cycle Conditions

Provide the motion cycle, operating time, rest time, ambient temperature, cooling method and installation structure. Peak torque and current values must not be treated as continuous ratings.

## Candidate SigGear Joint Products

The following published models can be considered as starting points. Final selection requires engineering review.

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver options depend on selected configuration |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver options depend on selected configuration |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and no integrated driver |

## Planetary or Cycloidal Joint Drive

A planetary joint actuator may be considered when compact integration, output speed and a broad range of motor-and-driver configurations are important.

A cycloidal joint module may be considered when the application requires a compact high-torque transmission and the selected model's speed, backlash and installation characteristics match the joint requirement.

Neither transmission type should be selected from a general rule alone. Compare the complete torque-speed cycle, external loads, backlash requirement, thermal conditions, size, weight and control architecture.

## Joint-by-Joint Review

For each humanoid joint, provide a separate requirement set. Shoulder, hip and knee joints often have different torque and structural-load conditions from elbow, wrist and ankle joints. A single actuator model should not be assumed suitable for every position without calculation and prototype testing.

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Communication and control configuration
- Customer branding and labeling

Customization availability depends on technical feasibility, prototype quantity and expected production volume.

## Request a Joint Selection Review

Please send the robot joint position, continuous torque, peak torque and duration, output speed, voltage, size and weight limits, external loads, duty cycle, driver and communication requirements, prototype quantity and annual forecast.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Send Humanoid Joint Requirements](../contact.md){ .md-button .md-button--primary }
