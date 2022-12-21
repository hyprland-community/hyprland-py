import socket
import os

def _connect(path):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(path)
        return s

def connect_events():
    hypr_sock = f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock"
    return _connect(hypr_sock)

def connect_commands():
    hypr_sock = f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock"
    return _connect(hypr_sock)
