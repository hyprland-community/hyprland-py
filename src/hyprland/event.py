import socket
import os
import asyncio
from .sockets import EventListener
from .dispatch import Dispatch

class Events:

    async def reload(self):
        await Dispatch.reload_config()
        self.__init__()

    def connect(self):
        for data in self.listener.start():
            dat = data.decode('utf-8').strip().split(">>")
            self.dispatch(dat[0], dat[1])
    
    def async_connect(self):
        async def _async_handler(self):
            await Dispatch.reload_config()
            self.listener = EventListener()
            async for dat in self.listener.async_start():
                dat = dat.strip().split(">>")
                await self.async_dispatch(dat[0], dat[1] if len(dat) > 1 else None)
        asyncio.run(_async_handler(self))
    
    def dispatch(self,event,raw=None):
        if hasattr(self, 'on_'+event):
            if raw:
                getattr(self, 'on_'+event)(*self.parse(raw))
            else:
                getattr(self, 'on_'+event)()
        if hasattr(self, 'on_any'):
            getattr(self, 'on_any')(event, *self.parse(raw))
    
    async def async_dispatch(self,event,raw=None):
        if hasattr(self, 'on_'+event):
            if raw:
                await getattr(self, 'on_'+event)(*self.parse(raw))
            else:
                await getattr(self, 'on_'+event)()
        if hasattr(self, 'on_any'):
           await getattr(self, 'on_any')(event, *self.parse(raw))
        
    
    def parse(self, raw):
        if raw:
            return tuple(map(lambda x: x.strip(),raw.split(",")))
        else:
            return []
    
    



