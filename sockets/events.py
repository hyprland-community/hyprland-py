import socket
import os

def recv():
    hypr_sock = f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock"
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        try:
            s.connect(hypr_sock)
        except ConnectionRefusedError:
            yield "", Exception("failed to connect to socket")
        while 1:
            data = s.recv(1024)
            if not data:
                yield "", Exception("No data received")
                break
            yield data.decode("utf-8"), None