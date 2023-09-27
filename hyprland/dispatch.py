from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from .socket import execute


class CommandEnum(StrEnum):
   def to_command(self):
      return self.value.encode()


class Direction(CommandEnum):
   LEFT = "l"
   RIGHT = "r"
   UP = "u"
   DOWN = "d"


class Corner(CommandEnum):
   BOTTOM_LEFT = "0"
   BOTTOM_RIGHT = "1"
   TOP_RIGHT = "2"
   TOP_LEFT = "3"


class ZHeight(CommandEnum):
   TOP = "top"
   BOTTOM = "bottom"


@dataclass
class WindowAddress:
   """Address of window."""

   _: str

   def to_command(self):
      return b"address:" + self._.encode()


@dataclass
class WindowClassPattern:
   """Regex pattern to match against the window class. Handled by Hyprland."""

   _: str

   def to_command(self):
      return self._.encode()


@dataclass
class WindowTitlePattern:
   """Regex pattern to match against the window title. Handled by Hyprland."""

   _: str

   def to_command(self):
      return b"title:" + self._.encode()


@dataclass
class WindowPID:
   """Process ID of window."""

   _: int

   def to_command(self):
      return b"pid:" + str(self._).encode()


WindowIdentifier = WindowAddress | WindowClassPattern | WindowPID


@dataclass
class WorkspaceID:
   """ID of workspace."""

   _: int

   def to_command(self):
      return str(self._).encode()


@dataclass
class WorkspaceRelative:
   """Relative offset to current workspace. Offset should not be 0."""

   _: int

   def to_command(self):
      if 0 < self._:
         return b"+" + str(self._).encode()
      elif self._ < 0:
         return b"-" + str(self._).encode()
      raise ValueError("workspace offset is 0.", self._)


@dataclass
class WorkspaceOnMonitorRelative:
   """Relative offset to current workspace on monitor. Offset should not be 0."""

   _: int

   def to_command(self):
      if 0 < self._:
         return b"m+" + str(self._).encode()
      elif self._ < 0:
         return b"m-" + str(self._).encode()
      raise ValueError("workspace offset is 0.", self._)


@dataclass
class WorkspaceOnMonitorRelativeIncludingEmpty:
   """Relative offset to current workspace on monitor including empty workspaces. Offset should not be 0."""

   _: int

   def to_command(self):
      if 0 < self._:
         return b"r+" + str(self._).encode()
      elif self._ < 0:
         return b"r-" + str(self._).encode()
      raise ValueError("workspace offset is 0.", self._)


@dataclass
class WorkspaceOpenRelative:
   """Relative offset to current workspace for open workspaces. Offset should not be 0."""

   _: int

   def to_command(self):
      if 0 < self._:
         return b"e+" + str(self._).encode()
      elif self._ < 0:
         return b"e-" + str(self._).encode()
      raise ValueError("workspace offset is 0.", self._)


@dataclass
class WorkspacePrevious:
   def to_command(self):
      return b"previous"


@dataclass
class WorkspaceFirstEmptyAvailable:
   def to_command(self):
      return b"empty"


@dataclass
class WorkspaceSpecial:
   _: str | None = None

   def to_command(self):
      if self._:
         return b"special:" + self._.encode()
      else:
         return b"special"


# `WorkspaceSpecial` is not included here, as it is only supported on the `MoveToWorkspace` dispatcher.
WorkspaceIdentifier = (
   WorkspaceID
   | WorkspaceRelative
   | WorkspaceOnMonitorRelative
   | WorkspaceOnMonitorRelativeIncludingEmpty
   | WorkspaceOpenRelative
   | WorkspacePrevious
   | WorkspaceFirstEmptyAvailable
)


@dataclass
class MonitorID:
   """Monitor ID or Name."""

   _: str

   def to_command(self):
      return self._.encode()


@dataclass
class MonitorCurrent:
   def to_command(self):
      return b"current"


@dataclass
class MonitorRelative:
   """Relative offset to current monitor. Offset should not be 0."""

   _: int

   def to_command(self):
      if 0 < self._:
         return b"+" + str(self._).encode()
      elif self._ < 0:
         return b"-" + str(self._).encode()
      raise ValueError("workspace offset is 0.", self._)


MonitorIdentifier = MonitorID | MonitorCurrent | MonitorRelative | Direction


@dataclass
class ResizeParams:
   x: Px | Percent
   y: Px | Percent
   exact: bool = False

   def __init__(self, x: int | Percent, y: int | Percent, exact: bool = False):
      if not isinstance(x, Percent):
         x = Px(x)
      if not isinstance(y, Percent):
         y = Px(y)
      self.x = x
      self.y = y
      self.exact = exact

   def to_command(self):
      return (b"exact" if self.exact else b"") + self.x.to_command() + b" " + self.y.to_command()


class Px(int):
   def to_command(self):
      return str(self).encode()


class Percent(int):
   def to_command(self):
      return str(self).encode() + b"%"


@dataclass
class Dispatcher:
   def to_command(self) -> tuple[bytes, ...]:
      raise NotImplementedError

   def dispatch(self):
      execute(b"dispatch " + b" ".join(self.to_command()))


@dataclass
class Exec(Dispatcher):
   """Executes a shell command. Hyprland appends additional envvars."""

   # FIXME: Support type-safe rules.
   command: str

   def to_command(self):
      return b"exec", self.command.encode()


@dataclass
class Execr(Dispatcher):
   """Executes a shell command without appending any additional envvars or support for rules."""

   command: str

   def to_command(self):
      return b"execr", self.command.encode()


@dataclass
class Pass(Dispatcher):
   """Passes the key (with mods) to a specified window. Can be used as a workaround to global keybinds not working on Wayland."""

   window: WindowIdentifier

   def to_command(self):
      return b"pass", self.window.to_command()


@dataclass
class KillActive(Dispatcher):
   """Closes the active window (Not kill)."""

   def to_command(self):
      return (b"killactive",)


@dataclass
class CloseWindow(Dispatcher):
   """Closes the specified window."""

   window: WindowIdentifier

   def to_command(self):
      return b"closewindow", self.window.to_command()


@dataclass
class Workspace(Dispatcher):
   """Switch to the specified workspace."""

   workspace: WorkspaceIdentifier

   def to_command(self):
      return b"workspace", self.workspace.to_command()


@dataclass
class MoveToWorkspace(Dispatcher):
   """Move the active window to specified workspace. `silent` doesn't switch to the workspace."""

   workspace: WorkspaceIdentifier | WorkspaceSpecial
   silent: bool = False
   """Don't switch to workspace."""

   def to_command(self):
      return b"movetoworkspace" if self.silent else b"movetoworkspacesilent", self.workspace.to_command()


@dataclass
class ToggleFloating(Dispatcher):
   """Toggles the window's floating state. If `window` is not given, the active window will be selected."""

   window: WindowIdentifier | None = None

   def to_command(self):
      if self.window:
         return b"togglefloating", self.window.to_command()
      return (b"togglefloating",)


@dataclass
class Fullscreen(Dispatcher):
   """Toggles the active window's fullscreen state. Use `FullscreenMaximize` to keep gaps and bar(s)."""

   def to_command(self):
      return b"fullscreen", b"0"


@dataclass
class FullscreenMaximize(Dispatcher):
   """Toggles the active window's fullscreen state while keeping gaps and bar(s) visible."""

   def to_command(self):
      return b"fullscreen", b"1"


@dataclass
class FakeFullscreen(Dispatcher):
   """Toggles the active window's internal fullscreen state without altering the geometry."""

   def to_command(self):
      return (b"fakefullscreen",)


@dataclass
class Dpms(Dispatcher):
   """Set all monitor's DPMS status. Do not use with a keybind directly. Use `DpmsToggle` to toggle."""

   to: bool

   def to_command(self):
      return b"dpms", b"on" if self.to else b"off"


@dataclass
class DpmsToggle(Dispatcher):
   """Toggle all monitor's DPMS status. Do not use with a keybind directly."""

   def to_command(self):
      return b"dpms", b"toggle"


@dataclass
class Pin(Dispatcher):
   """Pin the window (Visible on all workspaces). The window must be a floating window. If `window` is not given, the active window will be selected."""

   window: WindowIdentifier | None = None

   def to_command(self):
      if self.window:
         return b"pin", self.window.to_command()
      return (b"pin",)


@dataclass
class MoveWindowToMontior(Dispatcher):
   """Move the active window to specified monitor."""

   monitor: MonitorIdentifier

   def to_command(self):
      return b"movewindow", self.monitor.to_command()


@dataclass
class SwapWindow(Dispatcher):
   """Swaps the active window with the window in given direction."""

   direction: Direction

   def to_command(self):
      return b"swapwindow", self.direction.to_command()


@dataclass
class CenterWindow(Dispatcher):
   """Centers the active window. The window must be a floating window."""

   respect_monitor_reserved_area: bool = False

   def to_command(self):
      return (b"centerwindow", b"1") if self.respect_monitor_reserved_area else (b"centerwindow",)


@dataclass
class ResizeWindow(Dispatcher):
   """Resize the window. If window is not given, the active window is selected."""

   resizeparams: ResizeParams
   window: WindowIdentifier | None = None

   def to_command(self):
      if self.window:
         return b"resizewindowpixel", self.resizeparams.to_command(), self.window.to_command()
      return b"resizeactive", self.resizeparams.to_command()


@dataclass
class MoveWindow(Dispatcher):
   """Moves the window. If window is not given, the active window is selected."""

   resizeparams: ResizeParams
   window: WindowIdentifier | None = None

   def to_command(self):
      if self.window:
         return b"movewindowpixel", self.resizeparams.to_command(), self.window.to_command()
      return b"moveactive", self.resizeparams.to_command()


@dataclass
class CycleNext(Dispatcher):
   """Focuses the next window in a workspace. Also see `CyclePrevious`."""

   def to_command(self):
      return (b"cyclenext",)


@dataclass
class CyclePrevious(Dispatcher):
   """Focuses the next window in a workspace. Also see `CycleNext`."""

   def to_command(self):
      return b"cyclenext", b"prev"


@dataclass
class SwapNext(Dispatcher):
   """Swaps the active window with the next window in a workspace. Also see `SwapPrevious`."""

   def to_command(self):
      return (b"swapnext",)


@dataclass
class SwapPrevious(Dispatcher):
   """Swaps the active window with the next window in a workspace. Also see `SwapNext`."""

   def to_command(self):
      return b"swapnext", b"prev"


@dataclass
class FocusWindow(Dispatcher):
   """Focuses the first window matching identifier."""

   window: WindowIdentifier

   def to_command(self):
      return b"focuswindow", self.window.to_command()


@dataclass
class FocusMonitor(Dispatcher):
   """Focuses the given monitor."""

   monitor: MonitorIdentifier

   def to_command(self):
      return b"focusmonitor", self.monitor.to_command()


@dataclass
class SplitRatio(Dispatcher):
   """Sets the split ratio."""

   ratio: float

   def to_command(self):
      return b"splitratio", str(self.ratio).encode()


@dataclass
class ToggleOpaque(Dispatcher):
   """Toggles the active window's opaque state. Will override the opaque window rules."""

   def to_command(self):
      return (b"toggleopaque",)


@dataclass
class MoveCursorToCorner(Dispatcher):
   """Move the cursor to the corner of the active window."""

   corner: Corner

   def to_command(self):
      return b"movecursortocorner", self.corner.to_command()


@dataclass
class MoveCursor(Dispatcher):
   """Move the cursor to the given position."""

   x: int
   y: int

   def to_command(self):
      return b"movecursor", str(self.x).encode() + b"," + str(self.y).encode()


@dataclass
class RenameWorkspace(Dispatcher):
   """Renames a workspace."""

   id: int
   name: str

   def to_command(self):
      return b"renameworkspace", str(self.id).encode(), self.name.encode()


@dataclass
class Exit(Dispatcher):
   """Exit Hyprland."""

   def to_command(self):
      return (b"exit",)


@dataclass
class ForceRendererReload(Dispatcher):
   """Forces the renderer to reload all resources and outputs."""

   def to_command(self):
      return (b"forcerendererreload",)


@dataclass
class MoveWorkspaceToMonitor(Dispatcher):
   """Moves the workspace to a monitor. If workspace is not given, the current workspace is selected."""

   monitor: MonitorIdentifier
   workspace: WorkspaceIdentifier | None = None

   def to_command(self):
      if self.workspace:
         return b"moveworkspacetomonitor", self.workspace.to_command(), self.monitor.to_command()
      return b"movecurrentworkspacetomonitor", self.monitor.to_command()


@dataclass
class SwapActiveWorkspaces(Dispatcher):
   """Swaps the active workspaces between two monitors."""

   monitor1: MonitorIdentifier
   monitor2: MonitorIdentifier

   def to_command(self):
      return b"swapactiveworkspaces", self.monitor1.to_command(), self.monitor2.to_command()


@dataclass
class WorkspaceOptAllFloat(Dispatcher):
   """Make all new windows floating (also floats/unfloats windows on toggle)."""

   def to_command(self):
      return b"workspaceopt", b"allfloat"


@dataclass
class WorkspaceOptAllPseudo(Dispatcher):
   """Make all new windows pseudo (also pseudos/unpseudos windows on toggle)."""

   def to_command(self):
      return b"workspaceopt", b"allpseudo"


@dataclass
class AlterZOrder(Dispatcher):
   """
   Modify the window stack order of the active or specified window.
   Note: this cannot be used to move a floating window behind a tiled one.
   """

   zheight: ZHeight
   window: WindowIdentifier | None = None

   def to_command(self):
      if self.window:
         return b"alterzheight", self.zheight.to_command(), self.window.to_command()
      return b"alterzheight", self.zheight.to_command()
