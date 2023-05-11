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

### Topologie

TODO: Push-Pull mit Gain usw.





### Mikrocontroller

ESP32

## Wie kann der Mikro-Wechselrichter simuliert werden?

Das Schaltungsdesign des Mikro-Wechselrichters wurde in [LTspice](https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html) simuliert. Alle LTspice Simulationen sind im Ordner [simulation](simulation) abgelegt.
Da das gesamte Schaltungsdesign schnell komplex und aufwändig zu simulieren ist, wurden die einzelnen Bausteine der Schaltung zunächst einzeln aufgebaut und simuliert.

### Solarmodul und Auslegung der Eingangskapazität
Ein [Solarmodul in LTspice](simulation/pv-panel-input) wurde nach der Anleitung von [FesZ Electronics](https://www.youtube.com/watch?v=ox0UtYe4owI) modelliert.

Die vom Solarmodul abgegebene Leistung berechnet sich nach $P_{PV} = U_{PV} \cdot I_{PV}$.

Zunächst kann für das simulierte Solarmodul der Punkt gefunden werden, an dem die Leistung $P_{PV}$ maximal ist. Dieser Punkt wird auch Maximum Power Point (MPP) genannt.
![](simulation/pv-panel-input/pv-panel-mpp.emf "Grafik zur Ermittlung des MPP")

Zur Auslegung der Eingangskapazität ... TODO

### Push-Pull Wechselrichter 
Die [Simulation des Push-Pull Wechselrichters](simulation/push-pull-inverter) ... TODO

#### Auslegung des Transformators

TODO:
