# Docker container for KiCad automation

## Build Docker image

```bash
docker build --tag pipeline .
```

## Generate PDF file from schematic

``` bash
docker run --rm -v "${PWD}/OpenMI:/workspace" pipeline export OpenMI.kicad_sch
```
