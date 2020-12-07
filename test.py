from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel

Sum = Literal[1, 2]


@dataclass
class Base:
    literal: Sum


class What(BaseModel):
    base: Base


What(base=Base(literal=1))
