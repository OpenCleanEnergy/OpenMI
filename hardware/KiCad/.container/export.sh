#!/usr/bin/env bash
set -euo pipefail

EXPORT_ROOT_DIR="export"
EXPORT_SVG_DIR="$EXPORT_ROOT_DIR/svg"
HASH_FILE="$EXPORT_ROOT_DIR/.kicad_sch_hash"

PROJECT_NAME=$1
KICAD_SCH="$PROJECT_NAME.kicad_sch"

echo "📄 Exporting $KICAD_SCH"

echo "🔎 Checking schematic for changes..."
OLD_HASH=$(test -f "$HASH_FILE" && cat "$HASH_FILE" || echo "0")
NEW_HASH=$(find -type f -iname "*.kicad_sch" | sort | xargs sha256sum | sha256sum | head --bytes 64)

if [ $OLD_HASH == $NEW_HASH ]; then
  echo "... no changes detected."
  echo "✅ Skipped export."
  exit 0
fi

echo "⚠️ Old files will be removed first!"
rm --force --recursive $EXPORT_ROOT_DIR
mkdir --parent $EXPORT_ROOT_DIR

echo "🧮 Wriing new hash to file."
echo "$NEW_HASH" > $HASH_FILE

echo "📃 Exporting to PDF."
mkdir -p $EXPORT_ROOT_DIR
eeschema_do export \
    --all_pages \
    --file_format pdf\
     $KICAD_SCH $EXPORT_ROOT_DIR

echo "🖼️ Exporting to SVG."
mkdir -p $EXPORT_SVG_DIR
eeschema_do export \
    --all_pages \
    --file_format svg \
    --background_color \
    $KICAD_SCH $EXPORT_SVG_DIR

echo "✅ Done"
