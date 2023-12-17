# Contributing to OpenMI

## How to get started

This section describes how to get the different parts of the project running at your system.

### KiCad

1. Install the latest version of [KiCad](https://www.kicad.org/).
2. Install the latest release version of the [KiCad-Db-Lib](https://github.com/Projektanker/kicad-db-lib/releases).
3. Clone the [OpenMI]((https://github.com/OpenCleanEnergy/OpenMI.git)) repository.
4. Clone the [kicad-library](https://github.com/OpenCleanEnergy/kicad-library) repository.
5. Start KiCad and
   1. Click `Preferences` -> `Configure Paths...`
      1. Replace the `KICAD7_FOOTPRINT_DIR` by the absolute path of the `kicad-library/footprints`, so for example: *C:\Users\...\Documents\GitHub\kicad-library\footprints*
      2. Replace the` KICAD7_SYMBOL_DIR` by the absolute path of the `kicad-library/symbols`, so for example: *C:\Users\...\Documents\GitHub\kicad-library\symbols*
   2. Click `Preferences` -> `Manage Symbol Libraries...`
      1. Under Global Libraries click `Add existing library to table`, go into the `kicad-library/output` directory and select all files and press `open`.
