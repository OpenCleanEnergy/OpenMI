# Beitragen zu OpenMI

[![lang-en](https://img.shields.io/badge/lang-en-inactive?style=for-the-badge)](CONTRIBUTING.md)
[![lang-de](https://img.shields.io/badge/lang-de-informational?style=for-the-badge)](CONTRIBUTING.de.md)

## Einrichten des Projektes

Dieser Abschnitt beschreibt, wie ihr die verschiedenen Teile des Projekts auf eurem System zum Laufen bringt.

### KiCad

1. Installiert die neueste Version von [KiCad] (https://www.kicad.org/).
2. Installiert die neueste Version der [KiCad-Db-Lib](https://github.com/Projektanker/kicad-db-lib/releases).
3. Klone das [OpenMI]((https://github.com/OpenCleanEnergy/OpenMI.git)) Repository.
4. Klonen Sie das [kicad-library](https://github.com/OpenCleanEnergy/kicad-library) Repository.
5. Starte KiCad-Db-Lib und öffne das soeben geklonte Verzeichnis `kicad-library` als Arbeitsbereich und drücke anschließend auf `build`.
6. Starte KiCad und
   1. Klicke `Einstellungen` -> `Pfade konfigurieren...`
      1. Ersetzen Sie `KICAD7_FOOTPRINT_DIR` durch den absoluten Pfad des Verzeichnisses `Footprints` innerhalb der `kicad-library`, also zum Beispiel: C:\Users\jarib\Dokumente\GitHub\kicad-library\footprints
      2. Ersetzen Sie `KICAD7_SYMBOL_DIR` durch den absoluten Pfad des `Symbols`-Verzeichnisses innerhalb der `kicad-library`, also zum Beispiel: C:\Users\jarib\Documents\GitHub\kicad-library\symbols
   2. Klicken Sie auf `Einstellungen` -> `Symbolbibliotheken verwalten...`
      1. Klicken Sie unter Globale Bibliotheken auf `Vorhandene Bibliothek zur Tabelle hinzufügen`, gehen Sie in das Verzeichnis `Output`, wählen Sie alle Dateien aus und klicken Sie auf `Öffnen`.