import hyprland

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()

    async def callback(self):
        await hyprland.Dispatch.exec("kitty --") # open kitty term
    
    async def on_connect(self):
        print("Connected to hyprland")

        
    
c = Config()

c.async_connect()