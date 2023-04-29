# openMI
[![lang-en](https://img.shields.io/badge/lang-en-informational?style=for-the-badge)](README.md)
[![lang-de](https://img.shields.io/badge/lang-de-inactive?style=for-the-badge)](README.de.md)

## What is our goal?

We want to build an open source micro-inverter.

## What specifications should the micro-inverter have?

Subject to further modifications, the micro-inverter should have the following specifications:
- Efficiency > 90%
- Operating range: 16V - 58V
- Input power from solar panel: 350W - 550W
- Power: 400VA with possibility of software limitation.
- Power factor ≈ 1
- Total Harmonic Distortion (THD) < 5%.
- Electrical isolation between solar module and grid voltage
- Temperature range: -40 °C to 60 °C
- Interfaces:
  - WIFI with [SunSpec Modbus](https://sunspec.org/sunspec-modbus-specifications/)
  - Powerline Communication (PLC)

Optional features:
- Adjustable Power Factor

## How will the micro-inverter be technically implemented?

The technical implementation of the micro-inverter will be continuously revised and iteratively improved during the course of the project. Comments and suggestions for improvement are welcome here!

### Topology

TODO: Push-pull with gain etc.

### Transformer

TODO:

### Microcontroller

ESP32
