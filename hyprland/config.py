from settings import Defaults
import time
import math

class Config(Defaults):
    def __init__(self):
        super().__init__()
            
c = Config()

c.general.border_size = 10

i = 0
while 1:
    i += 1
    c.decoration.rounding += math.sin(i/10) * 10
    time.sleep(0.04)


