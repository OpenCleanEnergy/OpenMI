# Contributing Guidelines

Thank you for your interest in contributing to our project! At this time, the
project is in its early development stage and we are currently not accepting
external contributions.

## TL;DR

👋 **Thanks for your interest!** We're focused on building a stable prototype.

🚀 **Stay tuned for updates.** Once we're stable, we will provide detailed
guidelines on how you can contribute effectively.

## Why aren't we accepting contributions right now?

The project is in the early stages of development, and we are focused on
establishing a solid foundation and creating a working prototype. Accepting
external contributions at this early stage might introduce complexities that
could hinder our progress.

## When will we start accepting contributions?

We plan to open up the project to external contributions once we reach a more
stable state and have a working prototype. This will allow us to provide a
better experience for contributors and maintainers alike.

## How can you stay involved?

We understand that you may be eager to contribute, and we encourage you to stay
engaged with the project during this early phase:

1. **Star the Repository:** Keep an eye on the repository for updates, releases,
   and announcements.

2. **Spread the Word:** Help us build a community by sharing information about
   the project with others who might be interested.

## How can you contribute in the future?

Once we start accepting contributions, we will provide detailed guidelines on
how you can contribute effectively. This will include information on coding
standards, hardware design practices, issue tracking, and the contribution
process for both software and hardware components.

We appreciate your understanding and patience as we work towards making the
project more accessible to external contributors. If you have any questions or
concerns, please feel free to reach out to us.

Thank you for your support and interest in our project!

Open Clean Energy Team

---

## Discover the project right away.

If you are eager to discover the project follow the instructions below.
The instructions describe how to get the different parts of the project running
at your system.

### Required tools

**Required:**

- [KiCad 7](https://www.kicad.org/download/)

**Optional:**

- [just](https://github.com/casey/just#installation)
  - on Windows [PowerShell 7](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows)
    is required
  - [Docker](https://docs.docker.com/engine/install/)

### KiCad

1. Install the latest version of [KiCad](https://www.kicad.org/).
2. Install the latest release version of the
   [KiCad-Db-Lib](https://github.com/Projektanker/kicad-db-lib/releases).
3. Clone the [OpenMI]((https://github.com/OpenCleanEnergy/OpenMI.git))
   repository.
4. Clone the [kicad-library](https://github.com/OpenCleanEnergy/kicad-library)
   repository.
5. Start KiCad and
   1. Click `Preferences` -> `Configure Paths...`
      1. Replace the `KICAD7_FOOTPRINT_DIR` by the absolute path of the
         `kicad-library/footprints`, so for example:
         *C:\Users\...\Documents\GitHub\kicad-library\footprints*
      2. Replace the` KICAD7_SYMBOL_DIR` by the absolute path of the
         `kicad-library/symbols`, so for example:
         *C:\Users\...\Documents\GitHub\kicad-library\symbols*
   2. Click `Preferences` -> `Manage Symbol Libraries...`
      1. Under Global Libraries click `Add existing library to table`, go into
         the `kicad-library/output` directory and select all files and press
         `open`.
