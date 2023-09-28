**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# dispatch


 - [Dispatcher](#Dispatcher)

 - [CommandEnum](#CommandEnum)

 - [Direction](#Direction)

 - [Corner](#Corner)

 - [ZHeight](#ZHeight)

 - [WindowAddress](#WindowAddress)

 - [WindowClassPattern](#WindowClassPattern)

 - [WindowTitlePattern](#WindowTitlePattern)

 - [WindowPID](#WindowPID)

 - [WorkspaceID](#WorkspaceID)

 - [WorkspaceRelative](#WorkspaceRelative)

 - [WorkspaceOnMonitorRelative](#WorkspaceOnMonitorRelative)

 - [WorkspaceOnMonitorRelativeIncludingEmpty](#WorkspaceOnMonitorRelativeIncludingEmpty)

 - [WorkspaceOpenRelative](#WorkspaceOpenRelative)

 - [WorkspacePrevious](#WorkspacePrevious)

 - [WorkspaceFirstEmptyAvailable](#WorkspaceFirstEmptyAvailable)

 - [WorkspaceSpecial](#WorkspaceSpecial)

 - [MonitorID](#MonitorID)

 - [MonitorCurrent](#MonitorCurrent)

 - [MonitorRelative](#MonitorRelative)

 - [ResizeParams](#ResizeParams)

 - [Px](#Px)

 - [Percent](#Percent)

 - [Exec](#Exec)

 - [Execr](#Execr)

 - [Pass](#Pass)

 - [KillActive](#KillActive)

 - [CloseWindow](#CloseWindow)

 - [SwitchWorkspace](#SwitchWorkspace)

 - [MoveToWorkspace](#MoveToWorkspace)

 - [ToggleFloating](#ToggleFloating)

 - [Fullscreen](#Fullscreen)

 - [FullscreenMaximize](#FullscreenMaximize)

 - [FakeFullscreen](#FakeFullscreen)

 - [Dpms](#Dpms)

 - [DpmsToggle](#DpmsToggle)

 - [Pin](#Pin)

 - [MoveWindowToMontior](#MoveWindowToMontior)

 - [SwapWindow](#SwapWindow)

 - [CenterWindow](#CenterWindow)

 - [ResizeWindow](#ResizeWindow)

 - [MoveWindow](#MoveWindow)

 - [CycleNext](#CycleNext)

 - [CyclePrevious](#CyclePrevious)

 - [SwapNext](#SwapNext)

 - [SwapPrevious](#SwapPrevious)

 - [FocusWindow](#FocusWindow)

 - [FocusMonitor](#FocusMonitor)

 - [SplitRatio](#SplitRatio)

 - [ToggleOpaque](#ToggleOpaque)

 - [MoveCursorToCorner](#MoveCursorToCorner)

 - [MoveCursor](#MoveCursor)

 - [RenameWorkspace](#RenameWorkspace)

 - [Exit](#Exit)

 - [ForceRendererReload](#ForceRendererReload)

 - [MoveWorkspaceToMonitor](#MoveWorkspaceToMonitor)

 - [SwapActiveWorkspaces](#SwapActiveWorkspaces)

 - [WorkspaceOptAllFloat](#WorkspaceOptAllFloat)

 - [WorkspaceOptAllPseudo](#WorkspaceOptAllPseudo)

 - [AlterZOrder](#AlterZOrder)



# `Dispatcher`


```py

class Dispatcher:
    ...
```

## `to_command_args`


```py

def to_command_args(self) -> tuple[bytes, ...]:
    ...
```

## `to_command`


```py

def to_command(self):
    ...
```

# `CommandEnum`


```py

class CommandEnum:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Direction`


```py

class Direction:
    ...
```

# `Corner`


```py

class Corner:
    ...
```

# `ZHeight`


```py

class ZHeight:
    ...
```

# `WindowAddress`


```py

class WindowAddress:
    ...
```

Address of window.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WindowClassPattern`


```py

class WindowClassPattern:
    ...
```

Regex pattern to match against the window class. Handled by Hyprland.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WindowTitlePattern`


```py

class WindowTitlePattern:
    ...
```

Regex pattern to match against the window title. Handled by Hyprland.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WindowPID`


```py

class WindowPID:
    ...
```

Process ID of window.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceID`


```py

class WorkspaceID:
    ...
```

ID of workspace.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceRelative`


```py

class WorkspaceRelative:
    ...
```

Relative offset to current workspace. Offset should not be 0.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceOnMonitorRelative`


```py

class WorkspaceOnMonitorRelative:
    ...
```

Relative offset to current workspace on monitor. Offset should not be 0.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceOnMonitorRelativeIncludingEmpty`


```py

class WorkspaceOnMonitorRelativeIncludingEmpty:
    ...
```

Relative offset to current workspace on monitor including empty workspaces. Offset should not be 0.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceOpenRelative`


```py

class WorkspaceOpenRelative:
    ...
```

Relative offset to current workspace for open workspaces. Offset should not be 0.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspacePrevious`


```py

class WorkspacePrevious:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceFirstEmptyAvailable`


```py

class WorkspaceFirstEmptyAvailable:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceSpecial`


```py

class WorkspaceSpecial:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MonitorID`


```py

class MonitorID:
    ...
```

Monitor ID or Name.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MonitorCurrent`


```py

class MonitorCurrent:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MonitorRelative`


```py

class MonitorRelative:
    ...
```

Relative offset to current monitor. Offset should not be 0.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `ResizeParams`


```py

class ResizeParams:
    ...
```

## `__init__`


```py

def __init__(self, x: int | Percent, y: int | Percent, exact: bool):
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Px`


```py

class Px:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Percent`


```py

class Percent:
    ...
```

## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Exec`


```py

class Exec:
    ...
```

Executes a shell command. Hyprland appends additional envvars.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Execr`


```py

class Execr:
    ...
```

Executes a shell command without appending any additional envvars or support for rules.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Pass`


```py

class Pass:
    ...
```

Passes the key (with mods) to a specified window. Can be used as a workaround to global keybinds not working on Wayland.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `KillActive`


```py

class KillActive:
    ...
```

Closes the active window (Not kill).





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `CloseWindow`


```py

class CloseWindow:
    ...
```

Closes the specified window.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `SwitchWorkspace`


```py

class SwitchWorkspace:
    ...
```

Switch to the specified workspace.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MoveToWorkspace`


```py

class MoveToWorkspace:
    ...
```

Move the active window to specified workspace. `silent` doesn't switch to the workspace.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `ToggleFloating`


```py

class ToggleFloating:
    ...
```

Toggles the window's floating state. If `window` is not given, the active window will be selected.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Fullscreen`


```py

class Fullscreen:
    ...
```

Toggles the active window's fullscreen state. Use `FullscreenMaximize` to keep gaps and bar(s).





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `FullscreenMaximize`


```py

class FullscreenMaximize:
    ...
```

Toggles the active window's fullscreen state while keeping gaps and bar(s) visible.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `FakeFullscreen`


```py

class FakeFullscreen:
    ...
```

Toggles the active window's internal fullscreen state without altering the geometry.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Dpms`


```py

class Dpms:
    ...
```

Set all monitor's DPMS status. Do not use with a keybind directly. Use `DpmsToggle` to toggle.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `DpmsToggle`


```py

class DpmsToggle:
    ...
```

Toggle all monitor's DPMS status. Do not use with a keybind directly.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Pin`


```py

class Pin:
    ...
```

Pin the window (Visible on all workspaces). The window must be a floating window. If `window` is not given, the active window will be selected.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MoveWindowToMontior`


```py

class MoveWindowToMontior:
    ...
```

Move the active window to specified monitor.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `SwapWindow`


```py

class SwapWindow:
    ...
```

Swaps the active window with the window in given direction.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `CenterWindow`


```py

class CenterWindow:
    ...
```

Centers the active window. The window must be a floating window.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `ResizeWindow`


```py

class ResizeWindow:
    ...
```

Resize the window. If window is not given, the active window is selected.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MoveWindow`


```py

class MoveWindow:
    ...
```

Moves the window. If window is not given, the active window is selected.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `CycleNext`


```py

class CycleNext:
    ...
```

Focuses the next window in a workspace. Also see `CyclePrevious`.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `CyclePrevious`


```py

class CyclePrevious:
    ...
```

Focuses the next window in a workspace. Also see `CycleNext`.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `SwapNext`


```py

class SwapNext:
    ...
```

Swaps the active window with the next window in a workspace. Also see `SwapPrevious`.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `SwapPrevious`


```py

class SwapPrevious:
    ...
```

Swaps the active window with the next window in a workspace. Also see `SwapNext`.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `FocusWindow`


```py

class FocusWindow:
    ...
```

Focuses the first window matching identifier.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `FocusMonitor`


```py

class FocusMonitor:
    ...
```

Focuses the given monitor.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `SplitRatio`


```py

class SplitRatio:
    ...
```

Sets the split ratio.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `ToggleOpaque`


```py

class ToggleOpaque:
    ...
```

Toggles the active window's opaque state. Will override the opaque window rules.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MoveCursorToCorner`


```py

class MoveCursorToCorner:
    ...
```

Move the cursor to the corner of the active window.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MoveCursor`


```py

class MoveCursor:
    ...
```

Move the cursor to the given position.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `RenameWorkspace`


```py

class RenameWorkspace:
    ...
```

Renames a workspace.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `Exit`


```py

class Exit:
    ...
```

Exit Hyprland.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `ForceRendererReload`


```py

class ForceRendererReload:
    ...
```

Forces the renderer to reload all resources and outputs.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `MoveWorkspaceToMonitor`


```py

class MoveWorkspaceToMonitor:
    ...
```

Moves the workspace to a monitor. If workspace is not given, the current workspace is selected.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `SwapActiveWorkspaces`


```py

class SwapActiveWorkspaces:
    ...
```

Swaps the active workspaces between two monitors.





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceOptAllFloat`


```py

class WorkspaceOptAllFloat:
    ...
```

Make all new windows floating (also floats/unfloats windows on toggle).





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `WorkspaceOptAllPseudo`


```py

class WorkspaceOptAllPseudo:
    ...
```

Make all new windows pseudo (also pseudos/unpseudos windows on toggle).





## `to_command_args`


```py

def to_command_args(self):
    ...
```

# `AlterZOrder`


```py

class AlterZOrder:
    ...
```

Modify the window stack order of the active or specified window.



Note: this cannot be used to move a floating window behind a tiled one.


## `to_command_args`


```py

def to_command_args(self):
    ...
```

