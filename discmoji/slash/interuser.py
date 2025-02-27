from typing import Self

class InteractionInput:
    """Represents one user param input.
    ## NOTE
    This object usually fills in an input into your callback for a slash command, but you can use this class for special uses."""
    def __init__(self,_dict: dict):
        self.name: str = _dict["name"]
        self.value: float | str | int | str | bool | None = _dict.get("value")
        self.options: list[Self] = [self(option) for option in _dict["options"]] if _dict.get("options") else None
        self.focused: bool | None = _dict.get("focused")
