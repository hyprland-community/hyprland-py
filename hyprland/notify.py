from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .socket import Command


class Icon(Enum):
    NONE = -1
    WARNING = 0
    INFO = 1
    HINT = 2
    ERROR = 3
    CONFUSED = 4
    OK = 5


@dataclass
class Notify(Command):
    icon: Icon
    time: int
    color: str
    message: str

    def to_command(self):
        return f"notify {self.icon.value} {self.time} {self.color} {self.message}".encode()
