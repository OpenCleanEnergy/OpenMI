#!/usr/bin/env bash

EXPORT_ROOT_DIR="export"
EXPORT_SVG_DIR="${EXPORT_ROOT_DIR}/svg"

PROJECT_NAME=${1}
KICAD_SCH="${PROJECT_NAME}.kicad_sch"

echo "📄 Exporting ${KICAD_SCH}"
echo "⚠️ Old files will be removed first!"

rm --force --recursive ${EXPORT_ROOT_DIR}

mkdir -p ${EXPORT_ROOT_DIR}
eeschema_do export \
    --all_pages \
    --file_format pdf\
     ${KICAD_SCH} ${EXPORT_ROOT_DIR}

mkdir -p ${EXPORT_SVG_DIR}
eeschema_do export \
    --all_pages \
    --file_format svg \
    --background_color \
    ${KICAD_SCH} ${EXPORT_SVG_DIR}

echo "✅ Done"
