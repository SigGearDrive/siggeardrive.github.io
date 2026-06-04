# How to Choose a Gearbox for Robotics

## Introduction

Selecting the right gearbox is one of the most important decisions in robotic system design.

A gearbox directly influences:

- Torque Output
- Motion Accuracy
- System Efficiency
- Reliability
- Robot Performance

This guide explains how to evaluate gearbox technologies for robotics applications.

---

## Why Gearboxes Matter

Electric motors typically operate at:

- High Speed
- Low Torque

Robotic joints require:

- Low Speed
- High Torque

A gearbox converts motor output into usable robotic motion.

---

## Step 1: Determine Required Torque

Before selecting a gearbox, calculate:

### Rated Torque

The continuous torque required during normal operation.

### Peak Torque

The maximum torque required during:

- Acceleration
- Impact Loads
- Sudden Direction Changes

---

## Step 2: Evaluate Backlash Requirements

Backlash is the amount of lost motion between input and output.

Lower backlash improves:

- Position Accuracy
- Motion Smoothness
- Force Control

### Typical Requirements

| Application | Recommended Backlash |
|------------|------------|
| Educational Robots | <1° |
| Service Robots | <0.5° |
| Industrial Robots | <0.2° |
| Humanoid Robots | <0.1° |

---

## Step 3: Compare Gearbox Technologies

### Planetary Gearboxes

Advantages:

- High Efficiency
- Compact Design
- Lower Cost
- High Speed Capability

Best For:

- Service Robots
- AGV & AMR
- Educational Robots

Recommended SigGear Products:

- SG6010C
- SG8021

---

### Cycloidal Reducers

Advantages:

- Low Backlash
- High Torque Density
- Excellent Shock Resistance
- Long Service Life

Best For:

- Humanoid Robots
- Quadruped Robots
- Exoskeletons

Recommended SigGear Products:

- CPM80-25
- CPM100-25

---

### Harmonic Drives

Advantages:

- Near-Zero Backlash
- High Position Accuracy

Best For:

- Precision Robot Arms
- Surgical Robots
- Aerospace Systems

Limitations:

- Higher Cost
- Lower Shock Resistance

---

## Step 4: Evaluate Available Installation Space

Consider:

- Diameter
- Length
- Weight

Compact robots benefit from high torque density solutions.

---

## Step 5: Consider Communication and Integration

Modern robotic systems often require:

- CAN Bus
- EtherCAT
- UART
- RS485

Integrated joint modules can significantly reduce integration effort.

---

## Gearbox Selection by Robot Type

### Humanoid Robots

Recommended:

- CPM100-25
- CPM80-25

---

### Quadruped Robots

Recommended:

- CPM80-25
- SG8021

---

### Service Robots

Recommended:

- SG6010C
- SG8021

---

### Exoskeleton Systems

Recommended:

- CPM80-25
- SG6010C

---

## Quick Product Comparison

| Product | Technology | Rated Torque |
|----------|----------|----------|
| SG6010C | Planetary | 6 Nm |
| SG8021 | Planetary | 10 Nm |
| CPM80-25 | Cycloidal | 10 Nm |
| CPM100-25 | Cycloidal | 25 Nm |

---

## Common Mistakes

### Selecting by Torque Only

Always consider:

- Weight
- Backlash
- Integration Complexity
- Reliability

---

### Ignoring Peak Loads

Peak torque often determines gearbox lifespan.

---

### Overlooking Communication Requirements

Communication interfaces can significantly affect development time.

---

## Need Help Selecting a Gearbox?

SigGear engineers can assist with:

- Gearbox Selection
- Joint Design
- Robot Architecture
- Custom Development

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
