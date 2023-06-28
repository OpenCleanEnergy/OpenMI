# Beitragen zu OpenMI

[![lang-en](https://img.shields.io/badge/lang-en-inactive?style=for-the-badge)](CONTRIBUTING.md)
[![lang-de](https://img.shields.io/badge/lang-de-informational?style=for-the-badge)](CONTRIBUTING.de.md)

## Einrichten des Projektes

Dieser Abschnitt beschreibt, wie du die verschiedenen Teile des Projekts auf eurem System zum Laufen bringt.

### KiCad

1. Installiere die neueste Version von [KiCad](https://www.kicad.org/).
2. Installiere die neueste Version der [KiCad-Db-Lib](https://github.com/Projektanker/kicad-db-lib/releases).
3. Klone das [OpenMI]((https://github.com/OpenCleanEnergy/OpenMI.git)) Repository.
4. Klone das [kicad-library](https://github.com/OpenCleanEnergy/kicad-library) Repository.
5. Starte KiCad und
   1. Klicke `Einstellungen` -> `Pfade konfigurieren...`
      1. Ersetze `KICAD7_FOOTPRINT_DIR` durch den absoluten Pfad des Verzeichnisses `kicad-library/footprints`, also zum Beispiel: *C:\Users\...\Dokumente\GitHub\kicad-library\footprints*
      2. Ersetze `KICAD7_SYMBOL_DIR` durch den absoluten Pfad des Verzeichnisses `kicad-library/symbols`, also zum Beispiel: *C:\Users\...\Documents\GitHub\kicad-library\symbols*
   2. Klicke auf `Einstellungen` -> `Symbolbibliotheken verwalten...`
      1. Klicke unter Globale Bibliotheken auf `Vorhandene Bibliothek zur Tabelle hinzufügen`, gehe in das Verzeichnis `kicad-library/output`, wähle alle Dateien aus und klicke auf `Öffnen`.