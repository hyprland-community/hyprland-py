
import inspect


async def read_config(c):
    sections = inspect.getmembers(c, lambda a:not inspect.isroutine(a))
    sections = [a for a in sections if not(a[0].startswith('__') and a[0].endswith('__'))]
    for section in sections:
        print(section)

read_config()
        