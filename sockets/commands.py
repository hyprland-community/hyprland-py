import socket
import os

hypr_sock = f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock"

with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.connect(hypr_sock)
    s.sendall(b"keyword general:col.active_border rgba(ffffffff)")
    print(s.recv(1024).decode("utf-8"))