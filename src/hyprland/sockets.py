import socket
import os
from typing import TYPE_CHECKING
import asyncio

if TYPE_CHECKING:
    from .binds import Bind
    from .config import Config


def command_send(cmd:str):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        sock.send(cmd.encode())
        resp = sock.recv(100)
        if resp != b"ok":
            return Exception(f"Hyprland Error: {cmd} : {resp}")

async def async_command_send(cmd:str, ignore_ok:bool=False):
    reader, writer = await asyncio.open_unix_connection(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
    writer.write(cmd.encode())
    await writer.drain()
    resp = await reader.read(100)
    writer.close()
    if not ignore_ok and resp != b'ok':
        raise Exception(f'hyprland: {cmd.encode()!r} : {resp}')
    else:
        return resp
    

async def async_hyprctl(cmd:str):
    p = await asyncio.create_subprocess_shell(f'hyprctl {cmd}', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    await p.wait()
    resp = (await p.stdout.read()).decode('utf-8').strip()
    return resp
        

class keyword:    

    async def send_cmd (self,attr,value):
        if isinstance(value, bool):
            value = str(value).lower()
        await async_command_send(f'keyword {self.__class__.__name__.lower()}:{attr.replace("__",".")} {str(value)}')

    def __setattr__(self, attr, value,ignore=False):
        if not ignore:
            if isinstance(value, bool):
                value = str(value).lower()
            command_send(f'keyword {self.__class__.__name__.lower()}:{attr.replace("__",".")} {value}')
        super().__setattr__(attr, value)

class BindListener:

    def __init__(self,config:'Config'):
        self.config = config

    async def send_bind(self,bind:'Bind'):
        if isinstance(bind.f,str):
            cmd = f"keyword bind{bind.flag} \"{','.join(bind.key) },{bind.f}\""
        else:
            cmd = f"keyword bind{bind.flag} \"{','.join(bind.key) },exec,echo bind.{'.'.join(bind.key)} | socat unix-connect:/tmp/hypr_py/$HYPRLAND_INSTANCE_SIGNATURE/.socket.sock STDIO\""
        await async_hyprctl(cmd)

    async def handle_bind(self,reader:asyncio.StreamReader,writer:asyncio.StreamWriter):
        data = await reader.read(1024)
        data = data.decode('utf-8')
        if data.startswith('bind.'):
            data = data[5:].strip()
            for bind in self.config._binds:
                if ".".join(bind.key) == data:
                    await bind.f(*bind.args)
                    writer.write(bytes('ok', 'utf-8'))
                    await writer.drain()
                    return writer.close()
        writer.write(bytes('not ok', 'utf-8'))
        await writer.drain()
        return writer.close()
    
    async def start(self):
        ( not os.path.exists("/tmp/hypr_py/") ) and os.mkdir("/tmp/hypr_py/")
        ( not os.path.exists(f"/tmp/hypr_py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/") ) and os.mkdir(f"/tmp/hypr_py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/")
        os.path.exists(f"/tmp/hypr_py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock") and os.remove(f"/tmp/hypr_py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        server = await asyncio.start_unix_server(self.handle_bind, f"/tmp/hypr_py/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        async with server:
            await server.serve_forever()
        
class EventListener:
    
    def start(self):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock")
            yield "connect"
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                yield data.decode('utf-8')


    async def async_start(self):
        reader, writer = await asyncio.open_unix_connection(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock")
        yield "connect"

        buffer = b""
        while True:
            new_data = await reader.read(1024)
            if not new_data:
                break
            buffer += new_data
            while b"\n" in buffer:
                data, buffer = buffer.split(b"\n", 1)
                yield data.decode("utf-8")
