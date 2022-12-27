class BindFlag:
    locked = -1
    release = -2
    repeat = -3
    mouse = -4
    press = -5

class Bind:
    def __init__(self,key:list, f, flag:int=-5) -> None:
        self.key = key
        self.f = f
        match flag:
            case -1:
                self.flag = "l"
            case -2:
                self.flag = "r"
            case -3:
                self.flag = "e"
            case -4:
                self.flag = "m"
            case -5:
                self.flag = ""
            case _:
                raise Exception(f"hyprland: invalid flag: {flag}")