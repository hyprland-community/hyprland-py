from __future__ import annotations

from typing import Any

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


def set_option(path: str, value: int | float | str):
   execute(f"keyword {path} {value!r}".encode())


class Config:
   __slots__ = "_path", "_type"

   def __init__(self, path: str = "", type: str | None = None):
      self._path = path
      self._type = type

   def __getattr__(self, __name: str):
      type = self.__annotations__.get(__name)
      path = __name if self._path == "" else self._path + ":" + __name
      return Config(path, type=type)

   def set(self, value: Any):
      set_option(self._path, value)

   def get(self) -> Any:
      if self._type == "ConfigInt":
         return get_option(self._path).integer
      elif self._type == "ConfigFloat":
         return get_option(self._path).floating
      elif self._type == "ConfigStr":
         return get_option(self._path).string
      elif self._type == "ConfigData":
         return get_option(self._path).data
      return get_option(self._path)


class ConfigInt(Config):
   def get(self) -> int:
      ...

   def set(self, value: int):
      ...


class ConfigFloat(Config):
   def get(self) -> float:
      ...

   def set(self, value: float):
      ...


class ConfigStr(Config):
   def get(self) -> str:
      ...

   def set(self, value: str):
      ...


class ConfigData(Config):
   def get(self) -> str:
      ...

   def set(self, value: str):
      ...
