---

title: ROS2 Robot Joint Actuator
description: Learn how SigGear robot joint actuators, compact cycloidal joint modules, and custom robotic drive solutions can be integrated into ROS2 robot projects for humanoid robots, quadruped robots, robot arms, and automation systems.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ROS2 Robot Joint Actuator

SigGear provides compact robotic joint modules, cycloidal reducer drive solutions, planetary gear reducers, micro gear motors, and custom actuator solutions for robotics and automation projects.

For robotics engineers building humanoid robots, quadruped robots, robot arms, mobile manipulators, robotic grippers, and custom automation systems, ROS2 integration is often an important part of actuator evaluation. A ROS2-compatible actuator workflow can help engineers control robot joints, test motion commands, collect feedback, and integrate drive modules into larger robot software systems.

This page introduces a typical ROS2 robot joint actuator integration workflow for SigGear robotic drive solutions.

> Note: The examples below are general integration references. Final topic names, message formats, control modes, CAN IDs, parameters, and SDK interfaces should be confirmed according to the actual actuator model, firmware, controller, and project requirements.

## Why ROS2 Matters for Robot Joint Actuators

ROS2 is commonly used in modern robotics projects because it provides a flexible software framework for sensors, controllers, actuators, simulation, robot description, motion planning, and distributed communication.

For robot joint actuators, ROS2 can help engineers:

* Send position, velocity, or torque commands
* Read actuator feedback
* Monitor joint position, speed, current, voltage, temperature, and fault state
* Connect low-level actuator control with high-level robot software
* Integrate robot joints into humanoid robots, quadruped robots, robot arms, and mobile robots
* Test actuator performance during prototype development
* Build repeatable control and diagnostic workflows

## Typical SigGear Actuator Integration Architecture

A typical robot joint actuator integration includes hardware, firmware, communication, SDK, and ROS2 software layers.

| Layer                      | Function                                                                  |
| -------------------------- | ------------------------------------------------------------------------- |
| Robot application          | Humanoid robot, quadruped robot, robot arm, gripper, or automation system |
| ROS2 control layer         | Publishes commands and receives feedback                                  |
| SigGear ROS2 node          | Converts ROS2 messages into actuator commands                             |
| SDK or communication layer | Handles CAN, serial, RS485, or custom protocol communication              |
| Motor controller / driver  | Executes control commands                                                 |
| Actuator hardware          | Motor, reducer, encoder, brake, housing, and output interface             |
| Mechanical system          | Robot joint, arm link, leg joint, gripper, or custom mechanism            |

A simplified architecture is:

```text
ROS2 Application
      ↓
ROS2 Actuator Node
      ↓
SigGear SDK / Communication Layer
      ↓
CAN / RS485 / Serial / Custom Interface
      ↓
Motor Driver
      ↓
Robot Joint Actuator
```

## Typical Applications

SigGear ROS2 robot joint actuator integration can support:

* Humanoid robot joints
* Quadruped robot leg joints
* Robot arm joints
* Collaborative robot joints
* Compact robotic actuators
* Mobile manipulator joints
* Robotic grippers
* Research robot platforms
* Lab automation systems
* Custom automation equipment
* Servo drive modules
* Educational robotics platforms

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

## Typical Control Modes

A robot joint actuator may support different control modes depending on the actuator model, controller, firmware, and communication protocol.

| Control Mode           | Description                           | Typical Use                                        |
| ---------------------- | ------------------------------------- | -------------------------------------------------- |
| Position control       | Command target joint position         | Robot arms, humanoid joints, quadruped joints      |
| Velocity control       | Command target speed                  | Wheels, rotary mechanisms, test systems            |
| Torque control         | Command target torque or current      | Dynamic robots, force control, legged robots       |
| Current control        | Command motor current                 | Low-level motor control and torque-related control |
| Enable / disable       | Enable or disable actuator output     | Safety and initialization                          |
| Zero calibration       | Set or read actuator zero position    | Robot assembly and startup                         |
| Fault reset            | Clear fault state after diagnosis     | Maintenance and testing                            |
| Parameter read / write | Read or configure actuator parameters | Setup and commissioning                            |

Final supported control modes should be confirmed according to the actuator specification.

## Typical ROS2 Topics

The following topic structure is a recommended reference for organizing robot joint actuator communication.

| Topic                    | Direction             | Description                                                              |
| ------------------------ | --------------------- | ------------------------------------------------------------------------ |
| `/siggear/joint_command` | ROS2 to actuator node | Send target position, velocity, torque, or control command               |
| `/siggear/joint_state`   | Actuator node to ROS2 | Publish actuator position, velocity, torque, current, and status         |
| `/siggear/joint_fault`   | Actuator node to ROS2 | Publish fault code and diagnostic information                            |
| `/siggear/enable`        | ROS2 to actuator node | Enable or disable actuator                                               |
| `/siggear/zero`          | ROS2 to actuator node | Set zero position or run calibration                                     |
| `/siggear/diagnostics`   | Actuator node to ROS2 | Publish actuator temperature, voltage, current, and communication status |

For a robot with multiple joints, topic names can include joint names:

```text
/left_knee/joint_command
/left_knee/joint_state
/right_knee/joint_command
/right_knee/joint_state
/left_hip/joint_command
/left_hip/joint_state
```

## Example Joint Command Message

A simple joint command message may include actuator ID, control mode, position, velocity, torque, and enable state.

```yaml
actuator_id: 1
control_mode: "position"
target_position: 1.5708
target_velocity: 0.5
target_torque: 0.0
enable: true
```

For a torque-controlled robot joint, the command may look like:

```yaml
actuator_id: 1
control_mode: "torque"
target_position: 0.0
target_velocity: 0.0
target_torque: 8.5
enable: true
```

## Example Joint Feedback Message

A typical feedback message may include measured position, velocity, torque, current, voltage, temperature, and status.

```yaml
actuator_id: 1
position: 1.568
velocity: 0.48
torque: 8.2
current: 2.4
voltage: 24.0
temperature: 42.5
enabled: true
fault_code: 0
status: "normal"
```

## Example ROS2 Node Structure

A typical SigGear actuator ROS2 package may include:

```text
siggear_robot_joint_ros2/
  package.xml
  CMakeLists.txt
  launch/
    siggear_joint.launch.py
  config/
    actuator_config.yaml
  src/
    siggear_joint_node.cpp
  include/
    siggear_joint_node.hpp
  msg/
    JointCommand.msg
    JointFeedback.msg
  README.md
```

For Python-based development, the structure may look like:

```text
siggear_robot_joint_ros2/
  package.xml
  setup.py
  launch/
    siggear_joint.launch.py
  config/
    actuator_config.yaml
  siggear_robot_joint_ros2/
    siggear_joint_node.py
  msg/
    JointCommand.msg
    JointFeedback.msg
  README.md
```

## Example Configuration File

The actuator configuration file can store communication parameters, joint IDs, joint names, limits, and control settings.

```yaml
siggear_actuators:
  communication:
    interface: "can"
    channel: "can0"
    bitrate: 1000000
    timeout_ms: 10

  joints:
    - name: "left_knee"
      actuator_id: 1
      control_mode: "position"
      reduction_ratio: 25
      position_limit_min: -2.5
      position_limit_max: 2.5
      velocity_limit: 8.0
      torque_limit: 40.0

    - name: "right_knee"
      actuator_id: 2
      control_mode: "position"
      reduction_ratio: 25
      position_limit_min: -2.5
      position_limit_max: 2.5
      velocity_limit: 8.0
      torque_limit: 40.0
```

## Example Launch File

A simple launch file can load actuator configuration and start the ROS2 node.

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='siggear_robot_joint_ros2',
            executable='siggear_joint_node',
            name='siggear_joint_node',
            output='screen',
            parameters=['config/actuator_config.yaml']
        )
    ])
```

## Basic Startup Workflow

A typical ROS2 actuator startup workflow may include:

1. Check power supply and wiring.
2. Confirm CAN, RS485, serial, or communication interface.
3. Confirm actuator ID and communication bitrate.
4. Start ROS2 actuator node.
5. Read actuator status.
6. Check voltage, temperature, current, and fault state.
7. Enable actuator.
8. Run zero calibration if required.
9. Send low-speed test command.
10. Verify position, speed, torque, and feedback.
11. Integrate with robot control software.

## Example Command Test

A simple command-line test may publish a joint command to the actuator node.

```bash
ros2 topic pub /siggear/joint_command siggear_robot_joint_ros2/msg/JointCommand "{
  actuator_id: 1,
  control_mode: 'position',
  target_position: 0.5,
  target_velocity: 0.2,
  target_torque: 0.0,
  enable: true
}"
```

To read actuator feedback:

```bash
ros2 topic echo /siggear/joint_state
```

To check diagnostics:

```bash
ros2 topic echo /siggear/diagnostics
```

## Joint State Integration

For robot systems using standard robot state workflows, actuator feedback can be converted into joint state messages.

Typical joint state data includes:

* Joint name
* Position
* Velocity
* Effort or torque

Example:

```yaml
name:
  - left_knee
  - right_knee
position:
  - 1.25
  - 1.23
velocity:
  - 0.35
  - 0.34
effort:
  - 12.5
  - 12.2
```

This allows higher-level robot software to monitor actuator state and integrate with robot models, controllers, and visualization tools.

## Safety Considerations

Robot joint actuators can generate high torque. Safety logic should be included during development and testing.

Recommended safety checks include:

| Safety Item            | Description                                                      |
| ---------------------- | ---------------------------------------------------------------- |
| Enable control         | Actuator should only output torque after explicit enable command |
| Position limit         | Prevent commands beyond mechanical joint range                   |
| Velocity limit         | Prevent unsafe high-speed movement                               |
| Torque limit           | Prevent excessive torque output                                  |
| Temperature monitoring | Stop or reduce output when temperature is too high               |
| Voltage monitoring     | Detect low voltage or overvoltage                                |
| Current monitoring     | Detect overload or abnormal current                              |
| Communication timeout  | Stop actuator if command communication is lost                   |
| Fault handling         | Read and respond to actuator fault codes                         |
| Emergency stop         | Provide system-level stop logic for testing and operation        |

During early testing, use low speed, low torque, and no-load conditions before connecting the actuator to the full robot mechanism.

## CAN Communication Integration

Many robot actuators use CAN or CAN-based communication because CAN is reliable for distributed actuator systems.

A typical CAN-based actuator network includes:

```text
ROS2 Computer
      ↓
CAN Interface
      ↓
CAN Bus
      ↓
Actuator 1
Actuator 2
Actuator 3
...
```

Important CAN parameters include:

* CAN channel
* Bitrate
* Actuator ID
* Command frame format
* Feedback frame format
* Timeout setting
* Fault code definition
* Communication frequency
* Bus termination
* Cable length
* Electrical noise protection

For more details, see:

* [CAN Protocol Robot Joint Control](can-protocol-robot-joint-control.md)

## ROS2 Integration for Humanoid Robots

Humanoid robots require multiple actuators working together in a coordinated way.

Typical humanoid robot joint requirements include:

* Compact actuator size
* High torque density
* Low backlash
* Stable position feedback
* Smooth motion
* Synchronized multi-joint control
* Shock resistance
* Safety limits
* Temperature monitoring
* Communication reliability

Recommended resources:

* [Cycloidal Reducer for Humanoid Robot Joints](../Applications/humanoid-robot-joint-reducer.md)
* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)
* [Integrated Robot Joint vs Separate Motor Gearbox](../Comparisons/integrated-robot-joint-vs-separate-motor-gearbox.md)

## ROS2 Integration for Quadruped Robots

Quadruped robots require fast joint feedback, reliable torque output, and stable communication under dynamic motion.

Important quadruped joint requirements include:

* High peak torque
* Impact load resistance
* Fast command update
* Joint state feedback
* Temperature and current monitoring
* Compact leg joint layout
* Reliable cable routing
* Safety shutdown logic

Recommended resources:

* [Quadruped Robot Joint Gearbox](../Applications/quadruped-robot-joint-gearbox.md)
* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)
* [Planetary vs Cycloidal Gearbox](../Comparisons/planetary-vs-cycloidal-gearbox.md)

## ROS2 Integration for Robot Arms

Robot arms require stable positioning, repeatability, and coordinated multi-axis control.

Important robot arm actuator requirements include:

* Position accuracy
* Low backlash
* Stable velocity control
* Smooth acceleration and deceleration
* Joint limit protection
* Encoder feedback
* Payload-based torque evaluation
* Multi-axis synchronization

Recommended resources:

* [Robot Arm Joint Gearbox](../Applications/robot-arm-joint-gearbox.md)
* [Cycloidal Reducer vs Harmonic Drive](../Comparisons/cycloidal-vs-harmonic-drive.md)
* [Robot Joint Gearbox Selection Guide](../Selection-Guides/robot-joint-gearbox-selection-guide.md)

## Developer Checklist

Before integrating a SigGear actuator into a ROS2 robot project, confirm:

| Item                    | What to Confirm                                                      |
| ----------------------- | -------------------------------------------------------------------- |
| Actuator model          | CPM100-25, CPM80-25, SG series, custom actuator, or gearbox solution |
| Control mode            | Position, velocity, torque, current, or mixed control                |
| Communication interface | CAN, RS485, serial, or custom interface                              |
| Actuator ID             | Unique ID for each actuator                                          |
| Bitrate                 | Communication speed                                                  |
| Power supply            | Voltage and current capacity                                         |
| Encoder                 | Feedback type and zero position                                      |
| Brake                   | Brake requirement and release logic                                  |
| Joint limits            | Mechanical and software limits                                       |
| Torque limits           | Continuous and peak torque limits                                    |
| Temperature limits      | Warning and shutdown thresholds                                      |
| ROS2 topics             | Command, feedback, diagnostics, fault, enable                        |
| Update frequency        | Command and feedback cycle rate                                      |
| Safety logic            | Timeout, emergency stop, fault handling                              |
| Test method             | No-load test, low-speed test, load test, robot integration test      |

## Common Integration Mistakes

Avoid these common mistakes during actuator integration:

| Mistake                                       | Possible Result                                       |
| --------------------------------------------- | ----------------------------------------------------- |
| Sending high-speed commands during first test | Unexpected movement or mechanical damage              |
| Ignoring joint limits                         | Collision or mechanical overtravel                    |
| Ignoring torque limits                        | Overload or unsafe movement                           |
| No communication timeout                      | Actuator may continue moving after communication loss |
| Incorrect actuator ID                         | Commands may go to the wrong joint                    |
| Wrong bitrate or CAN configuration            | No communication or unstable feedback                 |
| No zero calibration                           | Incorrect joint position reference                    |
| No temperature monitoring                     | Overheating during continuous operation               |
| Skipping no-load testing                      | Problems may only appear after full robot assembly    |
| No emergency stop                             | Unsafe prototype testing environment                  |

## Recommended Testing Process

A safe and practical testing process is:

1. Power-on check without mechanical load.
2. Confirm communication with one actuator.
3. Read actuator status and feedback.
4. Enable actuator at low torque or low speed.
5. Send small position command.
6. Verify feedback direction.
7. Confirm zero position.
8. Add software position limits.
9. Add velocity and torque limits.
10. Test repeated motion.
11. Test under real mechanism load.
12. Integrate multiple actuators.
13. Add safety stop and fault handling.
14. Run long-cycle reliability testing.

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

* [CAN Protocol Robot Joint Control](can-protocol-robot-joint-control.md)
* [SigGear Robot Joint SDK](https://github.com/SigGearDrive/SigGear-robot-joint-sdk)
* [SigGear ROS2 Repository](https://github.com/SigGearDrive/SigGear-ros2)
* [SigGear CAD Models](https://github.com/SigGearDrive/SigGear-cad-models)

Related products:

* [CPM100-25 Compact Cycloidal Robotic Joint Module](../CPM100-25.md)
* [CPM80-25 Compact Cycloidal Robotic Joint Module](../CPM80-25.md)
* [SG6010C Compact Precision Drive Solution](../SG6010C.md)
* [SG8021 Precision Drive Solution](../SG8021.md)

## FAQ

### Can SigGear robot joint actuators be integrated with ROS2?

Yes. SigGear robot joint actuators and custom robotic drive solutions can be evaluated for ROS2-based robot projects through suitable communication interfaces, SDK layers, and ROS2 actuator nodes. Final integration depends on actuator model, controller, firmware, and project requirements.

### What control modes are used for ROS2 robot joint actuators?

Typical control modes may include position control, velocity control, torque control, current control, enable / disable, zero calibration, fault reset, and parameter read / write. Final supported modes depend on the actuator and controller.

### Can ROS2 control multiple robot joint actuators?

Yes. A ROS2 robot system can control multiple actuators by assigning unique actuator IDs, separate joint names, and structured command and feedback topics.

### What communication interface is used for robot joint actuators?

Robot joint actuators may use CAN, RS485, serial, or custom communication interfaces. CAN is commonly used for distributed actuator networks, but the final interface depends on the actuator model and controller design.

### What information is needed for ROS2 actuator integration support?

Please provide actuator model, application, number of joints, communication interface, control mode, power supply, torque requirement, speed requirement, ROS2 environment, and expected command / feedback workflow.

## Request ROS2 Integration Support

If you are developing a humanoid robot, quadruped robot, robot arm, robotic gripper, compact actuator, mobile manipulator, or custom automation system, contact SigGear for actuator selection and ROS2 integration support.

Please include the following information:

* Application
* Robot type
* Number of joints
* Required output torque
* Required output speed
* Control mode
* Communication interface
* Power supply
* Encoder or brake requirement
* ROS2 integration requirement
* SDK requirement
* Mechanical space limit
* Duty cycle
* Estimated annual quantity

**Email:** [wangwanrong984@gmail.com](mailto:wangwanrong984@gmail.com)
**Application:** Humanoid robot / quadruped robot / robot arm / robotic gripper / robotic actuator / ROS2 robot project
**Response:** SigGear can help evaluate a suitable robot joint actuator, gearbox, reducer, or custom drive solution for your ROS2 robot project.
