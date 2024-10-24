import sys
from typing import Callable

class __CLI__:
    def __init__(self):
        self.__args = sys.argv
        self.__attached_func_to_arg: dict[str,Callable] = {}
    
    def _cli_cmd(self, name: str) -> Callable:
        def decor(func: Callable) -> Callable:
            self.__attached_func_to_arg[name] = func
            return func
        return decor
    
    def is_cmd_invoked(self) -> list[bool, Callable] | bool:
        for arg in self.__args:
            if arg in self.__attached_func_to_arg:
                self.__attached_func_to_arg[arg]()
                return [True, self.__attached_func_to_arg[arg]]
        return False
