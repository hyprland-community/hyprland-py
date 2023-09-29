"""Async commands (Use `hyprland.syncio` for blocking versions of the same)."""
from __future__ import annotations

from hyprctl import active_window_async as active_window
from hyprctl import active_workspace_async as active_workspace
from hyprctl import binds_async as binds
from hyprctl import clients_async as clients
from hyprctl import cursor_position_async as cursor_position
from hyprctl import devices_async as devices
from hyprctl import global_shortcuts_async as global_shortcuts
from hyprctl import instances_async as instances
from hyprctl import kill_async as kill
from hyprctl import layers_async as layers
from hyprctl import monitors_async as monitors
from hyprctl import reload_async as reload
from hyprctl import set_cursor_theme_async as set_cursor_theme
from hyprctl import splash_async as splash
from hyprctl import switch_xkb_layout_async as switch_xkb_layout
from hyprctl import version_async as version
from hyprctl import workspaces_async as workspaces

from .socket import execute_async as execute
from .socket import execute_batch_async as execute_batch

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
