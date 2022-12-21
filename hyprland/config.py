from sockets import connect_commands
from settings import Defaults

class Config(Defaults):
    def __init__(self):
        self.sock = connect_commands()
        super().__init__(self.sock)
        

    

c = Config()

c.general.border_size = 5

