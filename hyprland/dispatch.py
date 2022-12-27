from .sockets import async_hyprctl

class Dispatch:
    async def exec(cmd):
        await async_hyprctl(f'dispatch -- exec {cmd}')