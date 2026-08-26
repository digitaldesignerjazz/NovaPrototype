#!/usr/bin/env python3
"""hello-nova — first public tick of NovaPrototype."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.contract import Prototype, PrototypeStatus


class HelloNova(Prototype):
    name = "hello-nova"

    def __init__(self) -> None:
        self._ticks = 0

    def status(self) -> PrototypeStatus:
        return PrototypeStatus(
            name=self.name,
            healthy=True,
            message="NovaPrototype public sandbox is live.",
            reading={"ticks": self._ticks, "node": "hannover"},
        )

    def tick(self) -> PrototypeStatus:
        self._ticks += 1
        return self.status()


def main() -> None:
    proto = HelloNova()
    state = proto.tick()
    print(f"[{state.name}] healthy={state.healthy} ticks={state.reading['ticks']}")
    print(state.message)


if __name__ == "__main__":
    main()
