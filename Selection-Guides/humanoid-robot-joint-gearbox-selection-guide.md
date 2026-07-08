---
title: How to Choose a Gearbox for Humanoid Robot Joints
description: Engineering guide for selecting humanoid robot joint gearboxes, cycloidal reducers, planetary gearboxes, compact robotic joint actuators, torque, speed, backlash, backdrivability, and OEM customization.
---

# How to Choose a Gearbox for Humanoid Robot Joints

Selecting a gearbox for humanoid robot joints is not only about rated torque. Engineers also need to evaluate output speed, peak load, backlash, stiffness, backdrivability, installation space, weight, thermal condition, motor matching, encoder feedback, control interface, and production requirements.

This guide helps robotics teams evaluate gearbox and actuator options for humanoid robot hips, knees, ankles, shoulders, elbows, wrists, and compact auxiliary joints.

## Key Selection Factors

| Factor | Why It Matters for Humanoid Robots |
| --- | --- |
| Rated output torque | Determines whether the joint can continuously support the required motion and load. |
| Peak output torque | Important for acceleration, impact, walking, standing recovery, and dynamic movement. |
| Output speed | Affects walking speed, arm movement speed, response time, and control performance. |
| Backlash | Influences positioning accuracy, joint stability, and control smoothness. |
| Stiffness | Helps maintain stable posture and accurate motion under load. |
| Backdrivability | Important for some joints that need compliance, manual movement, or safer interaction. |
| Installation space | Humanoid robots usually have strict diameter, thickness, length, and cable routing limits. |
| Weight | Lower actuator weight can improve whole-body dynamics and energy efficiency. |
| Motor and encoder matching | Motor power, encoder feedback, brake, and driver configuration affect control performance. |
| Duty cycle and thermal condition | Walking and repeated joint motion can create heat and long-duration load. |

## Cycloidal Reducer vs Planetary Gearbox for Humanoid Joints

Both cycloidal reducers and planetary gearboxes can be used in humanoid robot joints. The best choice depends on the joint position and engineering priority.

| Gearbox Type | Typical Advantage | Typical Consideration | Suitable Joint Examples |
| --- | --- | --- | --- |
| Compact cycloidal reducer | High torque density, shock resistance, compact axial structure, low backlash potential. | May require careful motor and interface integration. | Hip, knee, shoulder, elbow, high-load joints. |
| Planetary gearbox | Compact structure, higher speed options, mature motor integration, flexible size range. | Backlash, load capacity, and stiffness must be checked carefully. | Wrist, elbow, gripper, lightweight arm, auxiliary joints. |
| Integrated robotic joint module | Faster prototype integration with reducer, motor, encoder, driver, and communication option. | Electrical interface, firmware, and mechanical interface should be confirmed before design freeze. | Prototype humanoid robot joints and research platforms. |

## Joint-by-Joint Selection Notes

| Humanoid Joint | Common Requirement | Gearbox Selection Focus |
| --- | --- | --- |
| Hip joint | High torque, high peak load, strong structure, impact resistance. | Cycloidal or high-torque compact actuator; confirm peak torque, stiffness, bearing support, and thermal condition. |
| Knee joint | High torque during walking, standing, and load support. | Rated torque, peak torque, shock resistance, duty cycle, and output speed must be evaluated together. |
| Ankle joint | Compact size, impact load, balance control, sometimes compliance. | Backlash, stiffness, backdrivability, radial load, and compact installation space are important. |
| Shoulder joint | Medium to high torque, compact arm layout, smooth movement. | Torque density, thickness, output flange, cable routing, and weight should be balanced. |
| Elbow joint | Moderate torque, smooth rotation, compact size. | Planetary or compact cycloidal solution depending on torque and backlash requirements. |
| Wrist joint | Lower torque, small size, higher speed, low weight. | Miniature planetary gearbox or compact integrated actuator may be suitable. |

## Torque and Speed Should Be Checked Together

A common mistake is to choose a gearbox only by rated torque. For humanoid robots, output torque and output speed must be evaluated together.

For example, a joint may require high torque for standing support, but it also needs enough speed for dynamic motion. If the reduction ratio is too high, torque may increase but output speed may become too low. If the reduction ratio is too low, output speed may be enough but the motor may not provide enough torque.

Before selecting a model, define:

- Continuous output torque
- Peak output torque
- Required output speed
- Motion profile
- Duty cycle
- Expected load and impact condition
- Available motor voltage and power

## Backlash, Stiffness, and Control Accuracy

Low backlash helps improve joint positioning and control stability. However, backlash is not the only precision factor. Stiffness, encoder resolution, motor control quality, mechanical structure, and load condition also affect actual robot performance.

For humanoid joints, it is better to confirm:

- Backlash requirement
- Joint stiffness requirement
- Encoder type and position feedback method
- Control mode, such as position, velocity, or torque control
- Load condition and expected external force

## Backdrivability and Safety Considerations

Some humanoid robot joints may benefit from backdrivability or lower resistance movement, especially in research robots, exoskeletons, wearable systems, or human-interaction applications.

However, backdrivability must be evaluated together with holding torque, brake requirement, power-off behavior, safety logic, and control strategy.

Questions to confirm:

- Should the joint be manually movable when power is off?
- Is holding position required without power?
- Is a brake required?
- Is low resistance or compliance more important than static holding force?
- What is the expected external load on the joint?

## Mechanical Interface and Load Condition

Humanoid joints often have complex mechanical load conditions. The gearbox or actuator may experience radial load, axial load, moment load, shock load, or off-axis force.

Before prototype design, confirm:

- Output shaft or flange structure
- Mounting hole pattern
- Bearing support method
- Radial load and axial load
- Moment load and impact load
- Cable outlet direction
- Available diameter, thickness, and length

If the output side has high radial load or moment load, external bearing support or a custom output structure may be required.

## Standard Models as Starting Points

The following SigGear models can be used as starting points for humanoid robot joint evaluation.

| Model | Type | Typical Starting Use |
| --- | --- | --- |
| [CPM100-25](../CPM100-25.md) | Compact cycloidal robotic joint module | Higher-load humanoid joints, robot arm joints, compact high-torque actuator evaluation. |
| [CPM80-25](../CPM80-25.md) | Compact cycloidal robotic joint module | Smaller humanoid joints, quadruped joints, exoskeleton joints, compact actuator evaluation. |
| [SG6010C](../SG6010C.md) | Compact planetary robotic joint module | Lightweight humanoid arm, exoskeleton, service robot, research platform. |
| [SG8021](../SG8021.md) | High-performance planetary robotic joint module | Medium-size robotic joint, compact integrated actuator, robot arm or quadruped joint. |
| [6-42mm Planetary Gear Reducer](../Applications/6-42mm-planetary-gear-reducer.md) | Miniature planetary gearbox series | Wrist, gripper, micro actuator, compact servo motor gearbox, medical device drive. |

## When a Custom Gearbox or Actuator Is Needed

A custom solution may be needed when standard products do not meet the exact torque, speed, size, shaft, flange, weight, noise, encoder, brake, or control interface requirements.

Typical custom requirements include:

- Special output torque or peak torque
- Special output speed or gear ratio
- Limited joint space
- Custom output shaft or flange
- Hollow structure or special mounting pattern
- Backdrivable or low-resistance design
- CAN, RS485, EtherCAT, or custom protocol discussion
- Encoder, brake, driver, wiring, or connector integration
- OEM / ODM production planning

See [Custom Robotic Joint Actuator and OEM Gearbox Solutions](../custom-robotic-joint-actuator-oem-gearbox-solutions.md) for project-specific customization support.

## Information to Provide Before Selection

To recommend a suitable humanoid robot joint gearbox or actuator, please provide:

| Information | Example |
| --- | --- |
| Joint position | Hip, knee, ankle, shoulder, elbow, wrist, gripper. |
| Required output torque | Rated torque and peak torque. |
| Required output speed | Target rpm at the joint output. |
| Available space | Diameter, thickness, length, cable outlet limit. |
| Load condition | Radial load, axial load, moment load, impact load, duty cycle. |
| Precision requirement | Backlash, repeatability, stiffness, positioning accuracy. |
| Backdrive requirement | Manual movement, compliance, holding torque, power-off behavior. |
| Motor and control | Motor type, voltage, CAN, RS485, EtherCAT, encoder, brake, driver. |
| Quantity | Prototype quantity, first batch, estimated annual quantity. |
| Project stage | Concept, prototype, testing, small batch, or mass production. |

## Related Pages

- [Cycloidal Reducer for Humanoid Robot Joints](../Applications/humanoid-robot-joint-reducer.md)
- [Robot Joint Gearbox Selection Guide](robot-joint-gearbox-selection-guide.md)
- [Cycloidal Reducer vs Harmonic Drive](../Comparisons/cycloidal-vs-harmonic-drive.md)
- [Planetary vs Cycloidal Gearbox](../Comparisons/planetary-vs-cycloidal-gearbox.md)
- [Custom Robotic Joint Actuator and OEM Gearbox Solutions](../custom-robotic-joint-actuator-oem-gearbox-solutions.md)
- [Factory Capability, Quality Control, and OEM / ODM Support](../factory-capability-quality-oem-odm.md)

## Request Gearbox Recommendation, CAD, Sample, or Quote

For humanoid robot joint gearbox selection, CAD model request, 2D drawing, sample evaluation, quotation, or custom actuator support, send your project requirements to SigGear.

[Request CAD, Datasheet, Sample, or Quote](../request-cad-sample-quote.md)

**Website:** https://www.siggear.com  
**Email:** [wangwanrong984@gmail.com](mailto:wangwanrong984@gmail.com)  
**Products:** Humanoid robot joint gearboxes / compact cycloidal reducers / planetary robotic joint modules / custom robotic actuators
