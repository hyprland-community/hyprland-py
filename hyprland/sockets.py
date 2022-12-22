import socket
import os

def _connect(path):
    return 0

def connect_events():
    hypr_sock = f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock"
    return _connect(hypr_sock)


class _command:
    def __setattr__(self, attr, value):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
            print('from inside __setattr__ : ',sock)
            print(bytes(f'keyword {self.__class__.__name__.lower()}:{attr} {str(value)}', 'utf-8'))
            sock.send(bytes(f'keyword {self.__class__.__name__.lower()}:{attr.replace("__",".")} {str(value)}', 'utf-8'))
            print(sock.recv(1024).decode('utf-8'))
        super().__setattr__(attr, value)