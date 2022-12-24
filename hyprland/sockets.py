import socket
import os

class keyword:
    def __setattr__(self, attr, value):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
            sock.send(bytes(f'keyword {self.__class__.__name__.lower()}:{attr.replace("__",".")} {str(value)}', 'utf-8'))
            resp = sock.recv(1024).decode('utf-8')
            if resp != 'ok':
                raise Exception(f'hyprland: error while setting attribute: {resp}')
        super().__setattr__(attr, value)