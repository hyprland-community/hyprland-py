from __future__ import annotations

from dataclasses import dataclass
from itertools import chain
from typing import Callable, overload

from .dispatch import Dispatcher
from .socket import execute
from .info import Bind
from enum import StrEnum


# fmt: off
# <https://github.com/swaywm/wlroots/blob/0855cdacb2eeeff35849e2e9c4db0aa996d78d10/include/wlr/types/wlr_keyboard.h#L28>
WLR_MODIFIER_SHIFT = 1 << 0
WLR_MODIFIER_CAPS  = 1 << 1
WLR_MODIFIER_CTRL  = 1 << 2
WLR_MODIFIER_ALT   = 1 << 3
WLR_MODIFIER_MOD2  = 1 << 4
WLR_MODIFIER_MOD3  = 1 << 5
WLR_MODIFIER_LOGO  = 1 << 6
WLR_MODIFIER_MOD5  = 1 << 7
# fmt: on


class Key(str):
   """See <https://wiki.hyprland.org/Configuring/Binds/#uncommon-syms--binding-with-a-keycode>"""

   ...


class Mod(StrEnum):
   EMPTY = ""
   "For keybindings without any modifiers. Useful in submaps."
   SUPER = "SUPER"
   SHIFT = "SHIFT"
   CAPS = "CAPS"
   CTRL = "CTRL"
   ALT = "ALT"
   MOD2 = "MOD2"
   MOD3 = "MOD3"
   LOGO = "LOGO"
   "Treated the same as `Mod.SUPER`"
   WIN = "WIN"
   "Treated the same as `Mod.SUPER`"
   MOD4 = "MOD4"
   "Treated the same as `Mod.SUPER`"
   MOD5 = "MOD5"

   # <https://github.com/hyprwm/Hyprland/blob/ffacd2efd1ca7fdf364a519c9d8d8644da28412b/src/managers/KeybindManager.cpp#L115>
   @classmethod
   def from_modmask(cls, modmask: int):
      mods: list[Mod] = []
      if modmask & WLR_MODIFIER_SHIFT:
         mods.append(Mod.SHIFT)
      if modmask & WLR_MODIFIER_CAPS:
         mods.append(Mod.CAPS)
      if modmask & WLR_MODIFIER_CTRL:
         mods.append(Mod.CTRL)
      if modmask & WLR_MODIFIER_ALT:
         mods.append(Mod.ALT)
      if modmask & WLR_MODIFIER_MOD2:
         mods.append(Mod.MOD2)
      if modmask & WLR_MODIFIER_MOD3:
         mods.append(Mod.MOD3)
      if modmask & WLR_MODIFIER_LOGO:
         mods.append(Mod.SUPER)
      if modmask & WLR_MODIFIER_MOD5:
         mods.append(Mod.MOD5)
      return mods

   @overload
   def __add__(self, other: Key) -> Keybind:
      ...

   @overload
   def __add__(self, other: Mod) -> KeybindBuilder:
      ...

   def __add__(self, other: Key | Mod) -> Keybind | KeybindBuilder:  # type: ignore
      return KeybindBuilder([self]) + other


@dataclass
class Keybind:
   mods: list[Mod]
   key: Key
   _locked: bool = False
   _release: bool = False
   _repeat: bool = False
   _non_consuming: bool = False
   _mouse: bool = False  # FIXME: Implement mouse dispatchers.
   _transparent: bool = False

   @classmethod
   def from_bind(cls, bind: Bind):
      """Convert a `info.Bind` returned by `info.binds()` into a `Keybind`. Discards dispatcher information."""
      return cls(
         mods=Mod.from_modmask(bind.modmask),
         key=Key(bind.key),
         _locked=bind.locked,
         _release=bind.release,
         _repeat=bind.repeat,
         _non_consuming=bind.non_consuming,
         _mouse=bind.mouse,
      )

   def _flags(self):
      f = b""
      if self._locked:
         f += b"l"
      if self._release:
         f += b"r"
      if self._repeat:
         f += b"e"
      if self._non_consuming:
         f += b"n"
      if self._mouse:
         f += b"m"
      if self._transparent:
         f += b"t"
      return f

   def _bindstr(self, dispatcher: Dispatcher | None = None):
      return b",".join(
         chain(
            (b" ".join(i.encode() for i in self.mods),),
            (self.key.encode(),),
            dispatcher.to_command() if dispatcher else (),
         )
      )

   def locked(self):
      """locked, aka. works also when an input inhibitor (e.g. a lockscreen) is active."""
      self._locked = True
      return self

   def release(self):
      """release, will trigger on release of a key."""
      self._release = True
      return self

   def repeat(self):
      """repeat, will repeat when held."""
      self._repeat = True
      return self

   def non_consuming(self):
      """non-consuming, key/mouse events will be passed to the active window in addition to triggering the dispatcher."""
      self._non_consuming = True
      return self

   def mouse(self):
      """See <https://wiki.hyprland.org/Configuring/Binds/#mouse-binds>"""
      self._mouse = True
      return self

   def transparent(self):
      """transparent, cannot be shadowed by other binds."""
      self._transparent = True
      return self

   def bind(
      self,
      dispatcher: Dispatcher,
   ):
      execute(b"keyword bind" + self._flags() + b" " + self._bindstr(dispatcher))
      return self

   def unbind(self):
      execute(b"keyword unbind " + self._bindstr())
      return self

   def submap(self, func: Callable[[], None]):
      execute(b"keyword bind " + self._bindstr() + b",submap," + func.__name__.encode())
      execute(b"keyword submap " + func.__name__.encode())
      func()
      execute(b"keyword submap reset")
      return self


class KeybindBuilder:
   def __init__(self, mods: list[Mod]):
      self._mods = mods

   @overload
   def __add__(self, other: Key) -> Keybind:
      ...

   @overload
   def __add__(self, other: Mod) -> KeybindBuilder:
      ...

   def __add__(self, other: Mod | Key):
      if isinstance(other, Mod):
         return KeybindBuilder([*self._mods, other])
      else:
         return Keybind(self._mods, other)


def submap(keybind: Keybind):
   """
   Submap decorator. Apply on a function to create a submap, will be executed on application.

   Usage:
   >>> @submap(Mod.SUPER + Key('R'))
   >>> def my_submap():
   >>>    (Mod.EMPTY + Key('F')).bind(Exec('firefox'))
   """
   return keybind.submap
