from __future__ import annotations

import asyncio
import socket
from itertools import chain
from os import getenv
from pathlib import Path
from typing import TYPE_CHECKING, overload

from .errors import HyprlandError

if TYPE_CHECKING:
   from collections.abc import Iterable

BUFFER_SIZE = 1024
"The size of the buffer used to recieve messages from the IPC socket. Responses will be truncated if this is not large enough."

# <https://wiki.hyprland.org/IPC/>

HYPRLAND_INSTANCE_SIGNATURE = getenv("HYPRLAND_INSTANCE_SIGNATURE")
if HYPRLAND_INSTANCE_SIGNATURE is None:
   msg = "The env variable HYPRLAND_INSTANCE_SIGNATURE was not set, are you running inside Hyprland?"
   raise RuntimeError(msg)

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


async def query_async(command: bytes):
   """Executes a hyprctl command using the IPC socket with the json flag and returns the response."""
   reader, writer = await asyncio.open_unix_connection(HYPRLAND_SOCKET_ADDRESS)
   writer.write(b"j/" + command)
   # FIXME: Raise appropriate exception on error.
   return await reader.read()


def execute(command: Command | bytes):
   """Executes a hyprctl command using the IPC socket. Raises `HyprlandError` on error."""
   sock = _socket()
   sock.send(b"/" + command.to_command() if isinstance(command, Command) else command)
   response = sock.recv(BUFFER_SIZE)
   if response != b"ok":
      raise HyprlandError(command, response)


async def execute_async(command: Command | bytes):
   """Executes a hyprctl command using the IPC socket. Raises `HyprlandError` on error."""
   reader, writer = await asyncio.open_unix_connection(HYPRLAND_SOCKET_ADDRESS)
   writer.write(b"/" + command.to_command() if isinstance(command, Command) else command)
   response = await reader.read()
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
   if isinstance(commands, bytes | Command):
      commands = chain([commands], args)
   sock = _socket()
   # FIXME: The batch flag is wrong/ does not work.
   sock.send(b"b/" + b";".join(i.to_command() if isinstance(i, Command) else i for i in commands))
   response = sock.recv(BUFFER_SIZE)
   if response != b"ok":
      raise HyprlandError(commands, response)


@overload
async def execute_batch_async(commands: Iterable[Command | bytes]) -> None:
   ...


@overload
async def execute_batch_async(*commands: Command | bytes) -> None:
   ...


async def execute_batch_async(commands: Iterable[Command | bytes] | Command | bytes, *args: Command | bytes):
   """Executes a batch of hyprctl command using the IPC socket. Raises `HyprlandError` on error."""
   if isinstance(commands, bytes | Command):
      commands = chain([commands], args)
   reader, writer = await asyncio.open_unix_connection(HYPRLAND_SOCKET_ADDRESS)
   # FIXME: The batch flag is wrong/ does not work.
   writer.write(b"b/" + b";".join(i.to_command() if isinstance(i, Command) else i for i in commands))
   response = await reader.read()
   if response != b"ok":
      raise HyprlandError(commands, response)
