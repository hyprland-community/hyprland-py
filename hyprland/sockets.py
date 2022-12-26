import socket
import os
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
    from .binds import Bind
    from .config import Config

class keyword:    

    async def send_cmd (self,attr,value):
        if isinstance(value, bool):
            value = str(value).lower()
        reader, writer = await asyncio.open_unix_connection(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        writer.write(f'keyword {self.__class__.__name__.lower()}:{attr.replace("__",".")} {str(value)}'.encode())
        await writer.drain()
        resp = await reader.read(100)
        if resp != b'ok':
            raise Exception(f'hyprland: error while setting attribute: {resp}')
        writer.close()

    def __setattr__(self, attr, value,ignore=False):
        if not ignore:
            if isinstance(value, bool):
                value = str(value).lower()
            print(f'keyword {self.__class__.__name__} {attr} {value}')
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
                sock.send(f'keyword {self.__class__.__name__.lower()}:{attr.replace("__",".")} {value}'.encode())
                resp = sock.recv(100)
                if resp != b"ok":
                    return Exception(f"Hyprland Error: {resp}")
        super().__setattr__(attr, value)

class BindListener:

    def __init__(self,config:'Config'):
        self.config = config

    async def handle_bind(self,reader:asyncio.StreamReader,writer:asyncio.StreamWriter):
        data = await reader.read(1024)
        data = data.decode('utf-8')
        print(data)
        if data.startswith('bind '):
            data = data[5:]
            for bind in self.config._binds:
                if str(bind.key) == data:
                    bind.f()
                    writer.write(bytes('ok', 'utf-8'))
                    await writer.drain()
                    return writer.close()
        writer.write(bytes('not ok', 'utf-8'))
        await writer.drain()
        return writer.close()
    
    async def start(self):
        ( not os.path.exists("/tmp/hypr-py/") ) and os.mkdir("/tmp/hypr-py/")
        ( not os.path.exists(f"/tmp/hypr-py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/") ) and os.mkdir(f"/tmp/hypr-py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/")
        os.path.exists(f"/tmp/hypr-py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock") and os.remove(f"/tmp/hypr-py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        server = await asyncio.start_unix_server(self.handle_bind, f"/tmp/hypr-py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        async with server:
            await server.serve_forever()
        
class EventListener:
    
    async def connect(self):
        reader, writer = await asyncio.open_unix_connection(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock")
        yield "connect"
        while True:
            data = await reader.read(1024)
            if not data:
                break
            yield data.decode('utf-8')



def set_bind(bind:'Bind'):
    mod = bind.key.keys()[0]
    key = bind.key[mod]
    label = bind.label