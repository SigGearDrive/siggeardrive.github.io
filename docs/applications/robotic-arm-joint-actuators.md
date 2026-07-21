# Robotic Arm Joint Actuators and Gearboxes

## Application Overview

Robotic arms and collaborative automation systems require joint-drive solutions for base, shoulder, elbow, wrist and rotary-axis positions. Each axis has a different payload, reach, inertia, motion profile and installation envelope, so actuator selection must be based on the complete mechanism rather than output torque alone.

SigGear supplies planetary and cycloidal joint-drive products that can be evaluated for robotic arms, collaborative robots, research manipulators and compact automation axes. Depending on the selected model, a configuration may combine a BLDC motor, precision reducer, encoder and driver.

## Main Selection Factors

### Payload, Reach and Joint Position

Provide the payload, arm-link lengths, center-of-gravity locations and joint position. The required joint torque depends on the complete mechanism, posture, acceleration and external process forces.

### Continuous and Peak Torque

Continuous torque must cover sustained motion and holding conditions within the required duty cycle. Peak torque must be reviewed together with peak duration, controller current limit, acceleration profile, cooling and ambient conditions.

### Output Speed and Acceleration

Provide rated speed, maximum speed, acceleration, deceleration and motion cycle for every axis. A single maximum-speed value does not describe the complete operating requirement.

### Backlash, Positioning and Repeatability

State the allowable backlash, positioning accuracy and repeatability targets for the completed axis. Transmission, bearing arrangement, structural stiffness, encoder resolution, controller tuning and assembly tolerances must be evaluated together.

### Radial, Axial and Overturning Loads

Output bearings and mounting structures may experience radial load, axial load and overturning moment from the arm links, payload and external process forces. These structural loads must be reviewed separately from output torque.

### Holding, Brake and Safety Requirements

For vertical or gravity-loaded axes, specify the required holding mode, power-off behavior and brake requirement. A brake must not be assumed to be included unless it is confirmed in the selected configuration and quotation.

### Encoder, Driver and Communication

Encoder, driver and communication functions vary by model and configuration. Confirm the required position, velocity and torque-control functions, as well as CAN, RS485 or other project-specific interfaces.

### Thermal Conditions and Duty Cycle

Provide the motion cycle, operating time, holding time, rest time, ambient temperature, cooling method and installation structure. Peak torque and peak current must not be treated as continuous ratings.

## Candidate SigGear Products

The following published models can be used as starting points for engineering review. Final selection depends on the axis position and complete operating conditions.

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

A cycloidal joint module may be considered when the selected model's torque, speed, backlash and installation characteristics match the robotic-axis requirement.

Neither transmission type should be selected from a general rule alone. Compare the complete torque-speed cycle, payload inertia, external loads, positioning requirement, thermal conditions, size, weight and control architecture.

## Axis-by-Axis Evaluation

Base, shoulder and elbow axes normally have different torque and structural-load conditions from wrist and tool axes. Prepare a separate requirement sheet for every axis rather than applying one actuator specification to the complete robot.

Prototype validation should include representative payloads, repeated motion cycles, temperature monitoring, holding conditions, encoder behavior and controller-current limits.

## Prototype and Customization Support

Depending on the selected model and project scope, SigGear can evaluate:

- Motor, reducer, encoder and driver integration
- Reduction-ratio and output-interface customization
- Mounting and housing customization
- Cable and connector customization
- Brake integration after engineering review
- Communication and control configuration
- Customer branding and labeling

Customization availability depends on technical feasibility, prototype quantity and expected production volume.

## Request a Robotic Arm Joint Selection Review

Please send the axis position, payload, arm reach, center of gravity, continuous torque, peak torque and duration, output speed, acceleration profile, voltage, size and weight limits, radial and axial loads, overturning moment, backlash and positioning targets, duty cycle, brake requirement, driver and communication requirements, prototype quantity and annual forecast.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Send Robotic Arm Requirements](../contact.md){ .md-button .md-button--primary }
