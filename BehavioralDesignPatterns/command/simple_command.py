from __future__ import annotations
from command import Command

class SimpleCommand(Command):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print()
        print(f"SimpleCommand: I do simple things."
              f"({self._payload})")
