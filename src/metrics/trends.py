# src/metrics/trends.py

import pandas as pd
import numpy as np
from typing import Dict
from .base import Metric


class TrendMetric(Metric):
    def __init__(self, window: int = 3):
        self.window = window

    def compute(self, df: pd.DataFrame, schema) -> Dict:
        time_col = schema.time_col
        numeric_cols = schema.numeric_cols

        if not time_col:
            return {"message": "No time column detected"}

        if not numeric_cols:
            return {"message": "No numeric columns for trend analysis"}

        # sort by time
        df_sorted = df.sort_values(by=time_col)

        results = {}

        for col in numeric_cols:
            series = df_sorted[col].dropna()

            if len(series) < self.window:
                continue

            # rolling average
            rolling_series = series.rolling(window=self.window).mean().dropna()

            if len(rolling_series) < 2:
                continue

            # use smoothed values instead of raw
            change = rolling_series.iloc[-1] - rolling_series.iloc[0]

            # percentage change
            if rolling_series.iloc[0] != 0:
                pct_change = (change / abs(rolling_series.iloc[0])) * 100
            else:
                pct_change = None

            # direction
            if change > 0:
                direction = "increasing"
            elif change < 0:
                direction = "decreasing"
            else:
                direction = "stable"

            results[col] = {
                "direction": direction,
                "change": round(change, 3),
                "pct_change": round(pct_change, 2) if pct_change is not None else None,
                "method": f"rolling_avg_window_{self.window}"
            }

        return results