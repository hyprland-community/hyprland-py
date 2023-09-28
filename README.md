# Hyprland for Python

An unofficial [type-safe](https://microsoft.github.io/pyright/), async API wrapper for [Hyprland](https://hyprland.org/)'s [IPC](https://wiki.hyprland.org/IPC/) for [Python](https://www.python.org/).

## Examples

[examples/flicko.py](./examples/flicko.py)

```py
from __future__ import annotations

import asyncio

from hyprland.binds import Key, Mod
from hyprland.dispatch import (
   Exec,
   Exit,
   KillActive,
   MoveToWorkspace,
   Workspace,
   WorkspaceID,
)
from hyprland.socket import execute_batch_async


async def main():
   await execute_batch_async(
      (Mod.SUPER + Key("M")).bind(Exit()),
      (Mod.SUPER + Key("Return")).bind(Exec("wezterm")),
      (Mod.SUPER + Key("Q")).bind(KillActive()),
      *((Mod.SUPER + Key(str(i))).bind(Workspace(WorkspaceID(i))) for i in range(1, 11)),
      *((Mod.SUPER + Mod.SHIFT + Key(str(i))).bind(MoveToWorkspace(WorkspaceID(i))) for i in range(1, 11)),
   )


asyncio.run(main())
```

### Dependencies

-  [msgspec](https://jcristharif.com/msgspec/) for JSON parsing.

## Documentation

View the full documentation in [docs/hyprland/](./docs/hyprland).

## Install

### From source

```sh
git clone https://github.com/aspizu/hyprland-py
cd hyprland-py
pip install msgspec
pip install .
```

### From [PyPI](https://pypi.org/project/hyprland)

```sh
pip install hyprland
```
