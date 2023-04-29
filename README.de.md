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

### Transformator

TODO:

### Mikrocontroller

ESP32