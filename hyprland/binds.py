from __future__ import annotations

from dataclasses import dataclass
from itertools import chain
from typing import Callable, overload

from .dispatch import Dispatcher, Exec
from .socket import execute


class Key(str):
   """See <https://wiki.hyprland.org/Configuring/Binds/#uncommon-syms--binding-with-a-keycode>"""

   ...


class Mod(str):
   @overload
   def __add__(self, other: Key) -> Keybind:
      ...

   @overload
   def __add__(self, other: Mod) -> KeybindBuilder:
      ...

   def __add__(self, other: Key | Mod) -> Keybind | KeybindBuilder:  # type: ignore
      return KeybindBuilder([self]) + other


EMPTY = Mod("")
"For keybindings without any modifiers. Useful in submaps."
SUPER = Mod("SUPER")
"The Windows key."
SHIFT = Mod("SHIFT")
ALT = Mod("ALT")
CTRL = Mod("CTRL")


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
   return keybind.submap


@submap(SUPER + Key("E"))
def exec_submap():
   (EMPTY + Key("F")).repeat().bind(Exec("firefox"))
