from __future__ import annotations

import asyncio
import socket
from itertools import chain
from os import getenv
from pathlib import Path
from typing import Any, Callable, Coroutine, Iterable, overload

from .errors import HyprlandError

BUFFER_SIZE = 1024
"The size of the buffer used to recieve messages from the IPC socket. Responses will be truncated if this is not large enough."

# <https://wiki.hyprland.org/IPC/>

HYPRLAND_INSTANCE_SIGNATURE = getenv("HYPRLAND_INSTANCE_SIGNATURE")
if HYPRLAND_INSTANCE_SIGNATURE is None:
   raise RuntimeError("The env variable HYPRLAND_INSTANCE_SIGNATURE was not set, are you running inside Hyprland?")

HYPRLAND_SOCKET_ADDRESS: Path = Path("/tmp/hypr") / HYPRLAND_INSTANCE_SIGNATURE / ".socket.sock"
HYPRLAND_SOCKET2_ADDRESS: Path = Path("/tmp/hypr") / HYPRLAND_INSTANCE_SIGNATURE / ".socket2.sock"


def _socket():
   """Opens a connection to the Hyprland's hyprctl IPC socket."""
   sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
   sock.connect(HYPRLAND_SOCKET_ADDRESS.as_posix())
   return sock


class Command:
   def to_command(self) -> bytes:
      raise NotImplementedError


def query(command: bytes):
   """Executes a hyprctl command using the IPC socket with the json flag and returns the response."""
   sock = _socket()
   sock.send(b"j/" + command)
   # FIXME: Raise appropriate exception on error.
   return sock.recv(BUFFER_SIZE)


def execute(command: Command | bytes):
   """Executes a hyprctl command using the IPC socket. Raises `HyprlandError` on error."""
   sock = _socket()
   sock.send(b"/" + command.to_command() if isinstance(command, Command) else command)
   response = sock.recv(BUFFER_SIZE)
   if response != b"ok":
      raise HyprlandError(command, response)


@overload
def execute_batch(commands: Iterable[Command | bytes]) -> None:
   ...


@overload
def execute_batch(*commands: Command | bytes) -> None:
   ...


def execute_batch(commands: Iterable[Command | bytes] | Command | bytes, *args: Command | bytes):
   """Executes a batch of hyprctl command using the IPC socket. Raises `HyprlandError` on error."""
   if isinstance(commands, (bytes, Command)):
      commands = chain([commands], args)
   sock = _socket()
   # FIXME: The batch flag is wrong/ does not work.
   sock.send(b"b/" + b";".join(i.to_command() if isinstance(i, Command) else i for i in commands))
   response = sock.recv(BUFFER_SIZE)
   if response != b"ok":
      raise HyprlandError(commands, response)


async def socket2():
   reader, _DO_NOT_DEL = await asyncio.open_unix_connection(HYPRLAND_SOCKET2_ADDRESS)
   while data := await reader.readuntil(b"\n"):
      yield data[:-1].split(b">>")


R = Coroutine[Any, Any, None]


class Events:
   def __init__(self):
      self._workspace = None
      self._focusedmon = None
      self._activewindow = None
      self._activewindowv2 = None
      self._fullscreen = None
      self._monitorremoved = None
      self._monitoradded = None
      self._createworkspace = None
      self._destroyworkspace = None
      self._moveworkspace = None
      self._renameworkspace = None
      self._activespecial = None
      self._activelayout = None
      self._openwindow = None
      self._closewindow = None
      self._movewindow = None
      self._openlayer = None
      self._closelayer = None
      self._submap = None
      self._changefloatingmode = None
      self._urgent = None
      self._minimize = None
      self._screencast = None
      self._windowtitle = None
      self._ignoregrouplock = None
      self._lockgroups = None

   def workspace(self, f: Callable[[str], R]):
      """
      Emitted on workspace change. Is emitted ONLY when a user requests a workspace change, and is not emitted on mouse
      movements. See `activemon`.
      `(workspace_name)`
      """
      self._workspace = f

   def focusedmon(self, f: Callable[[str, str], R]):
      """
      Emitted on the active monitor being changed.
      `(mon_name, workspace_name)`
      """
      self._focusedmon = f

   def activewindow(self, f: Callable[[str, str], R]):
      """
      Emitted on the active window being changed.
      `(window_class, window_title)`
      """
      self._activewindow = f

   def activewindowv2(self, f: Callable[[str], R]):
      """
      Emitted on the active window being changed.
      `(window_address)`
      """
      self._activewindowv2 = f

   def fullscreen(self, f: Callable[[bool], R]):
      """
      Emitted when a fullscreen status of a window changes.
      `(window_entered_fullscreen)`
      """
      self._fullscreen = f

   def monitorremoved(self, f: Callable[[str], R]):
      """
      Emitted when a monitor is removed (disconnected).
      `(monitor_name)`
      """
      self._monitorremoved = f

   def monitoradded(self, f: Callable[[str], R]):
      """
      `(monitor_name)`
      """
      self._monitoradded = f

   def createworkspace(self, f: Callable[[str], R]):
      self._createworkspace = f

   def destroyworkspace(self, f: Callable[[str], R]):
      self._destroyworkspace = f

   def moveworkspace(self, f: Callable[[str], R]):
      self._moveworkspace = f

   def renameworkspace(self, f: Callable[[str], R]):
      self._renameworkspace = f

   def activespecial(self, f: Callable[[str], R]):
      self._activespecial = f

   def activelayout(self, f: Callable[[str], R]):
      self._activelayout = f

   def openwindow(self, f: Callable[[str], R]):
      self._openwindow = f

   def closewindow(self, f: Callable[[str], R]):
      self._closewindow = f

   def movewindow(self, f: Callable[[str], R]):
      self._movewindow = f

   def openlayer(self, f: Callable[[str], R]):
      self._openlayer = f

   def closelayer(self, f: Callable[[str], R]):
      self._closelayer = f

   def submap(self, f: Callable[[str], R]):
      self._submap = f

   def changefloatingmode(self, f: Callable[[str], R]):
      self._changefloatingmode = f

   def urgent(self, f: Callable[[str], R]):
      self._urgent = f

   def minimize(self, f: Callable[[str], R]):
      self._minimize = f

   def screencast(self, f: Callable[[str], R]):
      self._screencast = f

   def windowtitle(self, f: Callable[[str], R]):
      self._windowtitle = f

   def ignoregrouplock(self, f: Callable[[str], R]):
      self._ignoregrouplock = f

   def lockgroups(self, f: Callable[[str], R]):
      self._lockgroups = f

   async def listen(self):
      async for event in socket2():
         match event[0]:
            case b"workspace":
               if self._workspace:
                  await self._workspace(event[1].decode())
            case b"focusedmon":
               if self._focusedmon:
                  args = event[1].split(b",", 1)
                  await self._focusedmon(args[0].decode(), args[1].decode())
            case b"activewindow":
               if self._activewindow:
                  args = event[1].split(b",", 1)
                  await self._activewindow(args[0].decode(), args[1].decode())
            case b"activewindowv2":
               if self._activewindowv2:
                  await self._activewindowv2(event[1].decode())
            case b"fullscreen":
               if self._fullscreen:
                  await self._fullscreen(event[1] == b"1")
            case b"monitorremoved":
               if self._monitorremoved:
                  await self._monitorremoved(event[1].decode())
            case b"monitoradded":
               if self._monitoradded:
                  await self._monitoradded(event[1].decode())
            case a:
               raise HyprlandError("Unhandled event", a)
