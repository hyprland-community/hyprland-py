import requests
import bs4

def parse_val(s,t,quote=True):
    if s == '[EMPTY]':
        return ''
    if s == '[[EMPTY]]':
        return ''
    elif s in ['true','yes','on']:
        return True
    elif s in ['false','no','off']:
        return False
    elif s == 'unset':
        return None
    else:
        match t:
            case 'int':
                return int(s)
            case 'float':
                return float(s)
            case 'color':
                return int(s, 16)
            case _:
                if quote:
                    print('Unknown type: ' + t)
                    return f'\'{s}\''
                return s

def get_dat():
    raw = requests.get('https://wiki.hyprland.org/Configuring/Variables/#sections').text
    dat = {}
    soup = bs4.BeautifulSoup(raw, 'html.parser')
    sections = soup.find('h1', id = 'sections')
    if sections and sections.parent:
        blocks = sections.parent.findAllNext(class_='gdoc-page__anchorwrap')
        for block in blocks:
            name = block.find('h2') or block.find('h1')
            if name:
                table = block.next_sibling.find('table')
                if table and table.name == 'table':
                    dat[name.text.strip()] = []
                    for row in table.findAll('tr'):
                        cells = [cell.text.strip() for cell in row.findAll('td')]
                        if len(cells) >= 4:
                            dat[name.text.strip()].append({
                                    'name': cells[0],
                                    'desc': cells[1],
                                    'type': cells[2],
                                    'default': cells[3],
                            })
    return dat
            
def build_settings(dat,path:str):
    with open(path,'w') as f:
        f.write('""" This file is generated by util/scraper.py """\n\n')
        f.write('from . import sockets\n\n')
        setting_class = f'\nclass Defaults:\n\n    def __init__(self):\n'
        for section in dat:
            f.write(f'''class {section}(sockets.keyword):\n\n''')
            for setting in dat[section]:
                name = setting["name"].replace(".","__")
                parsed_val = parse_val(setting["default"],setting["type"])
                f.write(f'    {name} = {parsed_val}\n')
                f.write(f'    """ {setting["desc"]} """\n\n')
                f.write(f'    async def set_{name}(self,x:\'{type(parsed_val).__name__.replace("NoneType","None")}\'):\n        """ {setting["desc"]} """\n        await self.send_cmd(\"{name}\",x)\n        self.__setattr__(\"{name}\",x,ignore=True)\n\n\n')
            setting_class += f'        self.{section.lower()} = {section}()\n'
        f.write(setting_class)


if __name__ == '__main__':
    print("starting scrape")
    dat = get_dat()
    build_settings(dat,'./src/hyprland/settings.py')
    print("written to './src/hyprland/settings.py'")
