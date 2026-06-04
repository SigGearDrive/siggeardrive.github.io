# MIT Control Quick Start

## Introduction

MIT Control is one of the most widely used control methods in modern robotics.

It is commonly used in:

- Humanoid Robots
- Quadruped Robots
- Exoskeleton Systems
- Dynamic Motion Platforms

SigGear robotic joint modules support MIT-style control via CAN Bus.

---

## What is MIT Control?

MIT Control combines:

- Position Control
- Velocity Control
- Torque Feedforward

into a single command.

Control Equation:

```text
Torque Output

= Kp × Position Error
+ Kd × Velocity Error
+ Feedforward Torque
```

This provides:

- Smooth Motion
- Fast Response
- High Dynamic Performance

---

## Why Use MIT Control?

Compared with simple position control:

### Better Compliance

The actuator can respond naturally to external forces.

### Better Dynamic Motion

Suitable for:

- Walking
- Running
- Jumping
- Balancing

### Improved Force Control

Widely used in humanoid and quadruped robots.

---

## MIT Command Structure

Typical Parameters:

| Parameter | Description |
|----------|----------|
| Position | Target Position |
| Velocity | Target Velocity |
| Kp | Position Gain |
| Kd | Velocity Gain |
| Torque FF | Feedforward Torque |

---

## CAN Command

MIT Control Command:

```text
CMD ID = 0x008
```

Direction:

```text
Host → Joint Module
```

---

## Recommended Initial Parameters

### Position Gain (Kp)

```text
5 - 20
```

### Velocity Gain (Kd)

```text
0.1 - 1.0
```

### Feedforward Torque

```text
0 Nm
```

Start with conservative values and increase gradually.

---

## Example Usage

### Example 1

Target:

```text
Position = 0°
Velocity = 0
Torque FF = 0
```

Purpose:

```text
Hold Current Position
```

---

### Example 2

Target:

```text
Position = 30°
Velocity = 0
Torque FF = 0
```

Purpose:

```text
Move to Target Position
```

---

### Example 3

Target:

```text
Position = Dynamic
Velocity = Dynamic
Torque FF = Dynamic
```

Purpose:

```text
Walking Control
Running Control
Force Control
```

---

## Recommended Applications

### Humanoid Robots

Recommended Products:

- CPM100-25
- CPM80-25

---

### Quadruped Robots

Recommended Products:

- CPM80-25
- SG8021

---

### Exoskeleton Systems

Recommended Products:

- CPM80-25
- SG6010C

---

## Common Tuning Problems

### Oscillation

Symptoms:

- Vibration
- Instability

Solution:

```text
Reduce Kp
Increase Kd
```

---

### Slow Response

Symptoms:

- Delayed Motion

Solution:

```text
Increase Kp
```

---

### Excessive Current

Symptoms:

- High Motor Temperature
- High Current Draw

Solution:

```text
Reduce Kp
Reduce Feedforward Torque
```

---

## Development Workflow

Recommended Process:

1. Establish CAN Communication
2. Enter Closed Loop Control
3. Verify Position Control
4. Verify Velocity Control
5. Enable MIT Control
6. Tune Kp and Kd
7. Perform Dynamic Testing

---

## Related Documents

- CAN_PROTOCOL.md
- MIT_CONTROL.md
- CAN-Quick-Start.md
- ERROR_CODES.md

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
