# src/metrics/anomalies.py

import pandas as pd
from typing import Dict, List
from .base import Metric


class AnomalyMetric(Metric):

    def __init__(self, threshold: float = 2.0):
        self.threshold = threshold

    def compute(self, df: pd.DataFrame, schema) -> List[Dict]:

        numeric_cols = schema.numeric_cols

        if not numeric_cols:
            return []

        results = []

        for col in numeric_cols:

            series = df[col].dropna()
            # skip constant columns
            if series.std() == 0:
                continue

            mean = series.mean()
            std = series.std()
            for idx, value in series.items():
                z_score = (value - mean) / std
                # anomaly check
                if abs(z_score) >= self.threshold:
                    # severity
                    if abs(z_score) >= 3:
                        severity = "high"
                    else:
                        severity = "moderate"

                    # direction
                    if value > mean:
                        direction = "above_mean"
                    else:
                        direction = "below_mean"

                    results.append({
                        "column": col,
                        "index": idx,
                        "value": round(float(value), 3),
                        "mean": round(float(mean), 3),
                        "z_score": round(float(z_score), 3),
                        "severity": severity,
                        "direction": direction
                    })

        # strongest anomalies first
        results = sorted(
            results,
            key=lambda x: abs(x["z_score"]),
            reverse=True
        )

        return results