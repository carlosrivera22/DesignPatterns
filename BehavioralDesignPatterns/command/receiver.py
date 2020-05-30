from __future__ import annotations

class Receiver:

    def do_something(self, a: str) -> None:
        print()
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print()
        print(f"\nReceiver: Also working on ({b}.)", end="")


