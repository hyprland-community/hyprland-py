from . import settings
# from .binds import Bind, BindFlag
from .sockets import BindListener
from threading import Thread
from .dispatch import Dispatch
import asyncio


class Config(settings.Defaults):
    def __init__(self):
        super().__init__()
        self.bind_listener = BindListener(self)
        self._binds = []
        self.start_bind_listener()

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



        
        






    


