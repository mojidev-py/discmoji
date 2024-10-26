import sys
from typing import Callable, List

class __CLI__:
    def __init__(self):
        self.__args = sys.argv
        self.__attached_func_to_arg: dict[str, Callable] = {}
        self.__parsed_args: List[str] = []

    def _cli_cmd(self, name: str):
        def decor(func: Callable):
            self.__attached_func_to_arg[name] = func
            return self.__attached_func_to_arg[name]
        return decor

    def is_cmd_invoked(self) -> List[bool, Callable] | bool:
        for arg in self.__args:
            for name in self.__attached_func_to_arg.keys():
                if name == arg:
                    self.__attached_func_to_arg[name]()
                    return [True, self.__attached_func_to_arg[name]]
        return False

    def parse_args(self):
        self.__parsed_args = self.__args[1:]

    def get_parsed_args(self) -> List[str]:
        return self.__parsed_args

    def add_command(self, name: str, func: Callable):
        self.__attached_func_to_arg[name] = func

    def run(self):
        self.parse_args()
        for arg in self.__parsed_args:
            if arg in self.__attached_func_to_arg:
                self.__attached_func_to_arg[arg]()
