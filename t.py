import asyncio
import os


async def async_command_send(cmd:str):
    print(cmd)
    reader, writer = await asyncio.open_unix_connection(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket.sock")
    writer.write(cmd.encode())
    await writer.drain()
    resp = await reader.read(100)
    print(resp)
    if resp != b'ok':
        raise Exception(f'hyprland: {cmd.encode()!r} : {resp}')
    writer.close()


async def send_bind():
        cmd = f"keyword bind \"SUPER,y,exec,kitty\""
        await async_command_send(f'{cmd}')

asyncio.run(send_bind())