from __future__ import annotations

import msgspec.json as json
from msgspec import Struct, field

from .socket import execute, execute_async, query, query_async


class IncompleteWorkspace(Struct):
   id: int
   name: str


class Monitor(Struct):
   id: int
   name: str
   description: str
   make: str
   model: str
   serial: str
   width: int
   height: int
   refresh_rate: float = field(name="refreshRate")
   x: int
   y: int
   active_workspace: IncompleteWorkspace = field(name="activeWorkspace")
   special_workspace: IncompleteWorkspace = field(name="specialWorkspace")
   reserved: list[int]
   scale: float
   transform: float
   focused: bool
   dpms_status: bool = field(name="dpmsStatus")
   vrr: bool


class Workspace(Struct):
   id: int
   name: str
   monitor: str
   windows: int
   has_fullscreen: bool = field(name="hasfullscreen")
   last_window: str = field(name="lastwindow")
   last_window_title: str = field(name="lastwindowtitle")


class Client(Struct):
   address: str
   mapped: bool
   hidden: bool
   at: tuple[int, int]
   size: tuple[int, int]
   workspace: IncompleteWorkspace
   floating: bool
   monitor: int
   cls: str = field(name="class")
   title: str
   initial_cls: str = field(name="initialClass")
   initial_title: str = field(name="initialTitle")
   pid: int
   xwayland: bool
   pinned: bool
   fullscreen: bool
   fullscreen_mode: int = field(name="fullscreenMode")
   fake_fullscreen: bool = field(name="fakeFullscreen")
   grouped: list[str]
   swallowing: None  # FIXME: Type is unknown, is null for any case on my system.


class Layers(Struct):
   levels: dict[int, list[Layer]]


class Layer(Struct):
   address: str
   x: int
   y: int
   w: int
   h: int
   namespace: str


class Devices(Struct):
   mice: list[Mouse]
   keyboards: list[Keyboard]
   tablets: list[Tablet]
   touch: list[Touch]
   switches: list[Switch]


class Mouse(Struct):
   address: str
   name: str
   default_speed: float = field(name="defaultSpeed")


class Keyboard(Struct):
   address: str
   name: str
   rules: str
   model: str
   layout: str
   variant: str
   options: str
   active_keymap: str
   main: bool


class Tablet(Struct):
   address: str
   name: str


class Touch(Struct):
   address: str
   name: str


class Switch(Struct):
   address: str
   name: str


class Bind(Struct):
   locked: bool
   mouse: bool
   release: bool
   repeat: bool
   non_consuming: bool
   modmask: int
   submap: str
   key: str
   keycode: int
   dispatcher: str
   arg: str


class Version(Struct):
   branch: str
   commit: str
   dirty: bool
   commit_message: str
   tag: str
   flags: list[str]


class CursorPosition(Struct):
   x: int
   y: int


class Instance(Struct):
   instance: str
   time: int
   pid: int
   wl_socket: str


def monitors():
   return json.decode(query(b"monitors"), type=list[Monitor])


def workspaces():
   return json.decode(query(b"workspaces"), type=list[Workspace])


def active_workspace():
   return json.decode(query(b"activeworkspace"), type=Workspace)


def clients():
   return json.decode(query(b"clients"), type=list[Client])


def active_window():
   return json.decode(query(b"activewindow"), type=Client)


def layers():
   return json.decode(query(b"layers"), type=dict[str, Layers])


def devices():
   return json.decode(query(b"devices"), type=Devices)


def binds():
   """See `binds.Keybind.from_bind()` to get key combination information."""
   return json.decode(query(b"binds"), type=list[Bind])


def version():
   return json.decode(query(b"version"), type=Version)


def splash():
   return query(b"splash").decode()


def cursor_position():
   return json.decode(query(b"cursorpos"), type=CursorPosition)


def global_shortcuts():
   raise NotImplementedError


def instances():
   return json.decode(query(b"instances"), type=list[Instance])


def reload():
   """Reload configuration"""
   execute(b"reload")


def kill():
   """Kill Hyprland"""
   execute(b"kill")


def set_cursor_theme(theme: str, size: int):
   execute(b"cursor " + theme.encode() + b" " + str(size).encode())


def switch_xkb_layout(device: str, cmd: str):
   execute(b"switchxkblayout " + device.encode() + b" " + cmd.encode())


async def monitors_async():
   return json.decode(await query_async(b"monitors"), type=list[Monitor])


async def workspaces_async():
   return json.decode(await query_async(b"workspaces"), type=list[Workspace])


async def active_workspace_async():
   return json.decode(await query_async(b"activeworkspace"), type=Workspace)


async def clients_async():
   return json.decode(await query_async(b"clients"), type=list[Client])


async def active_window_async():
   return json.decode(await query_async(b"activewindow"), type=Client)


async def layers_async():
   return json.decode(await query_async(b"layers"), type=dict[str, Layers])


async def devices_async():
   return json.decode(await query_async(b"devices"), type=Devices)


async def binds_async():
   """See `binds.Keybind.from_bind()` to get key combination information."""
   return json.decode(await query_async(b"binds"), type=list[Bind])


async def version_async():
   return json.decode(await query_async(b"version"), type=Version)


async def splash_async():
   return (await query_async(b"splash")).decode()


async def cursor_position_async():
   return json.decode(await query_async(b"cursorpos"), type=CursorPosition)


async def global_shortcuts_async():
   raise NotImplementedError


async def instances_async():
   return json.decode(await query_async(b"instances"), type=list[Instance])


async def reload_async():
   """Reload configuration"""
   await execute_async(b"reload")


async def kill_async():
   """Kill Hyprland"""
   await execute_async(b"kill")


async def set_cursor_theme_async(theme: str, size: int):
   await execute_async(b"cursor " + theme.encode() + b" " + str(size).encode())


async def switch_xkb_layout_async(device: str, cmd: str):
   await execute_async(b"switchxkblayout " + device.encode() + b" " + cmd.encode())
