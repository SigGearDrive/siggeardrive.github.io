# Exoskeleton Joint Actuators and Gearboxes

## Application Overview

Powered exoskeletons and rehabilitation robots require compact joint-drive systems for hip, knee, ankle, shoulder, elbow and other assisted-motion axes. Each joint has a different human-interaction profile, range of motion, torque-speed cycle, installation envelope and safety requirement, so actuator selection must be based on the complete wearable system rather than torque alone.

SigGear supplies planetary and cycloidal joint-drive products that can be evaluated for exoskeleton prototypes, rehabilitation equipment and wearable-assistance mechanisms. Depending on the selected model, a configuration may combine a BLDC motor, precision reducer, encoder and driver.

## Main Selection Factors

### Assistance Torque and Motion Profile

Provide the required continuous assistance torque, peak torque, peak duration, joint speed, acceleration and complete motion cycle. Walking assistance, lifting support, rehabilitation training and static holding create different operating conditions.

### Size, Weight and Wearable Packaging

Specify the maximum outer diameter, axial thickness and mass for every joint position. Bearings, mounting brackets, covers, cables, connectors and human-interface structures must be included in the available envelope.

### Human Interaction and Mechanical Response

State the required mechanical response, allowable backlash, compliance strategy and power-off behavior. Transmission, structure, sensing and control must be evaluated together for the intended human-interaction mode.

### External Loads and Joint Alignment

Radial load, axial load, overturning moment and misalignment can be introduced by the wearable frame and the user's motion. These loads must be reviewed separately from actuator output torque.

### Holding, Brake and Power-Off Requirements

For gravity-loaded joints, specify the required holding mode, acceptable motion after power loss and brake requirement. A brake or self-holding function must not be assumed unless it is confirmed in the selected configuration and quotation.

### Encoder, Driver and Communication

Encoder, driver and communication functions vary by model and configuration. Confirm the required position, velocity and torque-control functions, as well as CAN, RS485 or other project-specific interfaces.

### Thermal, Acoustic and Duty-Cycle Conditions

Provide operating time, rest time, ambient temperature, cooling method, installation structure and any acoustic target. Noise, thermal performance and service life must be confirmed for the selected configuration and test condition; they must not be inferred from a general product-family statement.

### Safety and Validation Scope

The complete exoskeleton system requires project-specific risk assessment, control limits, mechanical stops, emergency behavior and validation. A component page does not establish medical-device approval or system-level safety compliance.

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

A cycloidal joint module may be considered when the selected model's torque, speed, backlash and installation characteristics match the wearable-joint requirement.

Neither transmission type should be selected from a general rule alone. Compare the complete torque-speed cycle, weight, external loads, mechanical response, thermal conditions, packaging and control architecture.

## Joint-by-Joint Evaluation

Hip and knee joints normally have different torque and structural-load conditions from ankle, shoulder and elbow axes. Prepare a separate requirement sheet for every joint rather than applying one actuator specification to the complete system.

Prototype validation should include representative users or test fixtures, repeated motion cycles, temperature monitoring, power-off behavior, mechanical stops, encoder behavior and controller-current limits under the project's safety procedure.

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

## Request an Exoskeleton Joint Selection Review

Please send the joint position, assistance mode, continuous torque, peak torque and duration, output speed, range of motion, voltage, size and weight limits, radial and axial loads, overturning moment, duty cycle, acoustic target, power-off and brake requirements, driver and communication requirements, prototype quantity and annual forecast.

**Wanrong Wang**  
International Sales, SigGear  
[wangwanrong@siggear.com](mailto:wangwanrong@siggear.com)

[Send Exoskeleton Joint Requirements](../contact.md){ .md-button .md-button--primary }
