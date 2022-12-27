from . import settings
# from .binds import Bind, BindFlag
from .sockets import BindListener
from threading import Thread
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
        print("adding bind")
        await self.bind_listener.send_bind(bind)
        self._binds.append(bind)
        






    


