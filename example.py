import hyprland
import asyncio

hypr = hyprland.Events()

@hypr.on("connect")
async def on_connect():
    print("Connected to the socket")

@hypr.on("workspace")
async def on_workspace(data):
    print(data)

@hypr.on("activewindow")
async def on_activewindow(win_class,title):
    print(win_class,title)

print(hyprland.fetch_version())

async def main():
    print(hyprland.fetch_workspaces())
    await hypr.async_connect()

print("starting")
asyncio.run(main())