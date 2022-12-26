class BindFlag:
    locked = 0
    release = 1
    repeat = 2
    mouse = 3

class Bind:
    def __init__(self, label:str , key:dict, f, mode:int) -> None:
        self.key = key
        self.f = f
        self.mode = mode