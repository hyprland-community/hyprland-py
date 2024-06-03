from .socket import command_send, async_command_send

from .obj.monitor import Monitor
from .obj.workspace import Workspace
from .obj.window import Window, WindowIdentity

from typing import Optional

def fetch_version()->str:
    return command_send("version")["tag"]

def fetch_monitors(all:bool=False, id:Optional[int]=None)->list[Monitor]:
    """lists active outputs, 'monitors all' lists active and inactive outputs"""

    monitors = []

    for data in command_send("monitors all" if all else "monitors"):
        
        monitors.append(Monitor.from_json(data))
    
    return monitors

def fetch_workspaces(id:Optional[int]=None)->list[Workspace] | Workspace:
    """lists all workspaces"""
    workspaces = []

    for data in command_send("workspaces"):
        if id and data["id"] == id:
            return Workspace.from_json(data)
        workspaces.append(Workspace.from_json(data))

    return workspaces

def fetch_active_workspace()->Workspace:
    """gets the active workspace"""

    return Workspace.from_json(command_send("activeworkspace"))

def fetch_workspace_rules()->list:
    """gets the list of defined workspace rules"""

    return command_send("workspacerules")

def fetch_clients(window:Optional[WindowIdentity]=None)->list[Window] | Window:
    """lists all windows"""
    windows = []
    for data in command_send("clients"):
        if window and data[window.key] == window.value:
            return Window.from_json(data)
        windows.append(Window.from_json(data))
    return windows

def fetch_devices()->list:
    """lists all connected keyboards and mice"""
    return command_send("devices")

def fetch_decorations(window:WindowIdentity)->list:
    """lists all decorations on a window"""
    return command_send(f"decorations {window.identifier}")

def fetch_binds()->list:
    """lists all registered binds"""
    return command_send("binds")

def fetch_active_window()->Window:
    """gets the active window"""
    return Window.from_json(command_send("activewindow"))

def fetch_layers()->dict:
    """lists all the layers"""
    return command_send("layers")

def fetch_splash()->str:
    """the current random splash"""
    return command_send("splash")

def fetch_option(key:str)->dict:
    """gets the config option status (values)"""
    return command_send(f"getoption {key}")

def fetch_cursor_pos() -> list[int, int]:
    """gets the current cursor position in global layout coordinates"""
    return command_send("cursorpos")

def fetch_animations() -> list:
    """gets the currently configured info about animations and beziers"""
    return command_send("animations")

def fetch_instances() -> list:
    """lists all running instances of Hyprland with their info"""
    return command_send("instances")

def fetch_layouts() -> list:
    """lists all layouts available (including from plugins)"""
    return command_send("layouts")

def fetch_config_errors() -> list:
    """lists all current config parsing errors"""
    return command_send("configerrors")

def fetch_rolling_log() -> str:
    """tail of the hyprland log"""
    return command_send("rollinglog",return_json=False)

def fetch_locked_state() -> bool:
    """whether the current session is locked"""
    return command_send("locked", return_json=False)