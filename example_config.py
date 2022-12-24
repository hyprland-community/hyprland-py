import hyprland
import random


class e(hyprland.Events):

    def on_connect(self):
        self.c = hyprland.Config()

        self.c.decoration.rounding = 12
        self.c.general.border_size = 2
    
    def on_openwindow(self, waddr, wname, wclass, wtitle):
        self.c.general.border_size = random.randint(0, 20)


e().connect()