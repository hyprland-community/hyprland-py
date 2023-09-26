from __future__ import annotations

import socket
from os import getenv
from pathlib import Path

from .errors import HyprlandError

BUFFER_SIZE = 1024
"The size of the buffer used to recieve messages from the IPC socket. Responses will be truncated if this is not large enough."

# <https://wiki.hyprland.org/IPC/>

HYPRLAND_INSTANCE_SIGNATURE = getenv("HYPRLAND_INSTANCE_SIGNATURE")
if HYPRLAND_INSTANCE_SIGNATURE is None:
   raise RuntimeError("The env variable HYPRLAND_INSTANCE_SIGNATURE was not set, are you running inside Hyprland?")

HYPRLAND_SOCKET_ADDRESS: Path = Path("/tmp/hypr") / HYPRLAND_INSTANCE_SIGNATURE / ".socket.sock"


def _socket():
   """Opens a connection to the Hyprland's hyprctl IPC socket."""
   sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
   sock.connect(HYPRLAND_SOCKET_ADDRESS.as_posix())
   return sock


def query(command: bytes):
   """Executes a hyprctl command using the IPC socket with the json flag and returns the response."""
   sock = _socket()
   sock.send(b"j/" + command)
   # FIXME: Raise appropriate exception on error.
   return sock.recv(BUFFER_SIZE)


def execute(command: bytes):
   """Executes a hyprctl command using the IPC socket. Raises `HyprlandError` on error."""
   sock = _socket()
   sock.send(b"/" + command)
   response = sock.recv(BUFFER_SIZE)
   if response != b"ok":
      raise HyprlandError(command, response)
