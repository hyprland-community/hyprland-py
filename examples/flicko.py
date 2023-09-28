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
