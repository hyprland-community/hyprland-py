from . import settings
# from .binds import Bind, BindFlag
from .sockets import BindListener
from threading import Thread
from .dispatch import Dispatch
from .info import Info
import asyncio
import inspect


class Config(settings.Defaults):
    def __init__(self):
        super().__init__()
        self.bind_listener = BindListener(self)
        self._binds = []
        self.start_bind_listener()
    
    async def from_conf()->'Config':
        from rich.console import Console
        config = Config()
        console = Console()
        sections = inspect.getmembers(settings.Defaults(), lambda a:not inspect.isroutine(a))
        sections = [a for a in sections if not(a[0].startswith('__') and a[0].endswith('__'))]
        for section in sections:
            options = inspect.getmembers(section[1], lambda a:not inspect.isroutine(a))
            options = [a for a in options if not(a[0].startswith('__') and a[0].endswith('__'))]
            for setting in options:
                option,value = setting
                val = await Info.get_option(f'{section[0]}:{option}',type(value))
                getattr(config,section[0]).__setattr__(option,val,ignore=True)
        return config

    def get_sections(self=None):
        sections = inspect.getmembers(settings.Defaults(), lambda a:not inspect.isroutine(a))
        sections = [a[0] for a in sections if not(a[0].startswith('__') and a[0].endswith('__'))]
        return sections
        
    def start_bind_listener(self):
        t = Thread(target=asyncio.run,args = [self.bind_listener.start()])
        t.start()
    
    async def add_bind(self, bind):
        await self.bind_listener.send_bind(bind)
        self._binds.append(bind)
    
    async def add_binds(self, binds):
        for bind in binds:
            await self.add_bind(bind)
    
    async def reload(self):
        await Dispatch.reload_config()
        self.__init__()
    
            


        
        






    


