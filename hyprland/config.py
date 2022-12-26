from . import settings
# from .binds import Bind, BindFlag
from .sockets import BindListener
import asyncio

class Config(settings.Defaults):
    def __init__(self):
        super().__init__()
        self._binds = []
    
    def add_bind(self, bind):
        self._binds.append(bind)

    
    def start_bind_listener(self):
        loop = asyncio.get_event_loop()
        listener = BindListener(self)
        loop.create_task(listener.start())
        loop.run_forever()





    


