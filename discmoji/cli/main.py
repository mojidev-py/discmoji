import sys
from typing import Callable

class __CLI__:
    def __init__(self):
        self.__args = sys.argv
        self.__attached_func_to_arg: dict[str,Callable] = {}
    
    
    def _cli_cmd(self,name: str):
        def decor(func: Callable):
            self.__attached_func_to_arg[name] = func
            return self.__attached_func_to_arg[name]
        return decor
    # this decorator is to provide a better interface for making callbacks for arguments
    
    def is_cmd_invoked(self) -> list[bool,Callable] | bool:
        for arg in self.__args:
            for name in self.__attached_func_to_arg.keys():
                if name == arg:
                    self.__attached_func_to_arg[name]()
                    # runs with no args for now
                return [True,self.__attached_func_to_arg[name]]
        return False