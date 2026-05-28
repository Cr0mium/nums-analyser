# src/metrics/categories.py

from .base import Metric

class CategoryMetric(Metric):

    def compute(self, df, schema):
        result = {}

        for col in schema.categorical_cols:
            result[col] = df[col].value_counts().to_dict()

        return result