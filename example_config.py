import src.hyprland as hyprland
import asyncio
from src.hyprland import Bind, BindFlag

class Config(hyprland.Events):
    async def terminal(self):
        await hyprland.Dispatch.exec("kitty --single-instance")
    
    async def on_connect(self):
        print("Connected to hyprland")

        self.c = await hyprland.Config.from_conf()
        
        print(self.c.decoration.screen_shader)

e = Config()
e.async_connect()






