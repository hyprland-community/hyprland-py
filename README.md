# Hyprland-py
An unofficial python wrapper for Hyprland's IPC

- [x] event listener
- [x] change config options
- [x] hyprland info
- [x] dispatchers
- [ ] binds
- [x] window object
- [x] monitor object
- [x] workspace object
- [ ] handle color values
- [x] socket commands
- [ ] docs

# Install

### git

from git
```py
pip install git+https://github.com/hyprland-community/hyprland-py
```

# Example
```py
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
    
# print(hyprland.Workspace.from_id(1))

print("starting")

config = hyprland.config.Default()
config.animations.enabled = True


workspace = hyprland.Workspace.from_id(1)
workspace.fetch_windows()

# fetch all workspaces
hyprland.fetch_workspaces()

asyncio.run(main())
```