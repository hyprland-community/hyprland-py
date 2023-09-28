**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# binds


 - [Keybinder](#Keybinder)

 - [Keyunbinder](#Keyunbinder)

 - [Key](#Key)

 - [Mod](#Mod)

 - [Keybind](#Keybind)

 - [KeybindBuilder](#KeybindBuilder)



## `submap`


```py

def submap(keybind: Keybind):
    ...
```

Submap decorator. Apply on a function to create a submap, will be executed on application.




Usage:
```py
>>> @submap(Mod.SUPER + Key('R'))
>>> def my_submap():
>>>    (Mod.EMPTY + Key('F')).bind(Exec('firefox'))
```


# `Keybinder`


```py

class Keybinder:
    ...
```

## `to_command`


```py

def to_command(self):
    ...
```

# `Keyunbinder`


```py

class Keyunbinder:
    ...
```

## `to_command`


```py

def to_command(self):
    ...
```

# `Key`


```py

class Key:
    ...
```

See <https://wiki.hyprland.org/Configuring/Binds/#uncommon-syms--binding-with-a-keycode>





# `Mod`


```py

class Mod:
    ...
```

## `from_modmask`


```py

def from_modmask(cls, modmask: int):
    ...
```

## `__add__`


```py

def __add__(self, other: Key | Mod) -> Keybind | KeybindBuilder:
    ...
```

# `Keybind`


```py

class Keybind:
    ...
```

## `from_bind`


```py

def from_bind(cls, bind: Bind):
    ...
```

Convert a `info.Bind` returned by `info.binds()` into a `Keybind`. Discards dispatcher information.





## `_flags`


```py

def _flags(self):
    ...
```

## `_bindstr`


```py

def _bindstr(self, dispatcher: Dispatcher | None):
    ...
```

## `locked`


```py

def locked(self):
    ...
```

locked, aka. works also when an input inhibitor (e.g. a lockscreen) is active.





## `release`


```py

def release(self):
    ...
```

release, will trigger on release of a key.





## `repeat`


```py

def repeat(self):
    ...
```

repeat, will repeat when held.





## `non_consuming`


```py

def non_consuming(self):
    ...
```

non-consuming, key/mouse events will be passed to the active window in addition to triggering the dispatcher.





## `mouse`


```py

def mouse(self):
    ...
```

See <https://wiki.hyprland.org/Configuring/Binds/#mouse-binds>





## `transparent`


```py

def transparent(self):
    ...
```

transparent, cannot be shadowed by other binds.





## `bind`


```py

def bind(self, dispatcher: Dispatcher):
    ...
```

## `to_bind_command`


```py

def to_bind_command(self, dispatcher: Dispatcher):
    ...
```

## `unbind`


```py

def unbind(self):
    ...
```

## `to_unbind_command`


```py

def to_unbind_command(self):
    ...
```

## `submap`


```py

def submap(self, func: Callable[[], None]):
    ...
```

# `KeybindBuilder`


```py

class KeybindBuilder:
    ...
```

## `__init__`


```py

def __init__(self, mods: list[Mod]):
    ...
```

## `__add__`


```py

def __add__(self, other: Mod | Key):
    ...
```

