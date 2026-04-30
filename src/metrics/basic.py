# src/metrics/basic.py

from .base import Metric

class BasicStats(Metric):

    def compute(self, df, schema):
        result = {}

        for col in schema.numeric_cols:
            result[col] = {
                "mean": df[col].mean(),
                "std": df[col].std(),
                "min": df[col].min(),
                "max": df[col].max(),
            }

        return result