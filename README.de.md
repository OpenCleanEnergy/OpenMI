# OpenCE

[![lang-en](https://img.shields.io/badge/lang-en-inactive?style=for-the-badge)](README.md)
[![lang-de](https://img.shields.io/badge/lang-de-informational?style=for-the-badge)](README.de.md)

## Was ist unser Ziel?

Wir wollen einen Open Source Mikro-Wechselrichter bauen.

## Welche Spezifikationen soll der Mikro-Wechselrichter haben?

Vorbehaltlich weiterer Änderungen soll der Mikro-Wechselrichter folgende technischen Daten haben:
- Wirkungsgrad > 90%
- Betriebsbereich: 16V - 58V
- Eingangsleistung vom Solarmodul: 350W - 550W
- Leistung: 400VA mit Möglichkeit zur softwareseitigen Begrenzung
- Power Faktor ≈ 1
- Total Harmonic Distortion (THD) < 5%
- Elektrische Isolation zwischen Solarmodul und Netzspannung
- Temperaturbereich: -40 °C bis 60 °C
- Schnittstellen:
  - WIFI mit [SunSpec Modbus](https://sunspec.org/sunspec-modbus-specifications/)
  - Powerline Communication (PLC)

Optionale Features:
- Einstellbarer Power Faktor

## Wie soll der Mikro-Wechselrichter technisch umgesetzt werden?

Die technische Umsetzung des Mikro-Wechselrichters wird im Projektverlauf stetig überarbeitet und iterativ verbessert. Anmerkungen und Verbesserungsvorschläge sind hier gerne gesehen!


### Regelungssystem

Bei der Grundlagenrecherche sind wir auf das Paper [^1] gestoßen. Das Paper schlägt ein relativ einfaches und kostengünstiges Regelungssystem vor, das vielversprechende Ergebnisse liefert. An diesem Regelungssystem haben wir uns orientiert und es für unsere Zwecke angepasst.

![Control Scheme](docs/control-scheme.drawio.svg)  

Der Duty Cycle $D$ wird durch den MPPT-Algorithmus und die Netzspannung bestimmt. Bei einem gegebenen maximalem Duty Cycle $D_{max}$ und Steuerungswert aus dem MPPT-Algorithmus $k$ wird der Duty Cycle wie folgt berechnet: 

$$ D(t) = D_{max} \cdot k \cdot | sin(2 \pi f t) | $$

$$ D\left(\frac{n}{2f}\right) = 0 ~~|~~ n\in \mathbb{N_0} $$

$$ D\left(\frac{2n+1}{4f}\right) = D_{max} \cdot k ~~|~~ n \in \mathbb{N_0} $$

Im Nulldurchgang der Netzspannung beträgt der Duty Cycle $D = 0$. Erreicht die Netzspannung ihren Höchstwert, so beträgt der Duty Cycle $D = D_{max} \cdot k$.

### Topologie

#### DC-Bus Kondensator

Die benötigte Kapazität des Kondensators $C$ kann mit der folgenden Formel [^4] berechnet werden:

$$ C = \frac{P_0}{2 \cdot \pi \cdot f \cdot V_{DC} \cdot \Delta V } $$

Dabei ist 
- $P_0$ die Ausgangsleistung, 
- $f$ die Netzfrequenz, 
- $V_{DC}$ die Spannung des DC Busses und 
- $\Delta V$ die zulässige peak-to-peak Spannungsschwankung.

Damit ergibt sich für die benötigte Kapazität des Kondensators $C$:

- $P_0 = 400W$
- $f = 50Hz$
- $V_{DC} = 380V$
- $\Delta V = 40V$ ($V_{DC_{min}} = 360V$ und $V_{DC_{max}} = 400V$)

$$ C = \frac{400W}{2 \cdot \pi \cdot 50Hz \cdot 380V \cdot 40V} = 83.77\mu F $$

### Mikrocontroller

ESP32

## Wie kann der Mikro-Wechselrichter simuliert werden?

Das Schaltungsdesign des Mikro-Wechselrichters wurde in [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html) simuliert. Alle LTspice Simulationen sind im Ordner [simulation](simulation) abgelegt.
Da das gesamte Schaltungsdesign schnell komplex und aufwändig zu simulieren ist, wurden die einzelnen Bausteine der Schaltung zunächst einzeln aufgebaut und simuliert.

### Solarmodul und Auslegung der Eingangskapazität
Ein [Solarmodul in LTspice](simulation/pv-panel-input) wurde nach der Anleitung von [FesZ Electronics](https://www.youtube.com/watch?v=ox0UtYe4owI) modelliert.

Die vom Solarmodul abgegebene Leistung berechnet sich nach $P_{PV} = U_{PV} \cdot I_{PV}$.

Zunächst kann für das simulierte Solarmodul der Punkt gefunden werden, an dem die Leistung $P_{PV}$ maximal ist. Dieser Punkt wird auch Maximum Power Point (MPP) und kann in LTSpice grafisch ermittelt werden, indem die Leistung $P_{PV}$ (in der Grafik V(pv1) $\cdot$ I(I1)) über der Stromstärke $I_{PV}$ (in der Grafik I(I1)) des Solarmoduls dargestellt wird.

<p align="center">
  <img src="simulation/pv-panel-input/pv-panel-mpp.svg" title="Grafik zur Ermittlung des MPP">
</p>

Für das beispielsweise in der Simulation verwendete 300-320 Watt [Solarmodul von sunceco](http://sunceco.com/wp-content/uploads/2017/01/SEP300-320.pdf) ergibt sich ein grafisch ermittelter Maximum Power Point $P_{MPP} = 312,55$ W für $I_{MPP} = 8,31$ A und $U_{MPP} = 37,61$ V.

Da der Wechselrichter den Strom aus dem Solarmodul entsprechend der Netzfrequenz sinusförmig einspeisen soll, kann zur Auslegung der Eingangskapazität eine gleichgerichtete sinusförmige Stromquelle an den Ausgang des Solarmoduls angeschlossen werden. Damit der Effektivwert der Stromquelle $I_{MPP}$ entspricht, muss die Amplitude des Sinus mit $\sqrt{2}$ multipliziert werden. Damit die Stromquelle das Solarmodul in der Simulation tatsächlich dazu bringen kann, die maximal mögliche Leistung abzugeben, musste darüber hinaus der empirisch ermittelte Faktor $1,1$ auf die Amplitude multipliziert werden. Der genaue Wert soll hier zweitrangig sein, da das Maximum Power Point Tracking (MPPT) später dafür sorgen wird, dass dem Solarmodul zu jedem Zeitpunkt die maximal mögliche Leistung entnommen werden kann. In diesem Schritt der Simulation liegt der Fokus lediglich auf der Ermittlung der Eingangskapazität.

<p align="center">
  <img src="simulation/pv-panel-input/pv-panel-grid-current-source-schematic.png" width="70%"  title="Solarmodul mit sinusförmiger Stromquelle">
</p>

Anschließend können für diesen Aufbau die Werte der Eingangskapazität Cp variiert und dabei die durchschnittliche Ausgangsleistung $P_{out}$ des Solarmoduls gemessen werden. Wird die gemessene Ausgangsleistung $P_{out}$ auf die jeweils maximal mögliche Ausgangsleistung $P_{MPP}$ normiert und über verschiedenen Werten von Cp dargestellt, ergeben sich am Beispiel eines 300 Watt und eines 550 Watt Solarmoduls folgende Kurven:

<p align="center">
  <img src="simulation/pv-panel-input/pv-panel-pout-over-cp.svg" alt="/pv-panel-pout-over-cp" title="Normierte Ausgangsleistung des Solarmodules dargestellt über verschiedenen Werten der Eingangskapazität">
</p>

Bei Betrachtung der dargestellten Kurven wird für die Wahl der Eingangskapazität eine Auswahl von vier 2200 µF Elektrolytkondensatoren als geeignet empfunden. Dies deckt sich mit Berichten für die Wahl der Eingangskapazität in Enphase Mikro-Wechselrichtern [^2].

Hinsichtlich der erwartbaren Lebensdauer der Elektrolytkondensatoren sollte es bei korrekter Auslegung der Schaltung und der Auswahl hochwertiger Bauteile keine Bedenken geben wie Enphase Energy in einer Zuverlässigkeitsstudie von Elektrolytkondensatoren in einem Mikrowechselrichter zeigen konnte [^3].


### Push-Pull Wechselrichter 
Die [Simulation des Push-Pull Wechselrichters](simulation/push-pull-inverter) ... TODO

#### Auslegung des Transformators

TODO:

## Fußnoten

[^1]: [Flyback Photovoltaic Micro-Inverter with a Low Cost and Simple Digital-Analog Control Scheme](https://www.researchgate.net/publication/353247133_Flyback_Photovoltaic_Micro-Inverter_with_a_Low_Cost_and_Simple_Digital-Analog_Control_Scheme) | http://dx.doi.org/10.3390/en14144239

[^2]: [Evaluation of Electrolytic Capacitor Application in Enphase Microinverters](https://www4.enphase.com/sites/default/files/Electrolytic_Capacitor_Expert_Report.pdf)

[^3]: [Reliability Study of Electrolytic Capacitors in a Microinverter](https://www4.enphase.com/sites/default/files/EnphaseElectrolyticCapacitorLife.pdf)

[^4]: [DC-Bus Design with Hybrid Capacitor Bank in Single-Phase PV Inverters](https://intelligentpower.engr.uga.edu/wp-content/uploads/2019/10/deqiang2017Dc-bus.pdf) | https://doi.org/10.1109/IECON.2017.8216408
