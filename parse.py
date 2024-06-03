import sys
import json

MODS = ["SHIFT","CTRL","ALT","META","SUPER"] # [TODO] find a proper list of valid modifiers

def parse_value(val:str,t:str):
    match t.lower():
        case "int":
            return int(val)
        case "float":
            return float(val)
        case "bool":
            if val.isnumeric():
                return bool(int(val))
            match val.lower():
                case "true":
                    return True
                case "false":
                    return False
                case "yes":
                    return True
                case "no":
                    return False
                case "on":
                    return True
                case "off":
                    return False
        case "vec2":
            if val.startswith("(") and val.endswith(")"):
                val = val[1:-1]
            if val.startswith("[") and val.endswith("]"):
                val = val[1:-1]
            if "," in val:
                return tuple([float(x) for x in val.split(",")])
            return tuple([float(x) for x in val.split()])
        case "mod":
            mods = []
            buf = ""
            for char in val.upper():
                buf += char
                if buf in MODS:
                    mods.append(buf)
                    buf = ""
            return mods
        
        # case "color":
        #     ...
        # case "gradient":
        #     ...

        case _:
            return val
        
def string_value(val):
    if isinstance(val,bool) or isinstance(val,int) or isinstance(val,float):
        return str(val)
    elif isinstance(val,tuple):
        return f"({','.join([str(x) for x in val])})"
    elif isinstance(val,list):
        return f"[{','.join([str(x) for x in val])}]"
    elif val == "\\[\\[Empty\\]\\]" or val == "[[EMPTY]]":
        return None
    elif val == "\\[\\[Auto\\]\\]" or val == "[[AUTO]]":
        return '"auto"'
    else:
        return f'"{val}"'
         
def standardize_name(name:str):
    return name.lower().replace(" ","_").replace("-","_").replace(".","_")

def gen_variables():
    path = 'hyprland-wiki/pages/Configuring/Variables.md'

    dat = {}
    keys = {}

    with open(path, 'r') as f:
        raw = f.readlines()

    in_sections = False

    current_section = None

    ignore = False
    
    for line in raw:
        if ignore:
            if line.startswith("{{< /callout >}}"):
                ignore = False
            continue
        if line.startswith("{{< callout type=info >}}"):
            ignore = True
        if line.startswith('## Sections'):
            in_sections = True
            continue

        if in_sections:
            if line.startswith('### '):
                current_section = line[4:-1]
                dat[current_section] = []
                table_heads = []
                keys[current_section.title().replace(" ","").replace("-","")] = f"{current_section.replace(' ','_').replace('-','_').lower()}:"

            if line.startswith('#### '):
                current_section = line[5:-1]
                dat[current_section] = []
                table_heads = []
                keys[current_section.title().replace(" ","").replace("-","")] = f"{current_section.replace(' ','_').replace('-','_').lower()}:"

            if line.lower().startswith("_subcategory"):
                key = line[14:-2].strip(":")
                parent = key.split(":")[0].replace(' ','_').replace('-','_').lower()

                keys[current_section.title().replace(" ","").replace("-","")] = f"{parent}:{keys[current_section.title().replace(" ","").replace("-","")]}"

            if line.startswith('|'):
                if not table_heads:
                    table_heads = [x.strip() for x in line[1:-1].split('|')[:-1]]
                else:
                    table_data = [x.strip() for x in line[1:-1].split('|')]
                    if table_data[0] == "---":
                        continue
                    if len(table_data) < len(table_heads):
                        continue
                    dat[current_section].append({table_heads[i]:table_data[i] for i in range(len(table_heads))})
    
    return dat, keys

def gen_python(variables:dict, keys: dict):
    out = f"from ._util import Section\nKEYS = {keys}\n\n"
    for section in variables:
        out += f"class {section.title().replace(" ","").replace("-","")}(Section):\n"
        section_map = {}

        part = ""

        for variable in variables[section]:
            val = parse_value(variable['default'],variable['type'])
            section_map[standardize_name(variable['name'])] = variable
            part += f"""    {standardize_name(variable['name'])}: {type(val).__name__} = {string_value(val)}\n    # {variable['description']}\n"""
        
        out += "    _section_name = " + f'"{section}"' + "\n"
        out += "    _section_map = " + json.dumps(section_map) + "\n"
        out += f'    _section_key = "{keys[section.title().replace(" ","").replace("-","")]}"\n\n'

        out += part + "\n"

    out += """class Default:\n"""
    for section in variables:
        out += f"    {section.replace(' ','_').replace('-','_').lower()}: {section.title().replace(' ','').replace('-','')} = {section.title().replace(' ','').replace('-','')}()\n"

    return out

if __name__ == "__main__":
    name = sys.argv[1:][0].lower()
    target = None
    if len(sys.argv[1:]) >= 2:
        target = sys.argv[1:][1]

    match name:
        case "variables":
            if target:
                with open(target, 'w') as f:
                    f.write(gen_python(*gen_variables()))
            else:
                print(gen_python(gen_variables()))
        case _:
            print("Invalid argument")
            sys.exit(1)
            