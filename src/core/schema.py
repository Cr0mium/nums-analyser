# src/core/schema.py

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Schema:
    time_col: Optional[str]
    numeric_cols: List[str]
    categorical_cols: List[str]