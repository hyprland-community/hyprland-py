from __future__ import annotations

import asyncio

from rich import print

from hyprland import hyprctl


async def main():
    client = await hyprctl.active_window_async()
    await hyprctl.reload_async()
    print(client)


asyncio.run(main())
