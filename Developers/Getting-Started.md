# Getting Started with SigGear Robotic Joint Modules

## Introduction

Welcome to SigGear Robotics.

This guide helps developers quickly evaluate and integrate SigGear robotic joint modules into robotic systems.

Supported products include:

- SG6010C
- SG8021
- CPM80-25
- CPM100-25

---

## Step 1: Select a Product

Choose the actuator according to your application.

| Application | Recommended Product |
|------------|------------|
| Robot Wrist | SG6010C |
| Robot Elbow | SG8021 |
| Exoskeleton Joint | CPM80-25 |
| Humanoid Hip | CPM100-25 |
| Humanoid Knee | CPM100-25 |

---

## Step 2: Review Product Documentation

Visit:

- Product Documentation
- CAD Models
- SDK Documentation

Recommended repositories:

- SigGear-product-docs
- SigGear-cad-models
- SigGear-robot-joint-sdk

---

## Step 3: Prepare Communication Interface

Supported communication methods:

- CAN Bus
- USB Type-C
- MIT Motion Control
- ODrive-Compatible Communication

---

## Step 4: Connect Power

Typical operating voltage:

```text
24V - 48V DC
```

Always verify:

- Power Supply Voltage
- Current Capacity
- Wiring Polarity

before powering the actuator.

---

## Step 5: Connect Communication Interface

Recommended for evaluation:

```text
CAN Bus
```

Benefits:

- Reliable
- Easy Integration
- Fast Development

---

## Step 6: Enter Closed Loop Control

Example:

```python
odrv0.axis0.requested_state = 8
```

---

## Step 7: Start Motion Testing

Recommended sequence:

1. Position Control
2. Velocity Control
3. Torque Control
4. MIT Control

---

## Available Resources

### Documentation

- CAN Protocol
- MIT Control Guide
- Error Codes

### Engineering Resources

- CAD Drawings
- Product Specifications

### Future Resources

- URDF Models
- Gazebo Simulation
- ROS2 Integration

---

## Need Help?

SigGear engineers can assist with:

- Product Selection
- System Integration
- CAN Communication
- Custom Development

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
