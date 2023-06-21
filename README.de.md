# OpenCE

[![lang-en](https://img.shields.io/badge/lang-en-inactive?style=for-the-badge)](README.md)
[![lang-de](https://img.shields.io/badge/lang-de-informational?style=for-the-badge)](README.de.md)

## Was ist unser Ziel?

Wir wollen einen Open Source Mikro-Wechselrichter bauen.

## Welche Spezifikationen soll der Mikro-Wechselrichter haben?

Vergleich von Mikro-Wechselrichtern mit einer Nennausgangsleistung zwischen 350VA und 400VA:

| Modell                       | HM-350[^HM] | HM-400[^HM] | IQ7A[^IQ7A] |
|:-----------------------------|:-----------:|:-----------:|:-----------:|
| Hersteller                   | Hoymiles    | Hoymiles    | Enphase     |
| $V_{MPPT,min}$ (V)           | 33          | 34          | 38 (18)     |
| $V_{MPPT,max}$ (V)           | 48          | 48          | 43 (58)     |
| Anlaufspannung (V)           | 22          | 22          | 22          |
| Betriebsspannungsbereich (V) | 16-60       | 16-60       | 16-58       |
| Maximum input current (A)    | 11.5        | 12          | 12          |
| Maximaler Eingangsstrom (A)  | 15          | 15          | 20          |
| Nennausgangsleistung (VA)    | 350         | 400         | 349         |

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


### Topologie

Bei der Grundlagenrecherche sind wir auf die Application Note [^AN4070] gestoßen. Die Application Note beschreibt die Implementierung eines 250W netzgekoppleten Mikro-Wechselrichters. Das Design basiert auf 2 Leistungsstufen, nämlich einem überlappenden isolierten DC-DC-Aufwärtswandler und einem DC-AC-Wandler.

![Block Scheme](docs/block-scheme.drawio.svg)  

Die Application Note liefert eine detaillierte Beschreibung der Funktionsweise und Bauteileauswahl.  
Das vorgestellte System ist relativ einfach, benötigt relativ wenig Komponenten. Es hat einen Wirkungsgrad $ > 90 \% $ und vermeidet Probleme mit Flux-Walk, weil der DC-DC-Aufwärtswandler stromgespeist ist[^2]. Die benötigten Kondensatoren haben eine so geringe Kapazität, dass sie als Folienkondensatoren realisiert werden können, was die etwaigen Probleme mit der Lebensdauer von Elektrolytkondensatoren vermeidet.
Aus diesen Gründen haben wir uns entschieden, das Design zu übernehmen und zu erweitern.

#### DC-Bus Leistungsentkopplung

Die benötigte Kapazität des Kondensators $C$ kann mit der folgenden Formel [^3] berechnet werden:

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
- $\Delta V = 40V \Rightarrow V_{DC_{min}} = 360V; V_{DC_{max}} = 400V$

$$ C = \frac{400W}{2 \cdot \pi \cdot 50Hz \cdot 380V \cdot 40V} = 83.77\mu F $$

Die Berechnung wurde mit der Simulation [dc-bus-power-decoupling](simulation/dc-bus-power-decoupling) verifiziert.

### Mikrocontroller

ESP32

## Wie kann der Mikro-Wechselrichter simuliert werden?

Das Schaltungsdesign des Mikro-Wechselrichters wurde in [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html) simuliert. Alle LTspice Simulationen sind im Ordner [simulation](simulation) abgelegt.
Da das gesamte Schaltungsdesign schnell komplex und aufwändig zu simulieren ist, wurden die einzelnen Bausteine der Schaltung zunächst einzeln aufgebaut und simuliert.

## Fußnoten

[^HM]: [HM Microinverter Datasheet](https://www.hoymiles.com/wp-content/uploads/downloadupload/Datasheet_HM-300-350-400_AP_EN_V202206.pdf)

[^IQ7A]: [IQ7A Microinverter Datasheet](https://enphase.com/download/iq7a-microinverter-data-sheet)

[^AN4070]: [AN4070 250 W grid connected microinverter](https://www.st.com/resource/en/application_note/dm00050692-250-w-grid-connected-microinverter-stmicroelectronics.pdf)

[^2]: [An Overview of Current-Fed Power Processing](https://magna-power.com/learn/white-paper/current-fed-power-processing)

[^3]: [DC-Bus Design with Hybrid Capacitor Bank in Single-Phase PV Inverters](https://intelligentpower.engr.uga.edu/wp-content/uploads/2019/10/deqiang2017Dc-bus.pdf) | https://doi.org/10.1109/IECON.2017.8216408

[^4]: [Evaluation of Electrolytic Capacitor Application in Enphase Microinverters](https://www4.enphase.com/sites/default/files/Electrolytic_Capacitor_Expert_Report.pdf)

[^5]: [Reliability Study of Electrolytic Capacitors in a Microinverter](https://www4.enphase.com/sites/default/files/EnphaseElectrolyticCapacitorLife.pdf)
