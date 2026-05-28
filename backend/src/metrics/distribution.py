# src/metrics/distribution.py

from .base import Metric

class DistributionMetric(Metric):

    def compute(self, df, schema):
        result = {}

        for col in schema.numeric_cols:
            result[col] = {
                "median": df[col].median(),
                "q1": df[col].quantile(0.25),
                "q3": df[col].quantile(0.75),
            }

        return result