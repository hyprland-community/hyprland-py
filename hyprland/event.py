import socket
import os
import asyncio
from .sockets import EventListener

class Events:

    def connect(self):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock")
            self.dispatch("connect")
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                dat = data.decode('utf-8').strip().split(">>")
                self.dispatch(dat[0], dat[1])

    async def _async_handler(self):
        print("async handler")
        self.listener = EventListener()
        print("async handler2")
        async for dat in self.listener.connect():
            print("async handler3")
            dat = dat.strip().split(">>")
            await self.async_dispatch(dat[0], dat[1] if len(dat) > 1 else "")
    
    def async_connect(self):
        asyncio.run(self._async_handler())
    
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
    
    



