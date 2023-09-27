#!/bin/bash
set -e

python tools/wiki.py > hyprland/variables.py
black .
isort --profile=black .
pyright .
