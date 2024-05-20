import asyncio
import socket
import os
import json

class UnknownRequest(Exception):
    ...

def command_send(cmd:str, return_json = True, check_ok = False):
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(f"{os.getenv('XDG_RUNTIME_DIR')}/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
        if return_json:
            cmd = f"[j]/{cmd}"
        sock.send(cmd.encode())
        resp = sock.recv(8192)

        while True:
            new_data = sock.recv(8192)
            if not new_data:
                break
            resp += new_data

        match resp:
            case b'ok' if check_ok:
                return True
            case b'unknown request':
                raise UnknownRequest(f'{cmd.encode()!r} : {resp}')
            case _:
                
                if check_ok and resp != b'ok':
                    raise Exception(f"Command failed: {cmd.encode()!r} : {resp}")
                
                if return_json and not check_ok:
                    return json.loads(resp.decode())
                
                return resp.decode()

async def async_command_send(cmd:str, return_json = True):
    reader, writer = await asyncio.open_unix_connection(f"{os.getenv('XDG_RUNTIME_DIR')}/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
    if return_json:
        cmd = f"[j]/{cmd}"
    writer.write(cmd.encode())
    await writer.drain()
    resp = await reader.read(8192)

    while True:
        new_data = await reader.read(8192)
        if not new_data:
            break
        resp += new_data

    writer.close()

    match resp:
        case b'unknown request':
            raise UnknownRequest(f'{cmd.encode()!r} : {resp}')
        case _:
            if return_json:
                return json.loads(resp.decode())
            return resp.decode()

class EventListener:
    async def start(self):
        reader, _ = await asyncio.open_unix_connection(f"{os.getenv('XDG_RUNTIME_DIR')}/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock")
        yield "connect"

        buffer = b""
        while True:
            new_data = await reader.read(8192)
            if not new_data:
                break
            buffer += new_data
            while b"\n" in buffer:
                data, buffer = buffer.split(b"\n", 1)
                yield data.decode("utf-8")