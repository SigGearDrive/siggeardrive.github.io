# SigGear Product and Engineering FAQ

These answers provide controlled public guidance. Model-specific pages, quotations and technical agreements take priority over general answers.

## What is an integrated robot joint actuator?

An integrated robot joint actuator combines a motor and precision transmission in a compact joint package. Depending on the selected SigGear model and configuration, the assembly may also include an encoder, driver and communication interface. Do not assume that every product includes every component.

## Can SigGear supply a joint actuator without an integrated driver?

Selected models can be supplied with or without an integrated driver. The sensor, cable, connector and control configuration must be confirmed in the quotation.

## Do SigGear joint actuators support CAN, RS485 or EtherCAT?

Communication capability is configuration-specific. Some driver-equipped products support CAN. RS485, EtherCAT and other interfaces may be optional or project-specific and must not be described as standard unless the selected product page, quotation and technical agreement confirm them.

## Can the actuator control position, velocity and torque?

Available control modes depend on the driver, encoder, firmware and product configuration. Confirm the required modes, protocol, command set, feedback signals and controller limits during engineering review.

## How should rated torque and peak torque be interpreted?

Rated torque is associated with sustained operation under defined electrical, thermal and duty-cycle conditions. Peak torque is a short-duration capability. Its permitted duration depends on voltage, current limit, cooling, installation, ambient temperature and motion cycle. Peak torque must not be used as a continuous rating.

## Should a planetary or cycloidal transmission be selected?

There is no universal choice. Compare the complete torque-speed cycle, allowable size and weight, backlash, external loads, efficiency, thermal conditions, shock loads, output speed, control architecture and project cost. Use the published model pages as starting points and confirm the final selection with complete application data.

## Is a gearbox or actuator backdrivable?

Backdrivability depends on the complete motor, transmission ratio, friction, seals, preload, mechanism, controller state and applied load. It must not be assumed from the product family alone. State the required power-off behavior and manual force or torque during selection.

## Are noise and service-life values available?

Noise and service life depend on model, ratio, speed, load, duty cycle, lubrication, mounting and test method. Numeric claims are supplied only when applicable data is available for the selected configuration. A product video is not a substitute for a controlled acoustic test.

## Can SigGear provide CAD models and detailed drawings?

STEP models, 2D drawings and detailed interface documents are provided after application review and inquiry. The supplied file must match the quoted model and configuration.

## What customization can SigGear evaluate?

Depending on engineering feasibility and project scope, SigGear can evaluate motor-and-reducer matching, reduction ratio, output shaft, flange, housing, cable, connector, encoder, driver, communication, branding, labeling and packaging changes. Availability, engineering cost, lead time and minimum quantity are confirmed case by case.

## What information is needed for product selection or quotation?

Provide at least:

- Application and axis position
- Continuous torque
- Peak torque and peak duration
- Rated and maximum output speed
- Operating voltage
- Outer-diameter, thickness, length and weight limits
- Radial, axial and overturning loads
- Duty cycle, ambient temperature and cooling method
- Backlash, positioning and repeatability requirements
- Encoder, driver, communication and brake requirements
- Prototype quantity and estimated annual quantity

For robot arms, humanoids, quadrupeds and exoskeletons, prepare a separate requirement set for every joint axis.

## Does a public product page replace a quotation or technical agreement?

No. Public pages support preliminary selection. The quotation and technical agreement define the ordered model, configuration, included components, interfaces, performance scope and commercial terms.

## Where can certification information be checked?

See [Certifications and Factory Verification](../company/certifications.md). Certification claims must match the actual certificate holder, scope, model and applicable standard.

