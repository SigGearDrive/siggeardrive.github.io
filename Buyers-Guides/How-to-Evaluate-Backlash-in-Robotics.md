# How to Evaluate Backlash in Robotics

## Introduction

Backlash is one of the most important performance indicators in robotic transmission systems.

For applications such as humanoid robots, robot arms and exoskeletons, excessive backlash can significantly reduce motion quality and positioning accuracy.

This guide explains what backlash is, how to evaluate it and how to select the right transmission solution.

---

## What Is Backlash?

Backlash is the angular movement that occurs when the input direction changes but the output shaft has not yet responded.

It is commonly caused by:

- Gear Tooth Clearance
- Manufacturing Tolerances
- Bearing Clearance
- Mechanical Wear

Backlash is usually measured in:

- Degrees (°)
- Arc Minutes (arcmin)

---

## Why Backlash Matters

Backlash directly affects:

### Position Accuracy

Higher backlash reduces positioning precision.

### Motion Smoothness

Backlash can create noticeable vibration and motion discontinuities.

### Force Control

Force and torque control become less accurate when backlash is excessive.

### Walking Stability

For humanoid robots, backlash can negatively impact:

- Balance
- Walking
- Running
- Dynamic Motion

---

## Typical Backlash Requirements

| Application | Recommended Backlash |
|------------|------------|
| Educational Robots | <1° |
| Service Robots | <0.5° |
| Industrial Robots | <0.2° |
| Humanoid Robots | <0.1° |
| Surgical Robots | Near Zero |

---

## How to Measure Backlash

### Method 1: Mechanical Measurement

1. Fix the actuator housing.
2. Lock the input shaft.
3. Apply a small force to the output shaft.
4. Measure angular movement.

The measured angle is the mechanical backlash.

---

### Method 2: Encoder-Based Measurement

Using high-resolution encoders:

1. Command a small position change.
2. Measure actual output movement.
3. Calculate deadband before motion occurs.

This method is commonly used in robotics testing.

---

## Comparison of Transmission Technologies

| Technology | Typical Backlash |
|------------|------------|
| Standard Spur Gear | 1°-3° |
| Planetary Gearbox | 0.2°-1° |
| Cycloidal Reducer | 0.05°-0.2° |
| Harmonic Drive | Near Zero |

---

## Backlash vs Robot Type

### Service Robots

Recommended:

- Planetary Gearboxes
- Moderate Backlash Acceptable

Products:

- SG6010C
- SG8021

---

### Exoskeleton Systems

Recommended:

- Cycloidal Reducers

Products:

- CPM80-25

---

### Humanoid Robots

Recommended:

- Low Backlash Solutions

Products:

- CPM100-25
- CPM80-25

Target Backlash:

```text
<0.1°
```

---

### Industrial Robot Arms

Recommended:

- Cycloidal Reducers
- Harmonic Drives

Target Backlash:

```text
<0.2°
```

---

## Common Mistakes

### Focusing Only on Torque

High torque does not guarantee good motion performance.

Backlash is equally important.

---

### Ignoring Long-Term Wear

Backlash may increase over time.

Always evaluate:

- Service Life
- Durability
- Load Cycles

---

### Comparing Different Measurement Methods

Always verify:

- Test Conditions
- Measurement Method
- Load State

when comparing suppliers.

---

## SigGear Recommendations

### Planetary Solutions

Products:

- SG6010C
- SG8021

Best For:

- Service Robots
- Educational Robots
- AGV & AMR

---

### Cycloidal Solutions

Products:

- CPM80-25
- CPM100-25

Best For:

- Humanoid Robots
- Exoskeletons
- Industrial Robots

---

## Quick Selection Guide

| Application | Recommended Product |
|------------|------------|
| Service Robot | SG6010C |
| Robot Arm | SG8021 |
| Exoskeleton | CPM80-25 |
| Humanoid Knee | CPM100-25 |
| Humanoid Hip | CPM100-25 |

---

## Conclusion

Backlash is one of the most critical specifications in robotic transmission systems.

For advanced robotic applications, low backlash often contributes more to system performance than simply increasing torque.

Selecting the correct transmission technology can significantly improve:

- Stability
- Accuracy
- Reliability
- Robot Performance

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
