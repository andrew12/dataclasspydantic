from __future__ import annotations

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from pydantic.typing import Literal


@dataclass
class Base:
    literal: Literal[1, 2]


class What(BaseModel):
    base: Base


What(base=Base(literal=1))
