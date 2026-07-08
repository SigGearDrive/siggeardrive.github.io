---
title: How to Calculate Torque for Robot Joint Gearbox Selection
description: Engineering guide for robot joint torque calculation, gearbox torque selection, reducer ratio, output speed, motor power, safety factor, radial load, and actuator sizing for robotics projects.
---

# How to Calculate Torque for Robot Joint Gearbox Selection

Correct torque calculation is one of the most important steps before selecting a robot joint gearbox, reducer, or integrated actuator module.

A gearbox that only meets the rated torque on paper may still fail if the project has high acceleration, impact load, radial load, poor bearing support, thermal overload, or an incorrect reduction ratio. This guide explains the main engineering factors to check before selecting a gearbox for robot joints, robot arms, humanoid robots, quadruped robots, grippers, AGV / AMR modules, and compact automation systems.

## Basic Torque Formula

The most common torque calculation is:

```text
Torque = Force × Distance
T = F × r
```

Where:

| Symbol | Meaning |
| --- | --- |
| T | Torque, usually in N·m |
| F | Force, usually in newtons |
| r | Lever arm or distance from rotation center, usually in meters |

For example, if a 50 N force acts at 0.1 m from the joint center:

```text
T = 50 N × 0.1 m = 5 N·m
```

This is only the static torque. Real robot joints often need additional torque for acceleration, impact, friction, gravity, and safety margin.

## Static Load Torque

For many robot joints, the first step is to estimate static load torque.

```text
Static torque = Load force × Distance from joint center
```

If the load is caused by mass under gravity:

```text
Load force = Mass × 9.81
Static torque = Mass × 9.81 × Distance
```

| Example | Value |
| --- | --- |
| Load mass | 5 kg |
| Gravity | 9.81 m/s² |
| Distance from joint center | 0.2 m |
| Static torque | 5 × 9.81 × 0.2 = 9.81 N·m |

In real selection, this result should not be used alone. Acceleration torque, shock load, duty cycle, friction, and safety factor should also be considered.

## Acceleration Torque

Robot joints often move dynamically. Acceleration torque depends on inertia and angular acceleration.

```text
Acceleration torque = Inertia × Angular acceleration
T = J × α
```

| Symbol | Meaning |
| --- | --- |
| J | Rotational inertia, kg·m² |
| α | Angular acceleration, rad/s² |

Acceleration torque becomes important when:

- The joint needs fast movement
- The robot has frequent start-stop cycles
- The arm or leg segment has high inertia
- The payload changes during operation
- The robot needs dynamic walking, jumping, or quick positioning

For humanoid robots, quadruped robots, and robot arms, acceleration torque can be a major part of the actual requirement.

## Total Required Output Torque

A practical estimate can be written as:

```text
Required output torque = (Static torque + Acceleration torque + Friction torque + External load torque) × Safety factor
```

A more conservative project estimate may also consider gearbox efficiency:

```text
Required gearbox output torque ≥ Required load torque / Efficiency
```

Typical safety factor depends on the application:

| Application Type | Suggested Consideration |
| --- | --- |
| Laboratory prototype | Lower safety factor may be acceptable for early testing. |
| Research robot | Consider repeated motion, unknown loads, and testing uncertainty. |
| Humanoid or quadruped robot | Higher margin is usually needed because of impact and dynamic motion. |
| Industrial automation | Consider duty cycle, lifetime, shock load, and production reliability. |
| Medical or safety-related device | Confirm requirements carefully with engineering testing and validation. |

## Rated Torque vs Peak Torque

Do not confuse rated torque and peak torque.

| Torque Type | Meaning | Selection Note |
| --- | --- | --- |
| Rated output torque | Torque that the gearbox or actuator can support continuously under specified conditions. | Use this for continuous load and duty cycle evaluation. |
| Peak output torque | Short-term overload torque. | Use this for acceleration, impact, emergency motion, or short transient loads. |
| Holding torque | Torque needed to hold a position. | Important for vertical joints, brakes, and power-off behavior. |
| Backdrive torque | Torque required to rotate the output from the load side. | Important for backdrivable robots, exoskeletons, and human interaction. |

A common mistake is selecting a joint only because the peak torque looks high. For real projects, rated torque, thermal condition, duty cycle, and lifetime are usually more important.

## Torque and Speed Must Be Checked Together

Gearbox selection is not only about torque. Output speed and motor speed must also match the application.

Output power can be estimated by:

```text
Power = Torque × Angular speed
P = T × ω
```

If output speed is given in rpm:

```text
ω = 2π × rpm / 60
P = T × 2π × rpm / 60
```

For example:

```text
T = 10 N·m
Speed = 100 rpm
P ≈ 10 × 2π × 100 / 60 ≈ 105 W
```

This means that if the customer asks for both high torque and high speed, the required motor power may increase quickly.

## Reduction Ratio Estimate

A simple reduction ratio estimate is:

```text
Gear ratio ≈ Motor speed / Required output speed
```

For example, if the motor speed is 3000 rpm and the required output speed is 100 rpm:

```text
Gear ratio ≈ 3000 / 100 = 30:1
```

However, the final ratio should also consider:

- Required output torque
- Motor torque curve
- Gearbox efficiency
- Required acceleration
- Backdrivability
- Noise and smoothness
- Space limit
- Backlash requirement
- Thermal condition

## Motor Torque and Gearbox Output Torque

A simplified estimate is:

```text
Output torque ≈ Motor torque × Gear ratio × Efficiency
```

For example:

```text
Motor torque = 0.5 N·m
Gear ratio = 20:1
Efficiency = 80%
Output torque ≈ 0.5 × 20 × 0.8 = 8 N·m
```

This is only a basic estimate. Real performance should be confirmed with motor curve, gearbox rating, thermal condition, control mode, and testing.

## Radial Load, Axial Load, and Moment Load

Torque is not the only mechanical risk. Many gearbox failures happen because the output side receives high radial load, axial load, or moment load.

| Load Type | Meaning | Example |
| --- | --- | --- |
| Radial load | Force perpendicular to the shaft. | Belt drive, pulley, tendon spool, wheel load. |
| Axial load | Force along the shaft direction. | Pressing, pulling, screw-type mechanisms. |
| Moment load | Bending load around the output bearing. | Offset arm, long lever, external impact. |

If the output shaft carries a pulley, wheel, tendon spool, or offset arm, external bearing support may be required. Do not select a gearbox only by torque rating when radial load is high.

## Application-Specific Notes

| Application | Important Torque Selection Points |
| --- | --- |
| Humanoid robot joint | Check rated torque, peak torque, walking impact, stiffness, backdrivability, thermal condition, and installation space. |
| Quadruped robot joint | Check peak torque, shock resistance, dynamic motion, duty cycle, and output bearing support. |
| Robot arm joint | Check payload, arm length, inertia, backlash, stiffness, and positioning accuracy. |
| Robotic gripper | Check finger force, linkage distance, speed, noise, and holding force. |
| AGV / AMR wheel drive | Check wheel radius, vehicle weight, slope, acceleration, duty cycle, and shock load. |
| Medical device drive | Check smoothness, low noise, lifetime, compact size, and safety margin. |

## Quick Information Needed for Gearbox Selection

Before selecting a gearbox or actuator, prepare the following information:

| Information | Example |
| --- | --- |
| Application | Humanoid joint, robot arm, gripper, AGV wheel drive, medical device. |
| Required output torque | Rated torque and peak torque. |
| Required output speed | Target rpm at output side. |
| Load distance | Lever arm, pulley radius, wheel radius, or center of mass distance. |
| Load condition | Static load, dynamic load, impact load, radial load, axial load. |
| Duty cycle | Continuous operation, intermittent operation, repeated start-stop. |
| Installation space | Diameter, length, thickness, mounting limit, cable routing. |
| Precision | Backlash, stiffness, repeatability, positioning accuracy. |
| Motor and control | Motor type, voltage, encoder, brake, CAN, RS485, EtherCAT, driver. |
| Quantity | Prototype quantity, first batch quantity, estimated annual quantity. |

## Common Selection Mistakes

Avoid these mistakes during early gearbox selection:

- Selecting only by peak torque
- Ignoring output speed and motor power
- Ignoring radial load or moment load
- Using static torque only for dynamic robots
- Forgetting safety factor
- Ignoring gearbox efficiency
- Ignoring thermal condition and duty cycle
- Choosing a high ratio that makes output speed too slow
- Choosing a low ratio that makes output torque too low
- Assuming all loads are centered on the output shaft

## Related SigGear Pages

- [How to Choose a Gearbox for Humanoid Robot Joints](humanoid-robot-joint-gearbox-selection-guide.md)
- [Robot Joint Gearbox Selection Guide](robot-joint-gearbox-selection-guide.md)
- [Planetary Gearbox Selection Guide](planetary-gearbox-selection-guide.md)
- [Cycloidal Reducer for Humanoid Robot Joints](../Applications/humanoid-robot-joint-reducer.md)
- [Custom Robotic Joint Actuator and OEM Gearbox Solutions](../custom-robotic-joint-actuator-oem-gearbox-solutions.md)
- [Factory Capability, Quality Control, and OEM / ODM Support](../factory-capability-quality-oem-odm.md)

## Request Torque Evaluation, CAD, Sample, or Quote

If you are not sure how much torque your robot joint, actuator, gripper, or gearbox requires, send your application details to SigGear for preliminary evaluation.

Please include load weight, lever arm, output speed, duty cycle, installation space, radial load, axial load, motor requirement, control interface, and estimated quantity.

[Request CAD, Datasheet, Sample, or Quote](../request-cad-sample-quote.md)

**Website:** https://www.siggear.com  
**Email:** [wangwanrong984@gmail.com](mailto:wangwanrong984@gmail.com)  
**Products:** Robot joint gearboxes / compact reducers / planetary gearboxes / cycloidal robotic joint modules / custom actuators
