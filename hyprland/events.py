from typing import Optional
from .socket import EventListener
import asyncio

class Events:
    def __init__(self):
        self.events = {}
        self.listener = None
    
    async def async_connect(self):
        self.listener = EventListener()
        async for event in self.listener.start():
            if ">>" in event:
                event_name, args = event.split(">>")
                args = args.split(",")
                await self.emit(event_name, *args)
            else:
                await self.emit(event)
    
    def on(self, event: Optional[str] = None):
        def decorator(callback):            
            self.add_handle(event, callback)
        return decorator
        
    def add_handle(self, event: str, callback: callable):
        if self.events.get(event):
            self.events[event].append(callback)
        else:
            self.events[event] = [callback]
        print(self.events)
    
    def remove_handle(self, event: str, callback: callable):
        if self.events.get(event):
            self.events[event].remove(callback)
        else:
            raise AttributeError(f'Event {event} not found')

    async def emit(self, event: str, *args, **kwargs):
        if event in self.events:
            for callback in self.events[event]:
                if asyncio.iscoroutinefunction(callback):
                    await callback(*args, **kwargs)
                else:
                    callback(*args, **kwargs)
    
        


