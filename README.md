# OpenMI

View Schematics and PCB Layout on [![kicanvas.org](https://img.shields.io/badge/kicanvas.org-8864CB)](https://kicanvas.org/?github=https://github.com/OpenCleanEnergy/OpenMI/tree/main/hardware/KiCad/OpenMI)

## What is our goal?

We want to build an open source micro-inverter.

## Why making this open source?

1. **Transparency and Trust:** Open sourcing fosters transparency, providing users and developers with complete visibility into how the microinverter works. This builds trust within the community and ensures that the technology operates as advertised.

2. **Collaborative Development:** The open-source model encourages collaboration from a diverse group of developers, engineers, and enthusiasts. This collective effort often leads to innovative solutions, enhanced functionality, and improved performance.

3. **Rapid Iteration and Improvement:** With a broader community involved, improvements and bug fixes can happen at a faster pace. Developers can quickly identify and rectify issues, leading to a more robust and reliable microinverter.

4. **Customization and Adaptability:** Open sourcing allows users to modify the microinverter to suit their specific needs. Whether it's adapting the hardware for different solar panel configurations or modifying the software for specific energy management, users have the freedom to customize.

5. **Cost-Effectiveness and Affordability:** By making the designs and software open source, the overall cost of development can be reduced. Individuals and organizations can access the project without expensive licensing fees, making renewable energy solutions more accessible to a wider audience.

6. **Knowledge Sharing and Learning Opportunities:** Open-source projects serve as valuable learning resources for students, researchers, and professionals looking to understand the technology, its design principles, and best practices in renewable energy.

7. **Global Impact and Adoption:** Open sourcing allows for widespread adoption and deployment, especially in regions where cost and accessibility are significant factors. It facilitates the dissemination of renewable energy technology to areas that need it most.

8. **Alignment with Ethical and Environmental Values:** Open-source projects align with values of openness, collaboration, and sustainability. By promoting transparency and knowledge sharing, it contributes to a sustainable and ethical approach to technology development and use.

9. **Long-Term Sustainability and Maintenance:** With a diverse community contributing to the project, the microinverter is likely to remain relevant and actively maintained over the long term, ensuring its sustainability and continued development.

## What specifications should the micro-inverter have?

Comparison of micro-inverters with rated output power between 350VA and 400VA:

| Model                                  | HM-350[^HM] | HM-400[^HM] | IQ7A[^IQ7A] |EVT300[^EVT300]|TSOL-M800[^TSOL] |
|:---------------------------------------|:-----------:|:-----------:|:-----------:|:-------------:|:---------------:|
| Manufacturer                           | Hoymiles    | Hoymiles    | Enphase     | Envertech     |    TSUN         |
| Number of solar panels                 | 1           | 1           | 1           | 1             | 2               |
| Recommended input power (W)            | 280-470+    | 320-540+    | 295-460     | 180-420+      |2 $\cdot$ 280-440|
| $V_{MPPT,min}$ (V)                     | 33          | 34          | 38 (18)     | 24            | 33              |
| $V_{MPPT,max}$ (V)                     | 48          | 48          | 43 (58)     | 45            | 48              |
| Start-up voltage (V)                   | 22          | 22          | 22          | -             | -               |
| Operating volage range (V)             | 16-60       | 16-60       | 16-58       | 18-54         | 16-60           |
| Maximum input current (A)              | 11.5        | 12          | 12          | 12            | 11.5            |
| Maximum input short circuit current (A)| 15          | 15          | 20          | 15            | 15              |
| Rated output power (VA)                | 350         | 400         | 349         | 300           | 600             |
| Peak efficiency (%)                    | 96.7        | 96.7        | 97.7        | 95.4          | 96.7            |
| CEC weighted efficiency (%)            | 96.5        | 96.5        | 97.0        | 95.0          | 96.5            |

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

During basic research, we came across the application note [^AN4070]. The application note describes the implementation of a 250W grid-connected micro-inverter. The design is based on 2 power stages, namely an interleaved isolated DC-DC boost converter and a DC-AC converter.

![Block Scheme](docs/block-scheme.drawio.svg)  

The application note provides a detailed description of the operation and component selection.  
The system presented is relatively simple and requires relatively few components. It has an efficiency $ > 90 \% $ and avoids flux-walk problems due to the DC-DC boost converter being current-fed [^MAGNA]. The capacitors required are of such low capacitance that they can be implemented as film capacitors, which avoids the eventual lifetime issues with electrolytic capacitors.
For these reasons, we decided to adopt and extend the design.

#### PV panel specifications

The following table shows a comparison of different solar modules and their technical data, which were adopted as a guide for designing the microinverter.

| Model                        | WS350M[^WS350M]| Meyer Burger White[^MB]| JAM72S-30-550-MR[^JA] |
|:-----------------------------|:--------------:|:----------------------:|:---------------------:|
| Manufacturer                 | Wattstunde     | Meyer Burger White     | JA Solar              |
| Power (Wp)                   | 350            | 400                    | 550                   |
| Short Circuit Current (A)    | 9.68           | 10.9                   | 14.00                 |
| Open Circuit Voltage (V)     | 46.7           | 44.6                   | 49.9                  |
| $V_{MPPT}$ (V)               | 38.1           | 38.6                   | 41.96                 |
| $I_{MPPT}$ (A)               | 9.19           | 10.4                   | 13.11                 |

## How can the micro inverter be simulated?

The circuit design of the micro inverter was simulated in [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html). All LTspice simulations are stored in the [simulation](simulation) folder.
Since the entire circuit design is quickly complex and time-consuming to simulate, the individual building blocks of the circuit were first built and simulated individually.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md).

## Footnotes

[^HM]: [HM Microinverter Datasheet](https://www.hoymiles.com/wp-content/uploads/downloadupload/Datasheet_HM-300-350-400_AP_EN_V202206.pdf)

[^IQ7A]: [IQ7A Microinverter Datasheet](https://enphase.com/download/iq7a-microinverter-data-sheet)

[^EVT300]: [EVT300 Microinverter Datasheet](https://envertec.com/wp-content/uploads/2022/11/EVT300_Datasheet.pdf)

[^TSOL]: [TSOL-M800 Microinverter Datasheet](https://www.ecoheroes.shop/media/pdf/c9/f6/5b/Datenblatt_Mikrowechselrichter_TSUN_M800_EN.pdf)

[^AN4070]: [AN4070 250 W grid connected microinverter](https://www.st.com/resource/en/application_note/dm00050692-250-w-grid-connected-microinverter-stmicroelectronics.pdf)

[^WS350M]: [Wattstunde solar panel 350Wp](https://solarkontor.de/mediafiles/PDF/Solarmodule/Wattstunde/M-Reihe/Datenblatt%20M%20%20v0123.pdf)

[^MB]: [Meyer Burger White solar panel 400Wp](https://www.meyerburger.com/fileadmin/user_upload/PDFs/Produktdatenblaetter/DE/DS_Meyer_Burger_White_de.pdf)

[^JA]: [JA Solar solar panel 550Wp](https://www.jasolar.com/uploadfile/2022/1122/20221122050252648.pdf)

[^MAGNA]: [An Overview of Current-Fed Power Processing](https://magna-power.com/learn/white-paper/current-fed-power-processing)
