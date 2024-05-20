from .socket import command_send, async_command_send




def exec(cmd:str, rules:list):
    return command_send("dispatch exec "+cmd,check_ok=True)

