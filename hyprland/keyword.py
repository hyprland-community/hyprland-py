from __future__ import annotations

from dataclasses import dataclass

import msgspec.json as json
from msgspec import Struct, field

from .socket import Command, query


class Option(Struct):
   option: str
   integer: int = field(name="int")
   floating: float = field(name="float")
   string: str = field(name="str")
   data: str


def get_option(path: str):
   return json.decode(query(f"getoption {path}".encode()), type=Option)


@dataclass
class SetOption(Command):
   path: str
   value: str

   def to_command(self):
      return f"keyword {self.path} {self.value}".encode()


@dataclass
class KeywordBool:
   path: str

   def get(self):
      return get_option(self.path).integer != 0

   def set(self, value: bool):
      return SetOption(self.path, "1" if value else "0")


@dataclass
class KeywordInt:
   path: str

   def get(self):
      return get_option(self.path).integer

   def set(self, value: int):
      return SetOption(self.path, str(value))


@dataclass
class KeywordFloat:
   path: str

   def get(self):
      return get_option(self.path).floating

   def set(self, value: float):
      return SetOption(self.path, str(value))


@dataclass
class KeywordVec2:
   path: str

   def get(self):
      return get_option(self.path)

   def set(self, x: float, y: float):
      return SetOption(self.path, f"{x} {y}")


@dataclass
class KeywordColor:
   path: str

   def get(self):
      return get_option(self.path)

   def set(self, color: str):
      return SetOption(self.path, color)


@dataclass
class KeywordStr:
   path: str

   def get(self):
      return get_option(self.path).string

   def set(self, value: str):
      return SetOption(self.path, value)


@dataclass
class KeywordGradient:
   path: str

   def get(self):
      return get_option(self.path)

   def set(self, colors: list[str], angle: int = 0):
      return SetOption(self.path, " ".join(colors) + f" {angle}deg")
