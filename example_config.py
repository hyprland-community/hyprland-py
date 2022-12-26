import hyprland

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()
    
    async def on_connect(self):
        print("Connected to the server!")
        self.c.general.border_size = 10
        await self.c.decoration.set_rounding(10)


    async def on_any(self,*args,**kwargs):
        print(f"any: {args}")
    

c = Config()

c.async_connect()