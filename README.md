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

### Microcontroller

ESP32

## How can the micro inverter be simulated?

The circuit design of the micro inverter was simulated in [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html). All LTspice simulations are stored in the [simulation](simulation) folder.
Since the entire circuit design is quickly complex and time-consuming to simulate, the individual building blocks of the circuit were first built and simulated individually.

### Solar module and input capacitance design
A [solar module in LTspice](simulation/pv-panel-input) was modeled following the instructions from [FesZ Electronics](https://www.youtube.com/watch?v=ox0UtYe4owI).

The power output from the solar panel is calculated as $P_{PV} = U_{PV} \cdot I_{PV}$.

First, the point at which the power $P_{PV}$ is maximum can be found for the simulated solar module. This point is also called Maximum Power Point (MPP) and can be found graphically in LTSpice by plotting the power $P_{PV}$ (in the graph V(pv1) $\cdot$ I(I1)) versus the current $I_{PV}$ (in the graph I(I1)) of the solar module.

<p align="center">
  <img src="simulation/pv-panel-input/pv-panel-mpp.svg" title="Graphic for determining the MPP">
</p>

For example, for the 300-320 watt [solar panel from sunceco](http://sunceco.com/wp-content/uploads/2017/01/SEP300-320.pdf) used in the simulation, there is a graphically determined Maximum Power Point $P_{MPP} = 312.55$ W for $I_{MPP} = 8.31$ A and $U_{MPP} = 37.61$ V.

Since the inverter is to inject the current from the solar module sinusoidally according to the grid frequency, a rectified sinusoidal current source can be connected to the output of the solar module to design the input capacitance. In order for the rms value of the current source to equal $I_{MPP}$, the amplitude of the sine wave must be multiplied by $\sqrt{2}$. Furthermore, in order for the current source to actually cause the solar module to output the maximum possible power in the simulation, the empirically determined factor $1.1$ had to be multiplied onto the amplitude. The exact value should be secondary here, since the Maximum Power Point Tracking (MPPT) will later ensure that the maximum possible power can be extracted from the solar module at any time. In this step of the simulation, the focus is only on determining the input capacity.

<p align="center">
  <img src="simulation/pv-panel-input/pv-panel-grid-current-source-schematic.png" width="70%" title="Solar module with sinusoidal power source">
</p>

Subsequently, the values of the input capacitance Cp can be varied for this setup and the average output power $P_{out}$ of the solar module can be measured. If the measured output power $P_{out}$ is normalized to the maximum possible output power $P_{MPP}$ in each case and plotted over different values of Cp, the following curves are obtained using a 300 watt and a 550 watt solar module as examples:

<p align="center">
  <img src="simulation/pv-panel-input/pv-panel-pout-over-cp.svg" alt="/pv-panel-pout-over-cp" title="Normalized output power of solar module plotted over different values of input capacitance">.
</p>

Looking at the curves shown, a selection of four 2200 µF electrolytic capacitors is found to be suitable for the choice of input capacitance. This is consistent with reports for input capacitance selection in Enphase microinverters [^4].

In terms of the expected life of the electrolytic capacitors, if the circuit is designed correctly and high quality components are selected, there should be no concerns as Enphase Energy was able to show in a reliability study of electrolytic capacitors in a microinverter [^5].


### Push-pull inverter 
The [simulation of push-pull inverter](simulation/push-pull-inverter) ... TODO

#### transformer design

TODO:

## Footnotes

[^AN4070]: [AN4070 250 W grid connected microinverter](https://www.st.com/resource/en/application_note/dm00050692-250-w-grid-connected-microinverter-stmicroelectronics.pdf)

[^2]: [An Overview of Current-Fed Power Processing](https://magna-power.com/learn/white-paper/current-fed-power-processing)

[^3]: [DC-Bus Design with Hybrid Capacitor Bank in Single-Phase PV Inverters](https://intelligentpower.engr.uga.edu/wp-content/uploads/2019/10/deqiang2017Dc-bus.pdf) | https://doi.org/10.1109/IECON.2017.8216408

[^4]: [Evaluation of Electrolytic Capacitor Application in Enphase Microinverters](https://www4.enphase.com/sites/default/files/Electrolytic_Capacitor_Expert_Report.pdf)

[^5]: [Reliability Study of Electrolytic Capacitors in a Microinverter](https://www4.enphase.com/sites/default/files/EnphaseElectrolyticCapacitorLife.pdf)