import hyprland
from hyprland import Bind, BindFlag

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()

    async def terminal(self):
        hyprland.Dispatch.exec("kitty --single-instance")
    
    async def on_connect(self):
        print("Connected to hyprland")
        
        await self.c.add_binds([
            # mouse binds
            Bind(["SUPER","mouse:272"],"movewindow",BindFlag.mouse),
            Bind(["SUPER","mouse:273"],"resizewindow",BindFlag.mouse),

            # keyboard binds
            Bind(["SUPER","return"],self.terminal),
            Bind(["SUPER","q"],hyprland.Dispatch.kill_active),
        ])

        # workspace binds
        for i in range(1,11):
            await self.c.add_bind(Bind([f"SUPER",str(i) if i!= 10 else str(0)],hyprland.Dispatch.workspace,args=[i]))
        
        for i in range(1,11):
            await self.c.add_bind(Bind([f"ALT",str(i) if i!= 10 else str(0)],hyprland.Dispatch.move_to_workspace,args=[i]))

    
c = Config()

c.async_connect()