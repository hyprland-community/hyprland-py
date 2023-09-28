**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# socket2


 - [Events](#Events)



# `Events`


```py

class Events:
    ...
```

## `__init__`


```py

def __init__(self):
    ...
```

## `workspace`


```py

def workspace(self, f: Callable[[str], R]):
    ...
```

Emitted on workspace change. Is emitted ONLY when a user requests a workspace change, and is not emitted on mouse



movements. See `activemon`.
`(workspace_name)`


## `focusedmon`


```py

def focusedmon(self, f: Callable[[str, str], R]):
    ...
```

Emitted on the active monitor being changed.



`(mon_name, workspace_name)`


## `activewindow`


```py

def activewindow(self, f: Callable[[str, str], R]):
    ...
```

Emitted on the active window being changed.



`(window_class, window_title)`


## `activewindowv2`


```py

def activewindowv2(self, f: Callable[[str], R]):
    ...
```

Emitted on the active window being changed.



`(window_address)`


## `fullscreen`


```py

def fullscreen(self, f: Callable[[bool], R]):
    ...
```

Emitted when a fullscreen status of a window changes.



`(window_entered_fullscreen)`


## `monitorremoved`


```py

def monitorremoved(self, f: Callable[[str], R]):
    ...
```

Emitted when a monitor is removed (disconnected).



`(monitor_name)`


## `monitoradded`


```py

def monitoradded(self, f: Callable[[str], R]):
    ...
```

`(monitor_name)`





## `createworkspace`


```py

def createworkspace(self, f: Callable[[str], R]):
    ...
```

## `destroyworkspace`


```py

def destroyworkspace(self, f: Callable[[str], R]):
    ...
```

## `moveworkspace`


```py

def moveworkspace(self, f: Callable[[str], R]):
    ...
```

## `renameworkspace`


```py

def renameworkspace(self, f: Callable[[str], R]):
    ...
```

## `activespecial`


```py

def activespecial(self, f: Callable[[str], R]):
    ...
```

## `activelayout`


```py

def activelayout(self, f: Callable[[str], R]):
    ...
```

## `openwindow`


```py

def openwindow(self, f: Callable[[str], R]):
    ...
```

## `closewindow`


```py

def closewindow(self, f: Callable[[str], R]):
    ...
```

## `movewindow`


```py

def movewindow(self, f: Callable[[str], R]):
    ...
```

## `openlayer`


```py

def openlayer(self, f: Callable[[str], R]):
    ...
```

## `closelayer`


```py

def closelayer(self, f: Callable[[str], R]):
    ...
```

## `submap`


```py

def submap(self, f: Callable[[str], R]):
    ...
```

## `changefloatingmode`


```py

def changefloatingmode(self, f: Callable[[str], R]):
    ...
```

## `urgent`


```py

def urgent(self, f: Callable[[str], R]):
    ...
```

## `minimize`


```py

def minimize(self, f: Callable[[str], R]):
    ...
```

## `screencast`


```py

def screencast(self, f: Callable[[str], R]):
    ...
```

## `windowtitle`


```py

def windowtitle(self, f: Callable[[str], R]):
    ...
```

## `ignoregrouplock`


```py

def ignoregrouplock(self, f: Callable[[str], R]):
    ...
```

## `lockgroups`


```py

def lockgroups(self, f: Callable[[str], R]):
    ...
```

