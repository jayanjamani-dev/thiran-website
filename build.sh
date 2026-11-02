#!/bin/sh
# Rebuild site/ from source/. Needs Python 3 with Pillow (pip install pillow).
set -e
cd "$(dirname "$0")"
rm -rf site && mkdir site
(cd source && python3 buildsite.py ../site)
(cd source && python3 buildguides.py ../site "$(cat ../site/.icon)")
cp -r source/download site/download
cp source/vercel.json site/vercel.json
mkdir -p site/og && cp source/og/*.jpg site/og/ 2>/dev/null || echo "No link preview pictures yet: run node source/og/make-og.cjs, then build again"
python3 source/buildseo.py site
rm -f site/.icon
echo "Built site/"
