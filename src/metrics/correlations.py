# src/metrics/correlations.py

import pandas as pd
from typing import Dict
from .base import Metric


class CorrelationMetric(Metric):
    def __init__(self, threshold: float = 0.3):
        self.threshold = threshold

    def compute(self, df: pd.DataFrame, schema) -> Dict:
        numeric_cols = schema.numeric_cols

        # Not enough columns for correlation
        if len(numeric_cols) < 2:
            return {"message": "Not enough numeric columns for correlation"}

        corr_matrix = pd.DataFrame(df[numeric_cols]).corr()

        results = {}
        positive_corrs = {}
        negative_corrs = {}

        cols = corr_matrix.columns

        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                col = cols[i]
                other_col = cols[j]

                value = corr_matrix.loc[col, other_col]

                # skip NaNs
                if pd.isna(value):
                    continue

                # filter weak correlations

                if value >= self.threshold:
                    positive_corrs[other_col] = round(value, 3)

                elif value <= -self.threshold:
                    negative_corrs[other_col] = round(value, 3)

                if positive_corrs or negative_corrs:    
                    results[col]={
                        "positive":positive_corrs,
                        "negative":negative_corrs
                    }

        return results