from .sockets import async_hyprctl
from .util.scraper import parse_val
import json



class Info:
    async def version():
        return json.loads(await async_hyprctl('version -j'))
    
    async def monitors():
        return json.loads(await async_hyprctl('monitors -j'))
    
    async def workspaces():
        return json.loads(await async_hyprctl('workspaces -j'))
    
    async def clients():
        return json.loads(await async_hyprctl('clients -j'))
    
    async def devices():
        return json.loads(await async_hyprctl('devices -j'))
    
    async def active_window():
        return json.loads(await async_hyprctl('activewindow -j'))
    
    async def layers():
        return json.loads(await async_hyprctl('layers -j'))
    
    async def splash():
        return json.loads(await async_hyprctl('splash'))

    async def get_option(opt,prefered_type=None):
        resp = await async_hyprctl(f'getoption {opt} -j')
        if resp.strip()[0] == '{':
            dat:dict = json.loads(resp)
            import sys
            dat.pop('option')
            if dat['int'] <= -sys.maxsize:
                dat.pop('int')
            if dat['float'] <= sys.float_info.min:
                dat.pop('float')
            if dat['str'] == '':
                dat.pop('str')
            if dat['data'] == '0x0':
                dat.pop('data')
            for key in dat:
                dat[key] = parse_val(dat[key],key,quote=False)
            if len(dat) == 1:
                if prefered_type and (not prefered_type is type(None)) :
                    return prefered_type(dat[list(dat.keys())[0]])
                return dat[list(dat.keys())[0]]
            return dat
        return resp
    
    async def cursor_pos():
        return json.loads(await async_hyprctl('cursorpos -j'))
    

    

    
