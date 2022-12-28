from .sockets import async_command_send

class Dispatch:

    async def exec(cmd):
        await async_command_send(f'/dispatch exec {cmd}')
    
    async def _pass(w):
        await async_command_send(f'/dispatch pass {w}')
    
    async def kill_active():
        await async_command_send('/dispatch killactive')
    
    async def close_window(window):
        await async_command_send(f'/dispatch closewindow {window}')
    
    async def workspace(w):
        await async_command_send(f'/dispatch workspace {w}')
    
    async def move_to_workspace(w):
        await async_command_send(f'/dispatch movetoworkspace {w}')
    
    async def move_to_workspace_silent(w):
        await async_command_send(f'/dispatch movetoworkspacesilent {w}')
    
    async def toggle_floating(w=''):
        await async_command_send(f'/dispatch togglefloating {w}')
    
    async def fullscreen(mode):
        await async_command_send(f'/dispatch fullscreen {mode}')
    
    async def dpms(m,active:bool):
        await async_command_send(f'/dispatch dpms {"on" if active else "off"} {m}')
    
    async def pseudo():
        await async_command_send('/dispatch pseudo')
    
    async def pin():
        await async_command_send('/dispatch pin')
    
    async def move_focus(direction):
        await async_command_send(f'/dispatch movefocus {direction}')

    async def move_window(direction):
        await async_command_send(f'/dispatch movewindow {direction}')
    
    async def center_window():
        await async_command_send('/dispatch centerwindow')
    
    async def resize_active(x,y):
        await async_command_send(f'/dispatch resizeactive {x} {y}')
    
    async def move_active(x,y):
        await async_command_send(f'/dispatch moveactive {x} {y}')

    async def resize_window_pixel(window,x,y):
        await async_command_send(f'/dispatch resizewindowpixel {x} {y},{window}')
    
    async def move_window_pixel(window,x,y):
        await async_command_send(f'/dispatch movewindowpixel {x} {y},{window}')
    
    async def cycle_next(prev=False):
        await async_command_send(f'/dispatch cyclenext {"prev" if prev else ""}')

    async def swap_next(prev=False):
        await async_command_send(f'/dispatch swapnext {"prev" if prev else ""}')
    
    async def focus_window(w):
        await async_command_send(f'/dispatch focuswindow {w}')
    
    async def focus_monitor(m):
        await async_command_send(f'/dispatch focusmonitor {m}')
    
    async def split_ratio(x:float):
        await async_command_send(f'/dispatch splitratio {float(x)}')
    
    async def toggle_opaque():
        await async_command_send('/dispatch toggleopaque')
        ### 
    async def move_cursor_to_corner(c):
        await async_command_send(f'/dispatch movecursortocorner {c}')
    
    async def workspace_opt(opt):
        await async_command_send(f'/dispatch workspaceopt {opt}')

    async def exit():
        await async_command_send('/dispatch exit')
    
    async def force_renderer_reload():
        await async_command_send('/dispatch forcerendererreload')
    
    async def move_current_workspace_to_monitor(m):
        await async_command_send(f'/dispatch movecurrentworkspacetomonitor {m}')
    
    async def move_workspace_to_monitor(w,m):
        await async_command_send(f'/dispatch moveworkspacetomonitor {w} {m}')
    
    async def swap_active_workspaces(m1,m2):
        await async_command_send(f'/dispatch swapactiveworkspaces {m1} {m2}')
    
    async def bring_active_to_top():
        await async_command_send('/dispatch bringactivetotop')
    
    async def toggles_pecial_workspace(sw=None):
        await async_command_send(f'/dispatch togglespecialworkspace {sw if sw else ""}')

    ### end of the actual dispatch commands
    ### and henceforth are the commands that are not 

    async def reload_config():
        await async_command_send('reload')
    
    async def kill_mode():
        await async_command_send('kill')
    
    async def cursor_theme(theme,size):
        await async_command_send(f'cursor {theme} {size}')
    
    async def switch_xkb_layout(device,cmd):
        await async_command_send(f'switchxkblayout {device} {cmd}')
