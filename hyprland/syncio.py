"""Sync commands (Use `hyprland.asyncio` for async versions of the same)."""
from __future__ import annotations

from hyprctl import (
   active_window,
   active_workspace,
   binds,
   clients,
   cursor_position,
   devices,
   global_shortcuts,
   instances,
   kill,
   layers,
   monitors,
   reload,
   set_cursor_theme,
   splash,
   switch_xkb_layout,
   version,
   workspaces,
)

from .socket import execute, execute_batch

__all__ = (
   "active_window",
   "active_workspace",
   "binds",
   "clients",
   "cursor_position",
   "devices",
   "global_shortcuts",
   "instances",
   "kill",
   "layers",
   "monitors",
   "reload",
   "set_cursor_theme",
   "splash",
   "switch_xkb_layout",
   "version",
   "workspaces",
   "execute",
   "execute_batch",
)
