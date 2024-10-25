import sys
from typing import Callable, Dict, List, Union

class CLI:
    def __init__(self):
        self.args = sys.argv
        self.attached_func_to_arg: Dict[str, Callable] = {}

    def cli_cmd(self, name: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.attached_func_to_arg[name] = func
            return func
        return decorator

    def is_cmd_invoked(self) -> Union[List[Union[bool, Callable]], bool]:
        for arg in self.args:
            if arg in self.attached_func_to_arg:
                self.attached_func_to_arg[arg]()
                return [True, self.attached_func_to_arg[arg]]
        return False
