# Quadruped Robot Joint Gearboxes and Actuators

## Application Overview

Quadruped robots require compact joint-drive systems for leg axes such as hip, knee and ankle joints. Walking, trotting, turning, standing and impact recovery create different torque-speed cycles, so actuator selection must be based on the complete gait profile rather than a single peak-torque value.

SigGear supplies planetary and cycloidal joint-drive products that can be evaluated for quadruped robot development. Depending on the selected model, a configuration may combine a BLDC motor, precision reducer, encoder and driver.

## Main Selection Factors

### Continuous and Peak Torque

Continuous torque must cover the sustained load during standing and repeated gait cycles. Peak torque must be reviewed together with peak duration, controller current limit, duty cycle, cooling and ambient conditions.

### Output Speed and Gait Profile

Provide the required joint speed for walking, trotting, jumping or recovery motions. The complete speed and acceleration profile is more useful than a single maximum-speed target.

### Size and Weight

For each leg joint, specify the maximum outer diameter, axial thickness and mass. Bearings, output structures, cable routing, covers and fasteners must be included in the available installation envelope.

### Radial, Axial and Impact Loads

Leg joints can experience radial load, axial load, overturning moment, shock and repeated landing impact. These structural loads must be reviewed separately from output torque.

### Backlash, Positioning and Mechanical Response

State the allowable backlash, positioning requirement and mechanical-response target. The selected transmission, bearing structure, encoder and controller must be evaluated together.

### Encoder, Driver and Communication

Encoder, driver and communication functions vary by model and configuration. Confirm the required position, velocity and torque-control functions, as well as CAN, RS485 or other project-specific interfaces.

### Thermal Conditions and Duty Cycle

Provide the gait cycle, operating time, rest time, ambient temperature, cooling method and installation structure. Peak torque and peak current must not be treated as continuous ratings.

## Candidate SigGear Products

The following published models can be used as starting points for engineering review. Final selection depends on the joint position and complete operating conditions.

| Model | Transmission | Rated torque | Peak torque | Rated output speed | Configuration note |
| --- | --- | ---: | ---: | ---: | --- |
| [SG-6010C](../products/robot-joint-actuators/sg6010c.md) | Planetary | 6 Nm | 18 Nm | 310 rpm | Driver options depend on selected configuration |
| [SG-6010D](../products/robot-joint-actuators/sg6010d.md) | Planetary | 16 Nm | 50 Nm | 100 rpm | Available with or without integrated driver |
| [SG-8021](../products/robot-joint-actuators/sg8021.md) | Planetary | 10 Nm | 30 Nm | 160 rpm | Driver options depend on selected configuration |
| [CPM-100-25](../products/cycloidal-joint-modules/cpm100-25.md) | Cycloidal pinwheel | 25 Nm | 75 Nm | 60 rpm | Available with or without integrated driver |
| [CPM-80-25](../products/cycloidal-joint-modules/cpm80-25.md) | Cycloidal pinwheel | 10 Nm | 50 Nm | 120 rpm | Available with or without integrated driver |
| [CPM-78-39](../products/cycloidal-joint-modules/cpm78-39.md) | Cycloidal pinwheel | 20 Nm | 52 Nm | 48 rpm | Standard catalog configuration uses Hall sensors and no integrated driver |

## Planetary or Cycloidal Joint Drive

A planetary joint actuator may be considered when compact integration, output speed and flexible motor-and-driver configuration are important.

A cycloidal joint module may be considered when the selected model's torque, speed, backlash and installation characteristics match the leg-joint requirement.

Neither transmission type should be selected from a general rule alone. Compare the full torque-speed cycle, impact loads, positioning requirement, thermal conditions, size, weight and control architecture.

## Joint-by-Joint Evaluation

Hip, knee and ankle axes normally have different torque, speed, structural-load and packaging requirements. Prepare a separate requirement sheet for every joint position instead of applying one actuator specification to the complete robot.

Prototype testing should include repeated gait cycles, temperature monitoring, impact conditions, encoder behavior and controller-current limits.

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Communication and control configuration
- Customer branding and labeling

Customization availability depends on technical feasibility, prototype quantity and expected production volume.

## Request a Quadruped Joint Selection Review

Please send the robot mass, joint position, continuous torque, peak torque and duration, output speed, gait profile, voltage, size and weight limits, radial and axial loads, impact conditions, duty cycle, driver and communication requirements, prototype quantity and annual forecast.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Send Quadruped Joint Requirements](../contact.md){ .md-button .md-button--primary }
