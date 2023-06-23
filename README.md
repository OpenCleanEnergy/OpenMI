# openMI
[![lang-en](https://img.shields.io/badge/lang-en-informational?style=for-the-badge)](README.md)
[![lang-de](https://img.shields.io/badge/lang-de-inactive?style=for-the-badge)](README.de.md)

## What is our goal?

We want to build an open source micro-inverter.

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
| Operating volage range (V)             | 16-60       | 16-60       | 16-58       | 18-54         | 16 -60          |
| Maximum input current (A)              | 11.5        | 12          | 12          | 12            | 11.5            |
| Maximum input short circuit current (A)| 15          | 15          | 20          | 15            | 15              |
| Rated output power (VA)                | 350         | 400         | 349         | 300           | 600             |

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
The system presented is relatively simple and requires relatively few components. It has an efficiency $ > 90 \% $ and avoids flux-walk problems due to the DC-DC boost converter being current-fed [^2]. The capacitors required are of such low capacitance that they can be implemented as film capacitors, which avoids the eventual lifetime issues with electrolytic capacitors.
For these reasons, we decided to adopt and extend the design.

#### DC bus power decoupling

The required capacitance of the capacitor $C$ can be calculated with the following formula [^3]:

$$ C = \frac{P_0}{2 \cdot \pi \cdot f \cdot V_{DC} \cdot \Delta V } $$

Where 
- $P_0$ is the output power, 
- $f$ the line frequency, 
- $V_{DC}$ the voltage of the DC bus and 
- $\Delta V$ is the allowed peak-to-peak voltage variation.

This gives the required capacitance of the capacitor $C$:

- $P_0 = 400W$
- $f = 50Hz$
- $V_{DC} = 380V$
- $\Delta V = 40V \Rightarrow V_{DC_{min}} = 360V; V_{DC_{max}} = 400V$

$$ C = \frac{400W}{2 \cdot \pi \cdot 50Hz \cdot 380V \cdot 40V} = 83.77\mu F $$

The calculation was verified with simulation [dc-bus-power-decoupling](simulation/dc-bus-power-decoupling).

### Microcontroller

ESP32

## How can the micro inverter be simulated?

The circuit design of the micro inverter was simulated in [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html). All LTspice simulations are stored in the [simulation](simulation) folder.
Since the entire circuit design is quickly complex and time-consuming to simulate, the individual building blocks of the circuit were first built and simulated individually.


## Footnotes

[^HM]: [HM Microinverter Datasheet](https://www.hoymiles.com/wp-content/uploads/downloadupload/Datasheet_HM-300-350-400_AP_EN_V202206.pdf)

[^IQ7A]: [IQ7A Microinverter Datasheet](https://enphase.com/download/iq7a-microinverter-data-sheet)

[^EVT300]: [EVT300 Microinverter Datasheet](https://envertec.com/wp-content/uploads/2022/11/EVT300_Datasheet.pdf)

[^TSOL]: [TSOL-M800 Microinverter Datasheet](https://www.ecoheroes.shop/media/pdf/c9/f6/5b/Datenblatt_Mikrowechselrichter_TSUN_M800_EN.pdf)

[^AN4070]: [AN4070 250 W grid connected microinverter](https://www.st.com/resource/en/application_note/dm00050692-250-w-grid-connected-microinverter-stmicroelectronics.pdf)

[^2]: [An Overview of Current-Fed Power Processing](https://magna-power.com/learn/white-paper/current-fed-power-processing)

[^3]: [DC-Bus Design with Hybrid Capacitor Bank in Single-Phase PV Inverters](https://intelligentpower.engr.uga.edu/wp-content/uploads/2019/10/deqiang2017Dc-bus.pdf) | https://doi.org/10.1109/IECON.2017.8216408

[^4]: [Evaluation of Electrolytic Capacitor Application in Enphase Microinverters](https://www4.enphase.com/sites/default/files/Electrolytic_Capacitor_Expert_Report.pdf)

[^5]: [Reliability Study of Electrolytic Capacitors in a Microinverter](https://www4.enphase.com/sites/default/files/EnphaseElectrolyticCapacitorLife.pdf)