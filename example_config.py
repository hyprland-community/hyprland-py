import hyprland

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()

    async def callback(self):
        print("keybind pressed")
    
    async def on_connect(self):
        print("Connected to the server!")
        self.c.general.border_size = 10
        await self.c.decoration.set_rounding(10)

        await self.c.add_bind(
            hyprland.Bind(
                ["SUPER", "a"],
                self.callback,
                hyprland.BindFlag.press
            )
        )
    
c = Config()

c.async_connect()