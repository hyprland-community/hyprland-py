import socket
import os

class Events:

    def connect(self):
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.connect(f"/tmp/hypr/{os.getenv('HYPRLAND_INSTANCE_SIGNATURE')}/.socket2.sock")
            self.dispatch("connect")
            while True:
                data = sock.recv(1024)
                if not data:
                    break
                dat = data.decode('utf-8').strip().split(">>")
                self.dispatch(dat[0], dat[1])
    
    def dispatch(self,event,raw=None):
        if hasattr(self, 'on_'+event):
            if raw:
                getattr(self, 'on_'+event)(*self.parse(raw))
            else:
                getattr(self, 'on_'+event)()
        if hasattr(self, 'on_any'):
            getattr(self, 'on_any')(event, *self.parse(raw))
        
    
    def parse(self, raw):
        if raw:
            return tuple(map(lambda x: x.strip(),raw.split(",")))
        else:
            return []
    
    



