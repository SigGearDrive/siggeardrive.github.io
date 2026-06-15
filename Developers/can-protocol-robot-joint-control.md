---

title: CAN Protocol Robot Joint Control
description: Learn how CAN communication can be used for robot joint actuator control, including actuator IDs, command frames, feedback frames, position control, velocity control, torque control, diagnostics, and safety logic.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CAN Protocol Robot Joint Control

CAN communication is widely used in robotics because it provides a reliable bus structure for controlling multiple actuators, motors, sensors, and embedded devices in one robot system.

For humanoid robots, quadruped robots, robot arms, robotic grippers, compact actuators, and automation systems, CAN bus can be used to send joint commands, read actuator feedback, monitor fault states, and coordinate multiple robot joints.

SigGear provides compact robotic joint modules, cycloidal reducer drive solutions, planetary gear reducers, micro gear motors, and customized robotic drive solutions for robotics and automation applications.

> Note: This page provides a general CAN protocol reference for robot joint actuator integration. Final CAN ID format, frame structure, byte order, command definitions, control modes, scaling factors, and safety settings should be confirmed according to the actual actuator model, firmware, controller, and project requirements.

## Why Use CAN for Robot Joint Actuators?

Robot systems often need to control many actuators at the same time. CAN communication is useful because it supports multi-node communication on a shared bus and can work reliably in embedded control systems.

CAN can help engineers:

* Control multiple robot joint actuators
* Assign unique actuator IDs
* Send position, velocity, torque, or current commands
* Read joint position, speed, current, voltage, temperature, and fault state
* Build distributed actuator networks
* Reduce wiring complexity
* Integrate actuators with embedded controllers
* Connect low-level actuator control with ROS2 or custom robot software
* Improve diagnostic and maintenance workflows

## Typical CAN-Based Robot Actuator Architecture

A typical CAN actuator system includes a main controller, CAN interface, CAN bus, and multiple actuators.

```text
Robot Controller / ROS2 Computer / Embedded Controller
        ↓
CAN Interface
        ↓
CAN Bus
        ↓
Robot Joint Actuator 1
Robot Joint Actuator 2
Robot Joint Actuator 3
...
```

A complete software and hardware stack may look like:

```text
Robot Application
        ↓
ROS2 / SDK / Control Software
        ↓
CAN Communication Layer
        ↓
CAN Adapter / MCU / Controller
        ↓
CAN Bus
        ↓
Motor Driver
        ↓
Robot Joint Actuator
```

## Typical Applications

CAN protocol robot joint control can be used in:

* Humanoid robot joints
* Quadruped robot leg joints
* Robot arm joints
* Collaborative robot joints
* Robotic grippers
* Compact robotic actuators
* Servo drive modules
* Mobile manipulators
* Research robot platforms
* AGV / AMR mechanisms
* Laboratory automation systems
* Custom automation equipment

## Recommended SigGear Hardware

Different robot applications may require different actuator or gearbox solutions.

| Application                         | Recommended SigGear Solution                                                            |
| ----------------------------------- | --------------------------------------------------------------------------------------- |
| Humanoid robot joint                | [CPM100-25 Compact Cycloidal Robotic Joint Module](../CPM100-25.md)                     |
| Compact humanoid or quadruped joint | [CPM80-25 Compact Cycloidal Robotic Joint Module](../CPM80-25.md)                       |
| Robot arm joint                     | [Robot Arm Joint Gearbox](../Applications/robot-arm-joint-gearbox.md)                   |
| Quadruped robot joint               | [Quadruped Robot Joint Gearbox](../Applications/quadruped-robot-joint-gearbox.md)       |
| Servo motor gearbox                 | [Servo Motor Planetary Gearbox](../Applications/servo-motor-planetary-gearbox.md)       |
| Compact motor gearbox               | [6-42mm Planetary Gear Reducer](../Applications/6-42mm-planetary-gear-reducer.md)       |
| Micro robotics                      | [6mm Micro Gear Motor for Micro Robotics](../Applications/micro-robotics-gear-motor.md) |
| Robotic gripper                     | [Robot Gripper Gear Motor](../Applications/robot-gripper-gear-motor.md)                 |

## Key CAN Communication Parameters

Before integrating a robot joint actuator through CAN, engineers should confirm the following parameters.

| Parameter            | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| CAN version          | Standard frame or extended frame                                             |
| CAN ID               | Unique identifier for command and feedback frames                            |
| Bitrate              | Common values include 500 kbps or 1 Mbps, depending on system design         |
| Actuator ID          | Unique ID assigned to each actuator                                          |
| Frame length         | Usually up to 8 bytes for classic CAN                                        |
| Byte order           | Little-endian or big-endian data layout                                      |
| Command type         | Position, velocity, torque, current, enable, disable, zero, reset, parameter |
| Feedback type        | Position, velocity, torque, current, voltage, temperature, status, fault     |
| Update rate          | Command and feedback frequency                                               |
| Timeout              | Safety timeout when communication is lost                                    |
| Termination resistor | CAN bus termination at both ends of the bus                                  |
| Ground reference     | Proper grounding and wiring design for stable communication                  |

## Typical CAN Network Layout

A multi-joint robot may connect several actuators on one CAN bus.

```text
CAN_H ─────────────────────────────────────
CAN_L ─────────────────────────────────────
          │        │        │        │
       Joint 1  Joint 2  Joint 3  Joint 4
```

Recommended wiring checks:

* Use twisted pair cable for CAN_H and CAN_L.
* Use proper termination resistors at both ends of the CAN bus.
* Keep wiring clean and avoid unnecessary long stubs.
* Confirm common ground where required.
* Avoid routing CAN wires close to high-power noise sources.
* Check connector quality and cable strain relief.
* Confirm power supply capacity before enabling actuators.

## Typical Control Modes

Robot joint actuators may support different control modes depending on actuator model, controller, firmware, and project requirements.

| Control Mode           | Description                           | Typical Use                                        |
| ---------------------- | ------------------------------------- | -------------------------------------------------- |
| Position control       | Command target joint position         | Robot arms, humanoid joints, quadruped joints      |
| Velocity control       | Command target speed                  | Wheels, rotary mechanisms, test benches            |
| Torque control         | Command target torque                 | Legged robots, force control, dynamic joints       |
| Current control        | Command motor current                 | Low-level motor control and torque-related control |
| Enable / disable       | Enable or disable actuator output     | Startup, safety, maintenance                       |
| Zero calibration       | Set or read zero position             | Assembly and commissioning                         |
| Fault reset            | Clear actuator fault state            | Diagnostics and recovery                           |
| Parameter read / write | Read or configure actuator parameters | Setup and tuning                                   |

## Example CAN ID Design

A simple CAN ID design can separate command and feedback frames.

| Frame Type               | Example CAN ID | Direction                   | Description               |
| ------------------------ | -------------: | --------------------------- | ------------------------- |
| Command to actuator 1    |          0x101 | Controller to actuator      | Send control command      |
| Feedback from actuator 1 |          0x181 | Actuator to controller      | Return actuator state     |
| Command to actuator 2    |          0x102 | Controller to actuator      | Send control command      |
| Feedback from actuator 2 |          0x182 | Actuator to controller      | Return actuator state     |
| Broadcast enable         |          0x100 | Controller to all actuators | Enable multiple actuators |
| Emergency stop           |          0x080 | Controller to all actuators | Stop actuator output      |

This is only an example. Final CAN ID mapping should be confirmed according to the actual actuator firmware and communication protocol.

## Example Command Frame Structure

A simple 8-byte command frame can include control mode, enable flag, target position, target velocity, or target torque.

Example position command frame:

| Byte | Data                | Description             |
| ---: | ------------------- | ----------------------- |
|    0 | Control mode        | 0x01 = position control |
|    1 | Enable flag         | 0x01 = enable           |
|  2-3 | Target position     | Scaled integer          |
|  4-5 | Target velocity     | Scaled integer          |
|  6-7 | Target torque limit | Scaled integer          |

Example interpretation:

```text
CAN ID: 0x101
Data:   01 01 D0 07 F4 01 10 27

Byte 0: 0x01      position control
Byte 1: 0x01      enable actuator
Byte 2-3: 0x07D0  target position value
Byte 4-5: 0x01F4  target velocity value
Byte 6-7: 0x2710  torque limit value
```

The actual scaling factor must be defined by the actuator protocol.

## Example Feedback Frame Structure

A typical feedback frame may return position, velocity, current, temperature, and fault status.

| Byte | Data                       | Description           |
| ---: | -------------------------- | --------------------- |
|  0-1 | Position feedback          | Scaled integer        |
|  2-3 | Velocity feedback          | Scaled integer        |
|  4-5 | Current or torque feedback | Scaled integer        |
|    6 | Temperature                | Temperature value     |
|    7 | Fault code                 | Actuator fault status |

Example interpretation:

```text
CAN ID: 0x181
Data:   C8 03 64 00 20 03 2A 00

Byte 0-1: 0x03C8  position feedback
Byte 2-3: 0x0064  velocity feedback
Byte 4-5: 0x0320  current or torque feedback
Byte 6:   0x2A    temperature
Byte 7:   0x00    no fault
```

## Example Scaling Factors

Many actuator protocols use scaled integers instead of floating-point numbers.

Example scaling table:

| Value       | Example Unit  | Example Scaling  |
| ----------- | ------------- | ---------------- |
| Position    | rad or degree | raw value / 1000 |
| Velocity    | rad/s or rpm  | raw value / 100  |
| Torque      | Nm            | raw value / 100  |
| Current     | A             | raw value / 100  |
| Voltage     | V             | raw value / 10   |
| Temperature | °C            | raw value        |

Example:

```text
Raw position value: 1570
Scaling: raw / 1000
Actual position: 1.570 rad
```

Final scaling factors must match the actual actuator firmware.

## Example Control Commands

### Enable Actuator

```text
CAN ID: 0x101
Data:   00 01 00 00 00 00 00 00
```

### Disable Actuator

```text
CAN ID: 0x101
Data:   00 00 00 00 00 00 00 00
```

### Position Command

```text
CAN ID: 0x101
Data:   01 01 D0 07 F4 01 10 27
```

### Velocity Command

```text
CAN ID: 0x101
Data:   02 01 00 00 F4 01 10 27
```

### Torque Command

```text
CAN ID: 0x101
Data:   03 01 00 00 00 00 20 03
```

### Fault Reset

```text
CAN ID: 0x101
Data:   0F 01 00 00 00 00 00 00
```

These command frames are general examples only. Final command values should be confirmed according to the actual actuator protocol.

## Basic Startup Workflow

A typical CAN robot joint actuator startup workflow includes:

1. Check power supply voltage and current capacity.
2. Confirm actuator wiring.
3. Confirm CAN_H and CAN_L connection.
4. Confirm CAN bus termination.
5. Confirm actuator ID.
6. Confirm CAN bitrate.
7. Power on the actuator.
8. Read feedback frame.
9. Check voltage, temperature, and fault code.
10. Send enable command.
11. Run zero calibration if required.
12. Send low-speed or small-angle test command.
13. Confirm position feedback direction.
14. Add software limits.
15. Test under low load.
16. Test under actual mechanism load.
17. Integrate with robot control software.

## Safety Requirements

Robot joint actuators can generate high torque. CAN communication should include safety logic.

| Safety Function       | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| Enable command        | Prevent actuator output before the system is ready     |
| Disable command       | Stop actuator output during maintenance or fault state |
| Emergency stop        | Immediately stop actuator output when required         |
| Position limit        | Prevent mechanical overtravel                          |
| Velocity limit        | Prevent unsafe high-speed movement                     |
| Torque limit          | Prevent excessive output torque                        |
| Current limit         | Protect motor and driver                               |
| Temperature limit     | Prevent overheating                                    |
| Voltage monitoring    | Detect undervoltage or overvoltage                     |
| Communication timeout | Stop actuator when commands are lost                   |
| Fault code monitoring | Detect and respond to actuator errors                  |
| Startup check         | Prevent unexpected motion after power-on               |

During early testing, always use low speed, low torque, and no-load conditions before connecting the actuator to the full robot mechanism.

## Communication Timeout

A communication timeout is important for robot safety. If the actuator does not receive a valid command within a defined time, it should stop output or enter a safe state.

Example timeout logic:

```text
If no valid command is received within 100 ms:
    reduce torque output
    stop motion
    report timeout fault
    wait for new enable command
```

Timeout behavior should be confirmed according to the actual controller and actuator firmware.

## Fault Code Design

A fault code helps the controller understand actuator status.

Example fault code table:

| Fault Code | Description             |
| ---------: | ----------------------- |
|       0x00 | Normal                  |
|       0x01 | Overcurrent             |
|       0x02 | Overvoltage             |
|       0x03 | Undervoltage            |
|       0x04 | Overtemperature         |
|       0x05 | Encoder error           |
|       0x06 | Communication timeout   |
|       0x07 | Position limit exceeded |
|       0x08 | Driver fault            |
|       0x09 | Motor stall             |
|       0x0A | Calibration error       |

Final fault codes should match the actual actuator firmware.

## Example Python CAN Test

A simple Python-based test can send and receive CAN frames through a compatible CAN interface.

```python
import can
import time


def main():
    bus = can.interface.Bus(channel="can0", bustype="socketcan", bitrate=1000000)

    enable_msg = can.Message(
        arbitration_id=0x101,
        data=[0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        is_extended_id=False
    )

    bus.send(enable_msg)
    print("Enable command sent")

    time.sleep(0.1)

    position_msg = can.Message(
        arbitration_id=0x101,
        data=[0x01, 0x01, 0xD0, 0x07, 0xF4, 0x01, 0x10, 0x27],
        is_extended_id=False
    )

    bus.send(position_msg)
    print("Position command sent")

    while True:
        msg = bus.recv(timeout=1.0)
        if msg is not None:
            print(f"RX ID: {hex(msg.arbitration_id)} Data: {msg.data.hex(' ')}")


if __name__ == "__main__":
    main()
```

This is a general communication example only. Actual CAN ID, data format, byte order, and scaling factors must match the actuator protocol.

## Example ROS2 Integration

CAN communication can be connected to ROS2 through a robot actuator node.

```text
ROS2 Topic
    ↓
ROS2 Actuator Node
    ↓
CAN Communication Layer
    ↓
Robot Joint Actuator
```

Example ROS2 topics:

| Topic                    | Direction             | Description                                               |
| ------------------------ | --------------------- | --------------------------------------------------------- |
| `/siggear/joint_command` | ROS2 to actuator node | Send position, velocity, torque, enable, or reset command |
| `/siggear/joint_state`   | Actuator node to ROS2 | Publish position, velocity, torque, current, and status   |
| `/siggear/joint_fault`   | Actuator node to ROS2 | Publish fault code and diagnostic state                   |
| `/siggear/diagnostics`   | Actuator node to ROS2 | Publish voltage, temperature, communication status        |

For more details, see:

* [ROS2 Robot Joint Actuator](ros2-robot-joint-actuator.md)

## CAN Integration for Humanoid Robots

Humanoid robots may include many actuators across legs, arms, waist, neck, and hands. CAN communication can help connect multiple joint actuators to the robot controller.

Important requirements include:

* Unique actuator ID for each joint
* Stable communication frequency
* Joint position feedback
* Torque or current monitoring
* Temperature monitoring
* Fault reporting
* Software joint limits
* Emergency stop logic
* Cable routing and connector reliability
* Multi-joint synchronization

Recommended resources:

* [Cycloidal Reducer for Humanoid Robot Joints](../Applications/humanoid-robot-joint-reducer.md)
* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)
* [Integrated Robot Joint vs Separate Motor Gearbox](../Comparisons/integrated-robot-joint-vs-separate-motor-gearbox.md)

## CAN Integration for Quadruped Robots

Quadruped robots require reliable actuator communication during walking, running, turning, and landing.

Important requirements include:

* Fast feedback update
* High peak torque monitoring
* Current and temperature monitoring
* Communication timeout protection
* Robust connector design
* Cable protection against repeated leg motion
* Fault handling during dynamic movement
* Safe disable behavior

Recommended resources:

* [Quadruped Robot Joint Gearbox](../Applications/quadruped-robot-joint-gearbox.md)
* [Planetary vs Cycloidal Gearbox](../Comparisons/planetary-vs-cycloidal-gearbox.md)
* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)

## CAN Integration for Robot Arms

Robot arms require stable multi-axis communication and accurate joint feedback.

Important requirements include:

* Position feedback
* Velocity feedback
* Low backlash gearbox selection
* Joint limit protection
* Smooth acceleration and deceleration
* Multi-axis synchronization
* Fault detection
* Repeatable startup calibration

Recommended resources:

* [Robot Arm Joint Gearbox](../Applications/robot-arm-joint-gearbox.md)
* [Cycloidal Reducer vs Harmonic Drive](../Comparisons/cycloidal-vs-harmonic-drive.md)
* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)

## Developer Checklist

Before testing CAN robot joint control, confirm:

| Item            | What to Confirm                                                      |
| --------------- | -------------------------------------------------------------------- |
| Actuator model  | CPM100-25, CPM80-25, SG series, custom actuator, or gearbox solution |
| CAN frame type  | Standard ID or extended ID                                           |
| CAN bitrate     | 500 kbps, 1 Mbps, or project-specific value                          |
| Actuator ID     | Unique ID for each actuator                                          |
| Command ID      | CAN ID for sending actuator commands                                 |
| Feedback ID     | CAN ID for reading actuator feedback                                 |
| Byte order      | Little-endian or big-endian                                          |
| Scaling factors | Position, velocity, torque, current, voltage, temperature            |
| Control mode    | Position, velocity, torque, current, or custom                       |
| Power supply    | Voltage and current capacity                                         |
| Wiring          | CAN_H, CAN_L, ground, power, connector                               |
| Termination     | Proper termination at both ends of CAN bus                           |
| Safety limits   | Position, velocity, torque, current, temperature                     |
| Timeout         | Safe behavior after communication loss                               |
| Fault handling  | Fault read, fault reset, safe shutdown                               |
| Test process    | No-load test, low-speed test, load test, robot integration test      |

## Common CAN Integration Mistakes

Avoid these common mistakes:

| Mistake                         | Possible Result                             |
| ------------------------------- | ------------------------------------------- |
| Wrong CAN bitrate               | No communication                            |
| Wrong actuator ID               | Commands sent to wrong joint or no response |
| Reversed CAN_H and CAN_L        | No communication                            |
| Missing termination resistor    | Unstable communication                      |
| No common ground where required | Communication errors                        |
| Incorrect byte order            | Wrong position, speed, or torque command    |
| Incorrect scaling factor        | Unsafe or incorrect actuator movement       |
| No communication timeout        | Actuator may keep moving after signal loss  |
| No torque limit                 | Unsafe output force                         |
| No position limit               | Mechanical overtravel                       |
| Testing at high speed first     | Unexpected motion or mechanical damage      |
| Ignoring fault codes            | Difficult debugging and unsafe testing      |

## Recommended Testing Process

A safe testing process is:

1. Test one actuator first.
2. Confirm CAN bitrate and actuator ID.
3. Read feedback without enabling torque.
4. Check voltage, temperature, and fault code.
5. Send enable command.
6. Send a very small movement command.
7. Confirm motion direction.
8. Confirm feedback direction.
9. Add position, velocity, and torque limits.
10. Test repeated low-speed motion.
11. Test communication timeout.
12. Test fault reset.
13. Add mechanical load.
14. Test multi-actuator communication.
15. Integrate with ROS2 or robot controller.
16. Run long-cycle reliability testing.

## Recommended SigGear Resources

Application pages:

* [Cycloidal Reducer for Humanoid Robot Joints](../Applications/humanoid-robot-joint-reducer.md)
* [Quadruped Robot Joint Gearbox](../Applications/quadruped-robot-joint-gearbox.md)
* [Robot Arm Joint Gearbox](../Applications/robot-arm-joint-gearbox.md)
* [Robot Gripper Gear Motor](../Applications/robot-gripper-gear-motor.md)
* [Servo Motor Planetary Gearbox](../Applications/servo-motor-planetary-gearbox.md)
* [6-42mm Planetary Gear Reducer](../Applications/6-42mm-planetary-gear-reducer.md)

Selection guides:

* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)
* [Planetary Gearbox Selection Guide](../Selection-Guides/planetary-gearbox-selection-guide.md)
* [Micro Gear Motor Selection Guide](../Selection-Guides/micro-gear-motor-selection-guide.md)

Comparison pages:

* [Cycloidal Reducer vs Harmonic Drive](../Comparisons/cycloidal-vs-harmonic-drive.md)
* [Planetary vs Cycloidal Gearbox](../Comparisons/planetary-vs-cycloidal-gearbox.md)
* [Integrated Robot Joint vs Separate Motor Gearbox](../Comparisons/integrated-robot-joint-vs-separate-motor-gearbox.md)

Developer resources:

* [ROS2 Robot Joint Actuator](ros2-robot-joint-actuator.md)
* [SigGear Robot Joint SDK](https://github.com/SigGearDrive/SigGear-robot-joint-sdk)
* [SigGear ROS2 Repository](https://github.com/SigGearDrive/SigGear-ros2)
* [SigGear CAD Models](https://github.com/SigGearDrive/SigGear-cad-models)

Related products:

* [CPM100-25 Compact Cycloidal Robotic Joint Module](../CPM100-25.md)
* [CPM80-25 Compact Cycloidal Robotic Joint Module](../CPM80-25.md)
* [SG6010C Compact Precision Drive Solution](../SG6010C.md)
* [SG8021 Precision Drive Solution](../SG8021.md)

## FAQ

### What is CAN protocol in robot joint control?

CAN protocol is a communication method that allows a robot controller to send commands and receive feedback from multiple robot joint actuators over a shared bus.

### Why is CAN used for robot actuators?

CAN is commonly used because it supports multi-node communication, reliable embedded control, actuator ID management, feedback monitoring, and distributed robot actuator networks.

### What data can be sent through CAN to a robot joint actuator?

Typical command data may include enable, disable, position command, velocity command, torque command, current command, zero calibration, parameter setting, and fault reset.

### What feedback can a robot joint actuator send through CAN?

Typical feedback data may include position, velocity, torque, current, voltage, temperature, enable state, fault code, and communication status.

### Can CAN be used with ROS2?

Yes. A ROS2 actuator node can convert ROS2 topic commands into CAN frames and convert CAN feedback frames into ROS2 joint state, diagnostics, and fault messages.

### What should I check if CAN communication does not work?

Check CAN bitrate, actuator ID, CAN_H and CAN_L wiring, termination resistor, power supply, frame type, CAN adapter, driver setup, byte order, and whether the actuator is powered correctly.

### Can SigGear help with CAN actuator integration?

Yes. SigGear can help evaluate robot joint actuators, compact drive solutions, CAN communication requirements, and integration workflows based on your robot application.

## Request CAN Integration Support

If you are developing humanoid robots, quadruped robots, robot arms, robotic grippers, compact actuators, servo drive modules, or custom automation systems, contact SigGear for actuator selection and CAN integration support.

Please include the following information:

* Application
* Robot type
* Number of joints
* Required output torque
* Required output speed
* Control mode
* CAN bitrate requirement
* Actuator ID plan
* Power supply
* Encoder or brake requirement
* ROS2 or SDK requirement
* Mechanical space limit
* Duty cycle
* Estimated annual quantity

**Email:** [wangwanrong984@gmail.com](mailto:wangwanrong984@gmail.com)
**Application:** Humanoid robot / quadruped robot / robot arm / robotic gripper / robotic actuator / CAN robot project
**Response:** SigGear can help evaluate a suitable robot joint actuator, gearbox, reducer, or custom drive solution for your CAN-based robot control system.
