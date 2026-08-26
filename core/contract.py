"""Shared contract for every NovaPrototype experiment."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class PrototypeStatus:
    name: str
    healthy: bool
    message: str
    reading: dict[str, Any] = field(default_factory=dict)
    observed_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


class Prototype(ABC):
    """Minimal loop every public experiment must implement."""

    name: str

    @abstractmethod
    def status(self) -> PrototypeStatus:
        """Health plus last reading. Must never raise."""

    @abstractmethod
    def tick(self) -> PrototypeStatus:
        """One iteration of the experiment loop."""
