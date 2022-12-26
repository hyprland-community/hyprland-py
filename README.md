# Hyprland-py
An unofficial python wrapper for Hyprland's IPC supposed to somewhat work like awesomewm api in lua


# Todo

- [x] async sockets
- [x] change config options
- [x] event listeners
- [ ] keybinds
- [ ] windowrules
- [ ] hyprland info
- [ ] misc hyprland commands(change workspace, move active window etc...)
- [ ] build `settings.py` file based on current hl version
- [ ] 

# Example
change window border to a random number between 0 and 20 everytime a new window is opened
```py
import hyprland
import random


class e(hyprland.Events):

    def on_connect(self):
        self.c = hyprland.Config()

        self.c.decoration.rounding = 12
        self.c.general.border_size = 10
    
    def on_openwindow(self, waddr, wname, wclass, wtitle):
        self.c.general.border_size = random.randint(0, 20)


e().connect()
```
