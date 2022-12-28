from .sockets import async_command_send
import json


class Info:
    async def version():
        return json.loads(await async_command_send('version -j'))
    
    async def monitors():
        return json.loads(await async_command_send('monitors -j'))
    
    async def workspaces():
        return json.loads(await async_command_send('workspaces -j'))
    
    async def clients():
        return json.loads(await async_command_send('clients -j'))
    
    async def devices():
        return json.loads(await async_command_send('devices -j'))
    
    async def active_window():
        return json.loads(await async_command_send('activewindow -j'))
    
    async def layers():
        return json.loads(await async_command_send('layers -j'))
    
    async def splash():
        return json.loads(await async_command_send('splash'))

    async def get_option(opt):
        return await async_command_send(f'getoption {opt}')
    
    async def cursor_pos():
        return json.loads(await async_command_send('cursorpos -j'))
    

    

    
