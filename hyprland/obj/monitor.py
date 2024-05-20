from dataclasses import dataclass
from ..info import fetch_workspaces

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..obj.workspace import Workspace

@dataclass
class Monitor:
    id:int
    name:str
    description:str
    make:str
    model:str
    serial:str
    width:int
    height:int
    refresh_rate:float
    x:int
    y:int
    active_workspace_id:int
    active_workspace_name:str
    special_workspace_id:int
    special_workspace_name:str
    reserved:list
    scale:float
    transform:int
    focused:bool
    dpms_status:bool
    vrr:bool
    actively_tearing:bool
    disabled:bool
    current_format:str
    available_modes:list[str]

    def fetch_active_workspace(self)->'Workspace':
        return fetch_workspaces(id=self.active_workspace_id)

    def fetch_special_workspace(self)->'Workspace':
        return fetch_workspaces(id=self.special_workspace_id)

    @staticmethod
    def from_json(data:dict):
        return Monitor(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            make=data["make"],
            model=data["model"],
            serial=data["serial"],
            width=data["width"],
            height=data["height"],
            refresh_rate=data["refreshRate"],
            x=data["x"],
            y=data["y"],
            active_workspace_id=data["activeWorkspace"]["id"],
            active_workspace_name=data["activeWorkspace"]["name"],
            special_workspace_id=data["specialWorkspace"]["id"],
            special_workspace_name=data["specialWorkspace"]["name"],
            reserved=data["reserved"],
            scale=data["scale"],
            transform=data["transform"],
            focused=data["focused"],
            dpms_status=data["dpmsStatus"],
            vrr=data["vrr"],
            actively_tearing=data["activelyTearing"],
            disabled=data["disabled"],
            current_format=data["currentFormat"],
            available_modes=data["availableModes"]
        )