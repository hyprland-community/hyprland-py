import hyprland

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()

    async def callback(self):
        await hyprland.Dispatch.exec("kitty") # open kitty term
    
    async def on_connect(self):
        print("Connected to hyprland")

        self.c.general.border_size = 10 # sync config
        await self.c.decoration.set_rounding(10) # async config

        await self.c.add_bind( # async bind
            hyprland.Bind(
                ["SUPER", "b"],
                self.callback, # function to run when bind is triggered
                hyprland.BindFlag.press
            )
        )
    
c = Config()

c.async_connect()