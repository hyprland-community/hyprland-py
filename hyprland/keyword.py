from __future__ import annotations

from dataclasses import dataclass

import msgspec.json as json
from msgspec import Struct, field

from .socket import execute, query


class Option(Struct):
   option: str
   integer: int = field(name="int")
   floating: float = field(name="float")
   string: str = field(name="str")
   data: str


def get_option(path: str):
   return json.decode(query(f"getoption {path}".encode()), type=Option)


def set_option(path: str, value: str):
   execute(f"keyword {path} {value}".encode())


@dataclass
class KeywordBool:
   path: str

   def get(self):
      return get_option(self.path).integer != 0

   def set(self, value: bool):
      set_option(self.path, "1" if value else "0")
      return self


@dataclass
class KeywordInt:
   path: str

   def get(self):
      return get_option(self.path).integer

   def set(self, value: int):
      set_option(self.path, str(value))
      return self


@dataclass
class KeywordFloat:
   path: str

   def get(self):
      return get_option(self.path).floating

   def set(self, value: float):
      set_option(self.path, str(value))
      return self


@dataclass
class KeywordVec2:
   path: str

   def get(self):
      return get_option(self.path)

   def set(self, x: float, y: float):
      set_option(self.path, f"{x} {y}")
      return self


@dataclass
class KeywordColor:
   path: str

   def get(self):
      return get_option(self.path)

   def set(self, color: str):
      set_option(self.path, color)
      return self


@dataclass
class KeywordStr:
   path: str

   def get(self):
      return get_option(self.path).string

   def set(self, value: str):
      set_option(self.path, value)
      return self


@dataclass
class KeywordGradient:
   path: str

   def get(self):
      return get_option(self.path)

   def set(self, colors: list[str], angle: int = 0):
      set_option(self.path, " ".join(colors) + f" {angle}deg")
      return self
