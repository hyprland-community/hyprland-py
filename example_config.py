import hyprland
import random


class e(hyprland.Events):

    def on_connect(self):
        self.c = hyprland.Config()

        self.c.decoration.rounding = 12
        self.c.general.border_size = 10
    
    def on_any(self, event, *args):
        self.c.general.border_size = random.randint(0, 20)


e().connect()