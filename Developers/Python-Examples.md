# Python Examples

## Introduction

This document provides simple Python examples for evaluating and testing SigGear robotic joint modules.

SigGear products are compatible with ODrive-based workflows and can be quickly evaluated using Python.

Supported products:

- SG6010C
- SG8021
- CPM80-25
- CPM100-25

---

## Install Python Package

Install ODrive tools:

```bash
pip install --upgrade odrive
```

Verify installation:

```bash
odrivetool
```

---

## Connect to Device

```python
import odrive

odrv0 = odrive.find_any()

print("Connected")
```

Expected Output:

```text
Connected
```

---

## Read Bus Voltage

```python
print(odrv0.vbus_voltage)
```

Example Output:

```text
48.2
```

---

## Enter Closed Loop Control

```python
odrv0.axis0.requested_state = 8
```

State:

```text
Closed Loop Control
```

---

## Enter Idle Mode

```python
odrv0.axis0.requested_state = 1
```

State:

```text
Idle
```

---

## Position Control Example

Move to position:

```python
odrv0.axis0.controller.input_pos = 1.0
```

Move back:

```python
odrv0.axis0.controller.input_pos = 0.0
```

Applications:

- Joint Testing
- Position Verification
- Motion Development

---

## Velocity Control Example

Set speed:

```python
odrv0.axis0.controller.input_vel = 2.0
```

Stop:

```python
odrv0.axis0.controller.input_vel = 0
```

Applications:

- Speed Testing
- Motion Experiments

---

## Torque Control Example

Apply torque:

```python
odrv0.axis0.controller.input_torque = 1.0
```

Remove torque:

```python
odrv0.axis0.controller.input_torque = 0
```

Applications:

- Force Control
- Exoskeleton Development
- Humanoid Robot Research

---

## Read Position Feedback

```python
print(
    odrv0.axis0.pos_vel_mapper.pos_rel
)
```

---

## Read Velocity Feedback

```python
print(
    odrv0.axis0.pos_vel_mapper.vel
)
```

---

## Read Errors

```python
from odrive.utils import dump_errors

dump_errors(odrv0)
```

---

## Clear Errors

```python
odrv0.clear_errors()
```

---

## Save Configuration

```python
odrv0.save_configuration()
```

---

## Reboot Device

```python
odrv0.reboot()
```

---

## Example Test Sequence

```python
import odrive
import time

odrv0 = odrive.find_any()

odrv0.axis0.requested_state = 8

time.sleep(1)

odrv0.axis0.controller.input_pos = 1.0

time.sleep(3)

odrv0.axis0.controller.input_pos = 0.0

time.sleep(3)

odrv0.axis0.requested_state = 1
```

Purpose:

- Verify Communication
- Verify Position Control
- Verify Basic Functionality

---

## Recommended Development Process

1. Connect Device
2. Verify Bus Voltage
3. Enter Closed Loop Control
4. Test Position Control
5. Test Velocity Control
6. Test Torque Control
7. Verify Feedback Signals
8. Integrate CAN Communication

---

## Notes

ODrive is a trademark of ODrive Robotics.

Examples shown here are provided for compatibility and evaluation purposes.

---

## Related Documents

- Getting-Started.md
- CAN-Quick-Start.md
- MIT-Control-Quick-Start.md
- ODRIVE_COMPATIBILITY.md

---

## Contact

Website:

https://www.siggear.com

Email:

wwang109@163.com
