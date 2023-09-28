#!/bin/bash
set -e

python tools/wiki.py > hyprland/variables.py
isort --profile=black .
black .
pyright .
python -m documatic
