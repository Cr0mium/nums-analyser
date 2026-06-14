# src/core/detector.py

from typing import List, Optional

import pandas as pd

from .schema import Schema

PERSONAL_COLUMNS = {
    "sleep",
    "workout",
    "mood",
    "focus",
    "productivity",
    "calories",
    "steps",
    "morning_page",
    "daylight",
    "journal",
}


def detect_time_column(df: pd.DataFrame) -> Optional[str]:
    for col in df.columns:
        try:
            parsed = pd.to_datetime(df[col], errors="coerce")
            if parsed.notna().sum() > 0.8 * len(df):
                return col
        except:
            continue
    return None


def detect_numeric_columns(df: pd.DataFrame) -> List[str]:
    return df.select_dtypes(include=["number"]).columns.tolist()


def detect_categorical_columns(df: pd.DataFrame, threshold: int = 20) -> List[str]:
    categorical_cols = []
    for col in df.columns:
        if df[col].dtype == "object":
            if df[col].nunique() <= threshold:
                categorical_cols.append(col)
    return categorical_cols


def detect_mode(columns: List[str]) -> str:
    cols_lower = {col.lower() for col in columns}
    if cols_lower & PERSONAL_COLUMNS:
        return "personal"
    return "general"


def detect_schema(df: pd.DataFrame, dataset_name: str | None = None) -> Schema:
    time_col = detect_time_column(df)
    numeric_cols = detect_numeric_columns(df)
    categorical_cols = detect_categorical_columns(df)

    # remove overlaps
    if time_col in numeric_cols:
        numeric_cols.remove(time_col)
    if time_col in categorical_cols:
        categorical_cols.remove(time_col)
    # mode=
    rows, cols = df.shape

    return Schema(
        rows=rows,
        cols=cols,
        time_col=time_col,
        numeric_cols=numeric_cols,
        categorical_cols=categorical_cols,
        mode=detect_mode(df.columns),
        dataset_name=dataset_name,
    )
