# Hyprland for Python

![GitHub repo size](https://img.shields.io/github/repo-size/aspizu/hyprland-py)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

An unofficial [type-safe](https://microsoft.github.io/pyright/), async API wrapper for [Hyprland](https://hyprland.org/)'s [IPC](https://wiki.hyprland.org/IPC/) for [Python](https://www.python.org/).

## Examples

[examples/flicko.py](./examples/flicko.py)

```py
import asyncio
from hyprland import (
   Exec,
   Exit,
   Key,
   KillActive,
   Mod,
   MoveToWorkspace,
   SwitchWorkspace,
   WorkspaceID,
)
from hyprland.asyncio import execute_batch


async def main():
   await execute_batch(
      (Mod.SUPER + Key("M")).bind(Exit()),
      (Mod.SUPER + Key("Return")).bind(Exec("wezterm")),
      (Mod.SUPER + Key("Q")).bind(KillActive()),
      *((Mod.SUPER + Key(i)).bind(SwitchWorkspace(WorkspaceID(i))) for i in range(1, 11)),
      *((Mod.SUPER + Mod.SHIFT + Key(i)).bind(MoveToWorkspace(WorkspaceID(i))) for i in range(1, 11)),
   )


asyncio.run(main())
```

## Documentation

View the full documentation in [docs/hyprland/](./docs/hyprland).

## Install

### Dependencies:

-  [msgspec](https://jcristharif.com/msgspec/) for JSON parsing.

### From source

```sh
git clone https://github.com/aspizu/hyprland-py
cd hyprland-py
pip install -r requirements.txt
pip install .
```

### From [PyPI](https://pypi.org/project/hyprland)

```sh
pip install hyprland
```

## Development

### Development dependencies:

-  [isort](https://pycqa.github.io/isort/)
-  [aspizu's black fork](https://github.com/aspizu/black)
-  [pyright](https://microsoft.github.io/pyright/)
-  [documatic](https://github.com/aspizu/documatic)
-  [ruff](https://github.com/astral-sh/ruff)

```sh
git clone https://github.com/aspizu/hyprland-py
cd hyprland-py
git submodule init
git submodule update
pip install -r requirements.txt
./build.sh
pip install -e .
```
