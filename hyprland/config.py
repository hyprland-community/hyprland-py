from dataclasses import dataclass

@dataclass
class Color:
    r: int
    g: int
    b: int
    a: int

    def to_rgba(self)->str:
        return f'rgba({self.r}{self.g}{self.b}{self.a})'
    
    def to_rgb(self)->str:
        return f'rgb({self.r}{self.g}{self.b})'

    @staticmethod
    def from_str(dat:str):
        dat = dat.strip()
        if dat.startswith("rgb("):
            code = dat[4:-1]
            r = int(code[:2],16)
            g = int(code[2:4],16)
            b = int(code[4:],16)
            return Color(dat,r,g,b,255)
        elif dat.startswith("rgba("):
            code = dat[5:-1]
            r = int(code[:2],16)
            g = int(code[2:4],16)
            b = int(code[4:6],16)
            a = int(code[6:],16)
            return Color(dat,r,g,b,a)
        elif dat.startswith("0x"):
            code = dat[2:]
            a = int(code[:2],16)
            r = int(code[2:4],16)
            g = int(code[4:6],16)
            b = int(code[6:],16)
            return Color(dat,r,g,b,a)

    @staticmethod
    def rgba(r:int,g:int,b:int,a:int):
        r = hex(r)[2:]
        g = hex(g)[2:]
        b = hex(b)[2:]
        a = hex(a)[2:]

        r = r if len(r) == 2 else '0' + r
        g = g if len(g) == 2 else '0' + g
        b = b if len(b) == 2 else '0' + b
        a = a if len(a) == 2 else '0' + a

        return Color(r,g,b,a)
    
    @staticmethod
    def rgb(r:int,g:int,b:int):
        r = hex(r)[2:]
        g = hex(g)[2:]
        b = hex(b)[2:]

        r = r if len(r) == 2 else '0' + r
        g = g if len(g) == 2 else '0' + g
        b = b if len(b) == 2 else '0' + b

        return Color(r,g,b,255)
    
    @staticmethod
    def legacy(hex:str):
        hex = hex[1:] if hex[0] == '#' else hex
        hex = hex[2:] if hex[:2] == '0x' else hex
        a = hex[:2]
        r = hex[2:4]
        g = hex[4:6]
        b = hex[6:8]
        return Color(int(r,16),int(g,16),int(b,16),int(a,16))


@dataclass
class Gradient:
    deg: float
    colors: list[Color]

    def to_str(self):
        return f"{' '.join(color.to_rgba() for color in self.colors)} {self.deg}deg"

    @staticmethod
    def from_colors(*colors:list[Color],deg:float = 0):
        return Gradient(f"{' '.join(color.value for color in colors)} {deg}deg",colors,deg)
    
    @staticmethod
    def from_str(dat:str):
        dat = dat.strip()
        segments = dat.split()
        if segments[-1].endswith("deg"):
            deg = int(segments[-1][:-3])
            colors = segments[:-1]

            return Gradient(deg=deg,colors=[Color.from_str(color) for color in colors])
        else:
            deg = 0
            colors = segments

        

    