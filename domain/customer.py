from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Customer:
id: int
name: str
birth_date: date
email: Optional[str] = None


def age(self, as_of: date = date.today()) -> int:
born = self.birth_date
age = as_of.year - born.year - ((as_of.month, as_of.day) < (born.month, born.day))
return age