from __future__ import annotations

import asyncio

from rich import print

from hyprland.hyprctl import active_window_async


async def main():
   client = await active_window_async()
   print(client)


asyncio.run(main())
