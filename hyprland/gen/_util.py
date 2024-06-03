from typing import Any
from ..socket import command_send

# class decorator
def section(name:str):
    def decorator(cls):
        cls.__section_name = name
        return cls
    return decorator

def unparse_values(value):
    if isinstance(value,tuple):
        return " ".join(*value)
    if isinstance(value,list): # mods
        return " ".join(*value)
    if value is int or value is float:
        return value
    if isinstance(value,bool):
        return "true" if value else "false"
    else:
        return value
        
class Section:
    _section_name : str
    _section_map : dict

    _section_key : str

    def __setattr__(self, name: str, value: Any, ignore:bool = False) -> None:
        if not ignore and name in self._section_map:
            info = self._section_map[name]
            key = self._section_key + info["name"]
            cmd = f"keyword {key} {unparse_values(value)}"
            command_send(cmd,return_json=False,check_ok=True)
            super().__setattr__(name,value)
        else:
            super().__setattr__(name,value)
            
            
        

    