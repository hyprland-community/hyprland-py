from dataclasses import dataclass
from .monitor import Monitor
from .window import Window

from ..info import fetch_workspaces

@dataclass
class WorkspaceIdentity:
    key:str = None
    value = None
    identifier:str=""

    def __post_init__(self):
        if self.key and self.value:
            self.identifier = f"{self.key}:{self.value}"
        else:
            raise AttributeError("WorkspaceIdentity must have a key and value or an identifier")
    
    @staticmethod
    def from_id(id:int):
        return WorkspaceIdentity(key="id", value=id)
    
    @staticmethod
    def from_name(name:str):
        return WorkspaceIdentity(key="name", value=name)
    
    @staticmethod
    def from_special_name(name:str):
        return WorkspaceIdentity(key="special", value=name)
    
    @staticmethod
    def relative_monitor(offset:int=0,include_empty:bool=False):
        return WorkspaceIdentity(identifier=f"{'r' if include_empty else 'm'}{offset}")
    
    @staticmethod
    def absolute_monitor(offset:int=0,include_empty:bool=False):
        return WorkspaceIdentity(identifier=f"{'r' if include_empty else 'm'}~{offset}")
    
    @staticmethod
    def relative(offset:int=0,include_empty:bool=False):
        return WorkspaceIdentity(identifier=f"{'r' if include_empty else 'w'}{offset}")
    
    @staticmethod
    def absolute(offset:int=0,include_empty:bool=False):
        return WorkspaceIdentity(identifier=f"{'r' if include_empty else 'w'}~{offset}")

    @staticmethod
    def next(count:int=1):
        return WorkspaceIdentity(identifier=f"+{count}")
    
    @staticmethod
    def previous(count:int=1):
        return WorkspaceIdentity(identifier=f"-{count}")
    
    @staticmethod
    def first_empty_monitor():
        return WorkspaceIdentity(identifier="emptym")
    
    @staticmethod
    def first_empty():
        return WorkspaceIdentity(identifier="empty")
    
    @staticmethod
    def next_empty_monitor():
        return WorkspaceIdentity(identifier=f"emptynm")

    @staticmethod
    def next_empty():
        return WorkspaceIdentity(identifier=f"emptyn")


@dataclass
class Workspace:
    id:int
    name:str
    monitor_id:int
    windows:int
    has_fullscreen:bool = False
    last_active_window_id:str = None
    last_active_window_title:str = None

    # def fetch_monitor(self)->Monitor:
    #     return Monitor.from_id(self._monitor_id)

    def fetch_windows(self)->list[Window]:
        ...
    
    def fetch_last_active_window(self)->Window:
        ...

    @staticmethod
    def from_json(data:dict):
        return Workspace(
            id=data["id"],
            name=data["name"],
            windows=data["windows"],
            monitor_id=data["monitorID"],
            has_fullscreen=data["hasfullscreen"],
            last_active_window_id=data["lastwindow"],
            last_active_window_title=data["lastwindowtitle"]
        )
    
    @staticmethod
    def from_id(id:int):
        return fetch_workspaces(id=id)