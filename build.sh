#!/bin/sh
# Rebuild site/ from source/. Needs Python 3 with Pillow (pip install pillow).
set -e
cd "$(dirname "$0")"
rm -rf site && mkdir site
(cd source && python3 buildsite.py ../site)
cp -r source/download site/download
cp source/vercel.json site/vercel.json
echo "Built site/"
