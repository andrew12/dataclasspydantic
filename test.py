from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel


@dataclass
class Base:
    literal: Literal[1, 2]


class What(BaseModel):
    base: Base


What(base=Base(literal=1))
