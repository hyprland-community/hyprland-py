# Hyprland-py
An unofficial async python wrapper for Hyprland's IPC supposed to somewhat work like awesomewm api in lua


# Todo

- [x] async sockets
- [x] change config options
- [x] event listeners
- [x] keybinds
- [ ] windowrules
- [x] hyprland info
- [x] misc hyprland commands(change workspace, move active window etc...)*(dispatchers)*
- [ ] a nice way to handle colors
- [ ] build `settings.py` file based on current hl version
- [x] get config values from the current hyprland config instead of using default values
> getting binds still dont work
- [ ] docs
- [ ] widgets??

# Install

### git

from git
```py
pip install git+https://github.com/hyprland-community/hyprland-py
```

### release

from [pypi](https://pypi.org/project/hyprland/0.1/)
```py
pip install hyprland
```

# Example
change window border to a random number between 0 and 20 everytime a new window is opened
```py
import hyprland
from hyprland import Bind, BindFlag

class Config(hyprland.Events):
    def __init__(self):
        self.c = hyprland.Config()
        super().__init__()

    async def terminal(self):
        await hyprland.Dispatch.exec("kitty --single-instance")
    
    async def on_connect(self):
        print("Connected to hyprland")
        
        await self.c.add_binds([
            # general binds
            Bind(["SUPER","m"],hyprland.Dispatch.exit),

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
```
