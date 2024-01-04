# Docker container for KiCad automation

## Build Docker image

```bash
docker build --tag pipeline .
```

## Generate PDF file from schematic

``` bash
cd OpenMI && \
docker run --rm -v "${PWD}:/workspace" pipeline export OpenMI.kicad_sch
```
