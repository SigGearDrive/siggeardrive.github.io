# Humanoid Robot Joint Torque Reference

## Introduction

One of the most common questions in humanoid robot development is:

> How much torque does each joint actually need?

The answer depends on:

- Robot Weight
- Height
- Walking Speed
- Payload
- Motion Requirements

This document provides a practical reference for actuator selection.

---

## Typical Humanoid Robot Categories

| Robot Type | Weight |
|------------|------------|
| Small Humanoid | 10-20 kg |
| Medium Humanoid | 20-50 kg |
| Full-Size Humanoid | 50-90 kg |
| Heavy-Duty Humanoid | 90+ kg |

---

## Neck Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 1-5 Nm |
| Peak Torque | 3-10 Nm |

Recommended Products:

- SG6010C

---

## Wrist Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 2-8 Nm |
| Peak Torque | 5-15 Nm |

Recommended Products:

- SG6010C

---

## Elbow Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 5-20 Nm |
| Peak Torque | 10-40 Nm |

Recommended Products:

- SG8021
- CPM80-25

---

## Shoulder Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 10-40 Nm |
| Peak Torque | 20-80 Nm |

Recommended Products:

- CPM80-25
- CPM100-25

---

## Ankle Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 15-50 Nm |
| Peak Torque | 30-100 Nm |

Recommended Products:

- CPM100-25

---

## Hip Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 20-80 Nm |
| Peak Torque | 50-150 Nm |

Recommended Products:

- CPM100-25

---

## Knee Joint

### Typical Requirements

| Parameter | Value |
|------------|------------|
| Rated Torque | 20-80 Nm |
| Peak Torque | 50-150 Nm |

Recommended Products:

- CPM100-25

---

## Product Mapping

| Robot Joint | Recommended Product |
|------------|------------|
| Neck | SG6010C |
| Wrist | SG6010C |
| Elbow | SG8021 / CPM80-25 |
| Shoulder | CPM80-25 |
| Hip | CPM100-25 |
| Knee | CPM100-25 |
| Ankle | CPM100-25 |

---

## Important Notes

The values above are engineering references only.

Actual torque requirements depend on:

- Robot Mass
- Joint Position
- Walking Dynamics
- Payload Requirements
- Safety Factors

Always perform system-level calculations before final actuator selection.

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
