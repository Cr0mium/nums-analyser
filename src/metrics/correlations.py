# src/metrics/correlations.py

import pandas as pd
from typing import List, Dict
from .base import Metric



class CorrelationMetric(Metric):
    def __init__(self, threshold: float = 0.3):
        self.threshold = threshold
    
    def compute(self, df: pd.DataFrame, schema) -> List[Dict]:
        def get_strength(value):
            v = abs(value)
            if v >= 0.9:
                return "very strong"
            elif v >= 0.7:
                return "strong"
            elif v >= 0.5:
                return "moderate"
            else:
                return "weak"
        numeric_cols = schema.numeric_cols

        if len(numeric_cols) < 2:
            return [{"message": "Not enough numeric columns for correlation"}]

        corr_matrix = pd.DataFrame(df[numeric_cols]).corr()

        results = []
        cols = corr_matrix.columns

        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                col1 = cols[i]
                col2 = cols[j]

                value = corr_matrix.loc[col1, col2]

                if pd.isna(value):
                    continue

                # filter weak correlations
                results.append({
                    "col1": col1,
                    "col2": col2,
                    "value": float(round(value, 3)),
                    "type": "positive" if value > 0 else "negative",
                    "strength": get_strength(value),
                })

        return results