from .socket import command_send, async_command_send
from dataclasses import dataclass   
from enum import StrEnum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from .obj.window import WindowRule,WindowIdentity
    from .obj.workspace import WorkspaceIdentity

class Direction(StrEnum):
    """Direction enum"""
    UP = "u"
    DOWN = "d"
    LEFT = "l"
    RIGHT = "r"

@dataclass
class ResizeParam:
    value:str
    exact:bool = False
    
    def pair(self,y:'ResizeParam'):
        return "exact "if self.exact else "" + self.value + " " + y.value

    @staticmethod
    def exact_px(value:int):
        return ResizeParam(f"{value}",exact=True)
    
    @staticmethod
    def exact_percent(value:float):
        return ResizeParam(f"{value}%",exact=True)

    @staticmethod
    def relative_px(value:int):
        return ResizeParam(f"{'+' if value>=0 else '-'}{value}")
    
    @staticmethod
    def relative_percent(value:float):
        return ResizeParam(f"{'+' if value>=0 else '-'}{value}%")

def _dispatch(cmd:'str'):
    """sends a dispatch command"""
    return command_send(f"dispatch {cmd}",check_ok=True)

def dispatch_exec(cmd:'str', rules:'list[WindowRule]'):
    """executes a shell command"""
    return _dispatch(f"exec [{','.join(r.rule for r in rules)}] {cmd}")

def dispatch_execr(cmd:'str'):
    """executes a raw shell command (does not support rules)"""
    return _dispatch(f"execr {cmd}")

def dispatch_pass(window:'WindowIdentity'):
    """passes the key (with mods) to a specified window. Can be used as a workaround to global keybinds not working on Wayland."""
    return _dispatch(f"pass {window.identifier}")

def dispatch_kill_active():
    """closes (not kills) the active window"""
    return _dispatch("killactive")

def dispatch_close_window(window:'WindowIdentity'):
    """closes a specified window"""
    return _dispatch(f"closewindow {window.identifier}")

def dispatch_workspace(w:'WorkspaceIdentity'):
    """changes the workspace"""
    return _dispatch(f"workspace {w.identifier}")

def dispatch_move_to_workspace(w:'WorkspaceIdentity',window:'Optional[WindowIdentity]'=None):
    """moves the focused window (or the specified window) to a workspace"""
    return _dispatch(f"movetoworkspace {w.identifier}{','+window.identifier if window else ''}")

def dispatch_move_to_workspace_silent(w:'WorkspaceIdentity',window:'Optional[WindowIdentity]'=None):
    """moves the focused window (or the specified window) to a workspace without switching to workspace"""
    return _dispatch(f"movetoworkspacesilent {w.identifier}{','+window.identifier if window else ''}")

def dispatch_toggle_floating(window:'Optional[WindowIdentity]'=None):
    """toggles the floating state of a window, if no window is specified, the active window is used."""
    return _dispatch(f"togglefloating{' '+window.identifier if window else ''}")

def dispatch_set_floating(window:'Optional[WindowIdentity]'=None):
    """sets the current window’s floating state to true"""
    return _dispatch(f"setfloating{' '+window.identifier if window else ''}")

def dispatch_set_tiled(window:'Optional[WindowIdentity]'=None):
    """sets the current window’s floating state to false"""
    return _dispatch(f"settiled{' '+window.identifier if window else ''}")

def dispatch_fullscreen(alter_window_state:bool=False):
    """toggles the focused window’s fullscreen state"""
    return _dispatch(f"fullscreen {2 if alter_window_state else 0}")

def dispatch_maximize():
    """toggles the focused window’s fullscreen state to maximize the window. This is different from fullscreen as it does not cover the entire screen."""
    return _dispatch("fullscreen 1")

def dispatch_fake_fullscreen():
    """toggles the focused window’s internal fullscreen state without altering the geometry"""
    return _dispatch("fakefullscreen")

def dispatch_dpms(state:bool,monitor_name:'str'=None):
    """sets the DPMS state of all monitors"""
    return _dispatch(f"dpms {'on' if state else 'off'}{' '+monitor_name if monitor_name else ''}")

def dispatch_toggle_dpms(monitor_name:'str'=None):
    """toggles the DPMS state of all monitors"""
    return _dispatch(f"dpms toggle{' '+monitor_name if monitor_name else ''}")

def dispatch_pin(window:'Optional[WindowIdentity]'=None):
    """pins a window (i.e. show it on all workspaces) note: floating only"""
    return _dispatch(f"pin{' '+window.identifier if window else ''}")

def dispatch_move_focus(direction:'Direction'):
    """moves the focus in the specified direction"""
    return _dispatch(f"movefocus {direction.value}")

def dispatch_move_window(direction:'Direction', monitor:'Optional[str]'=None, silent:bool=False):
    """moves the active window in a direction or to a monitor. For floating windows, moves the window to the screen edge in that direction"""
    return _dispatch(f"movewindow {direction.value}{' mon:'+monitor if monitor else ''}{' silent' if silent else ''}")

def dispatch_swap_window(direction:'Direction'):
    """swaps the active window with another window in the given direction"""
    return _dispatch(f"swapwindow {direction.value}")

def dispatch_center_window(respect_reserved:bool=False):
    """center the active window note: floating only"""
    return _dispatch(f"centerwindow{' 1' if respect_reserved else ''}")

def dispatch_resize_active(x:ResizeParam,y:ResizeParam):
    """resizes the active window"""
    return _dispatch(f"resizeactive {x.pair(y)}")

def dispatch_move_active(x:ResizeParam ,y:ResizeParam):
    """moves the active window"""
    return _dispatch(f"moveactive {x.pair(y)}")

def dispatch_resize_window_pixel(x:ResizeParam, y:ResizeParam, regex:str):
    """resizes a selected window"""    
    return _dispatch(f"resizewindow {x.pair(y)},{regex}")

def dispatch_move_window_pixel(x:ResizeParam, y:ResizeParam, regex:str):
    """moves a selected window"""    
    return _dispatch(f"movewindow {x.pair(y)},{regex}")

def dispatch_cycle_next(prev:bool, tiled_only:bool, floating_only:bool):
    """focuses the next window on a workspace"""
    return _dispatch(f"cyclewindow {'prev' if prev else 'next'}{' tiled' if tiled_only else ''}{' floatingonly' if floating_only else ''}")

def dispatch_swap_next(prev:bool):
    """swaps the focused window with the next window on a workspace"""
    return _dispatch(f"swapwindow {'prev' if prev else 'next'}")

def dispatch_focus_window(window:'WindowIdentity'):
    """focuses the first window matching"""
    return _dispatch(f"focuswindow {window.identifier}")

def dispatch_focus_monitor(monitor_name:'str'):
    """focuses the monitor"""
    return _dispatch(f"focusmonitor {monitor_name}")

def dispatch_split_ratio(ratio:float):
    """changes the split ratio"""
    return _dispatch(f"splitratio {ratio}")

def dispatch_toggle_opaque():
    """toggles the current window to always be opaque. Will override the opaque window rules."""
    return _dispatch("toggleopaque")

def dispatch_cursor_to_top_left():
    """moves the cursor to the top left corner of the screen"""
    return _dispatch("movecursortocorner 3")

def dispatch_cursor_to_top_right():
    """moves the cursor to the top right corner of the screen"""
    return _dispatch("movecursortocorner 2")

def dispatch_cursor_to_bottom_left():
    """moves the cursor to the bottom left corner of the screen"""
    return _dispatch("movecursortocorner 0")

def dispatch_cursor_to_bottom_right():
    """moves the cursor to the bottom right corner of the screen"""
    return _dispatch("movecursortocorner 1")

def dispatch_move_cursor(x:int,y:int):
    """moves the cursor to the specified coordinates"""
    return _dispatch(f"movecursor {x} {y}")

def dispatch_rename_workspace(id:str,name:str):
    """renames a workspace"""
    return _dispatch(f"renameworkspace {id} {name}")

def dispatch_exit():
    """exits the compositor with no questions asked."""
    return _dispatch("exit")

def dispatch_force_render_reload():
    """forces the renderer to reload all resources and outputs"""
    return _dispatch("forcerenderreload")

def dispatch_move_current_workspace_to_monitor(monitor_name:str):
    """moves the current workspace to the specified monitor"""
    return _dispatch(f"movecurrentworkspacetomonitor {monitor_name}")

def dispatch_focus_workspace_on_current_monitor(w:'WorkspaceIdentity'):
    """Focuses the requested workspace on the current monitor, swapping the current workspace to a different monitor if necessary. If you want XMonad/Qtile-style workspace switching, replace workspace in your config with this."""
    return _dispatch(f"focusworkspaceoncurrentmonitor {w.identifier}")

def dispatch_move_workspace_to_monitor(w:'WorkspaceIdentity',monitor_name:str):
    """Moves a workspace to a monitor"""
    return _dispatch(f"moveworkspacetomonitor {w.identifier} {monitor_name}")

def dispatch_swap_active_workspaces(monitor1_name:str, monitor2_name:str):
    """Swaps the active workspaces between two monitors"""
    return _dispatch(f"swapactiveworkspaces {monitor1_name} {monitor2_name}")

def dispatch_alter_z_top(window:'Optional[WindowIdentity]'=None):
    """Modify the window stack order of the active or specified window to be on top. Note: this cannot be used to move a floating window behind a tiled one."""
    return _dispatch(f"alterzorder top{','+window.identifier if window else ''}")

def dispatch_alter_z_bottom(window:'Optional[WindowIdentity]'=None):
    """Modify the window stack order of the active or specified window to be on bottom. Note: this cannot be used to move a floating window behind a tiled one."""
    return _dispatch(f"alterzorder bottom{','+window.identifier if window else ''}")

def dispatch_toggle_special_workspace(name:'Optional[str]'=None):
    """toggles a special workspace on/off"""
    return _dispatch(f"togglespecialworkspace{' '+name if name else ''}")

def dispatch_focus_urgent_or_last():
    """Focuses the urgent window or the last window"""
    return _dispatch("focusurgentorlast")

def dispatch_toggle_group():
    """toggles the current active window into a group"""
    return _dispatch("togglegroup")

def dispatch_change_group_active(prev:'bool', index:'Optional[int]'=None):
    """switches to the next window in a group."""
    if index:
        return _dispatch(f"changegroup {index}")
    return _dispatch(f"changegroup {'b' if prev else 'f'}")

def dispatch_focus_current_or_last():
    """Switch focus from current to previously focused window"""
    return _dispatch("focuscurrentorlast")

def dispatch_lock_groups():
    """Locks the groups (all groups will not accept new windows)"""
    return _dispatch("lockgroups lock")

def dispatch_unlock_groups():
    """Unlocks the groups (all groups will accept new windows)"""
    return _dispatch("lockgroups unlock")

def dispatch_toggle_lock_groups():
    """Toggles the lock state of all groups"""
    return _dispatch("lockgroups toggle")

def dispatch_lock_active_group():
    """Locks the active group (the group will not accept new windows)"""
    return _dispatch("lockactivegroup lock")

def dispatch_unlock_active_group():
    """Unlocks the active group (the group will accept new windows)"""
    return _dispatch("lockactivegroup unlock")

def dispatch_toggle_lock_active_group():
    """Toggles the lock state of the active group"""
    return _dispatch("lockactivegroup toggle")

def dispatch_move_into_group(direction:'Direction'):
    """Moves the active window into a group in a specified direction. No-op if there is no group in the specified direction."""
    return _dispatch(f"moveintogroup {direction.value}")

def dispatch_move_out_of_group(window:'Optional[WindowIdentity]'=None):
    """Moves the active window out of a group. No-op if not in a group"""
    return _dispatch(f"moveoutofgroup{' '+window.identifier if window else ''}")

def dispatch_move_window_or_group(direction:'Direction'):
    """Behaves as moveintogroup if there is a group in the given direction. Behaves as moveoutofgroup if there is no group in the given direction relative to the active group. Otherwise behaves like movewindow."""
    return _dispatch(f"movewindoworgroup {direction.value}")

def dispatch_move_group_window(back:'bool'):
    """Swaps the active window with the next or previous in a group"""
    return _dispatch(f"movegroupwindow {'b' if back else 'nevergonnagiveyouup'}")

def dispatch_deny_window_from_group():
    """Prohibit the active window from becoming or being inserted into group"""
    return _dispatch("denywindowfromgroup on")

def dispatch_allow_window_into_group():
    """Allow the active window to become or be inserted into group"""
    return _dispatch("denywindowintogroup off")

def dispatch_toggle_deny_window_into_group():
    """Toggle the deny state of the active window from becoming or being inserted into group"""
    return _dispatch("denywindowintogroup toggle")

def dispatch_enable_ignore_group_lock():
    """Temporarily disable binds:ignore_group_lock"""
    return _dispatch("setignoregrouplock on")

def dispatch_disable_ignore_group_lock():
    """enables binds:ignore_group_lock"""
    return _dispatch("setignoregrouplock off")

def dispatch_toggle_ignore_group_lock():
    """toggles binds:ignore_group_lock"""
    return _dispatch("setignoregrouplock toggle")

def dispatch_global(name:str):
    """Executes a Global Shortcut using the GlobalShortcuts portal"""
    return _dispatch(f"global {name}")

def dispatch_submap(name:str):
    """Change the current mapping group. See """
    return _dispatch(f"submap {name}")

def dispatch_submap_reset():
    """Reset the current mapping group"""
    return _dispatch("submap reset")

