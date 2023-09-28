**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# socket


 - [Command](#Command)



## `_socket`


```py

def _socket():
    ...
```

Opens a connection to the Hyprland's hyprctl IPC socket.





## `query`


```py

def query(command: bytes):
    ...
```

Executes a hyprctl command using the IPC socket with the json flag and returns the response.





## `execute`


```py

def execute(command: Command | bytes):
    ...
```

Executes a hyprctl command using the IPC socket. Raises `HyprlandError` on error.





## `execute_batch`


```py

def execute_batch(commands: Iterable[Command | bytes] | Command | bytes):
    ...
```

Executes a batch of hyprctl command using the IPC socket. Raises `HyprlandError` on error.





# `Command`


```py

class Command:
    ...
```

## `to_command`


```py

def to_command(self) -> bytes:
    ...
```

