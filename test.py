import socket
import os


with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
    sock.send(bytes(f'keyword general:col.active_border 0xffff00ff', 'utf-8'))
    print(sock.recv(1024).decode('utf-8'))
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
    sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
    sock.send(bytes(f'keyword general:border_size 10', 'utf-8'))
    print(sock.recv(1024).decode('utf-8'))
