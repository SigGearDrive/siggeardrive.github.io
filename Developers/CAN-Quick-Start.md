# CAN Quick Start

## Introduction

This guide helps developers quickly establish CAN communication with SigGear robotic joint modules.

Supported products:

- SG6010C
- SG8021
- CPM80-25
- CPM100-25

---

## Hardware Requirements

Prepare the following:

- SigGear Joint Module
- 24V-48V Power Supply
- USB-CAN Adapter
- CAN Cable
- PC or Embedded Controller

---

## CAN Communication Parameters

### Default Baud Rate

```text
500 kbps
```

### Optional Baud Rate

```text
1 Mbps
```

### CAN Frame Type

```text
Standard 11-bit CAN Frame
```

---

## CAN ID Structure

```text
CAN_ID = (Node_ID << 5) + CMD_ID
```

Example:

```text
Node ID = 5
CMD ID  = 12

CAN ID = (5 << 5) + 12
```

---

## Recommended Node IDs

| Device | Node ID |
|----------|----------|
| Joint 1 | 1 |
| Joint 2 | 2 |
| Joint 3 | 3 |
| Joint 4 | 4 |
| Joint 5 | 5 |
| Joint 6 | 6 |

---

## Step 1: Power On

Connect:

- Power Supply
- CAN Bus

Verify:

- Correct Voltage
- Correct Wiring
- CAN Termination

---

## Step 2: Enter Closed Loop Control

Command:

```text
CMD ID = 0x007
State = 8
```

Meaning:

```text
Closed Loop Control
```

---

## Step 3: Position Control

Command:

```text
CMD ID = 0x00C
```

Typical Use:

- Joint Position Testing
- Robot Arm Control
- Motion Verification

---

## Step 4: Velocity Control

Command:

```text
CMD ID = 0x00D
```

Typical Use:

- Speed Regulation
- Motion Experiments

---

## Step 5: Torque Control

Command:

```text
CMD ID = 0x00E
```

Typical Use:

- Force Control
- Robot Joint Development
- Exoskeleton Research

---

## Step 6: MIT Motion Control

Command:

```text
CMD ID = 0x008
```

MIT Control combines:

- Position
- Velocity
- Torque Feedforward

into a single command.

Recommended for:

- Humanoid Robots
- Quadruped Robots
- Dynamic Motion Systems

---

## Read Feedback

Available feedback:

- Position
- Velocity
- Bus Voltage
- Error Status

---

## Common Issues

### No Response

Check:

- Power Supply
- CAN Wiring
- Node ID
- Baud Rate

---

### Communication Error

Check:

- CAN Termination Resistors
- CANH/CANL Connections
- Baud Rate Configuration

---

### Motor Does Not Move

Check:

- Axis State
- Error Codes
- Control Mode

---

## Related Documents

See also:

- CAN_PROTOCOL.md
- MIT_CONTROL.md
- ERROR_CODES.md

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
