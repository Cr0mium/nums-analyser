# src/engine/metrics_engine.py

import pandas as pd

from backend.src.metrics.anomalies import AnomalyMetric
from backend.src.metrics.basic import BasicStats
from backend.src.metrics.categories import CategoryMetric
from backend.src.metrics.correlations import CorrelationMetric
from backend.src.metrics.distribution import DistributionMetric
from backend.src.metrics.trends import TrendMetric


class MetricsEngine:
    def __init__(self):
        self.metrics = [
            BasicStats(),
            DistributionMetric(),
            CategoryMetric(),
            CorrelationMetric(),
            TrendMetric(),
            AnomalyMetric(),
        ]

    def run(self, df, schema):
        results = {}
        for metric in self.metrics:
            name = metric.__class__.__name__
            results[name] = metric.compute(df, schema)

        from backend.src.utils.types import clean_dict, to_column_view

        results = clean_dict(results)
        final_results = to_column_view(results)

        from backend.src.insights.basic_insights import generate_insights

        final_results["insights"] = generate_insights(final_results)
        # print(results)
        corr_matrix = None

        numeric_cols = schema.numeric_cols

        if len(numeric_cols) >= 2:
            corr_matrix = df[numeric_cols].corr().round(3).to_dict()

        final_results["correlation_matrix"] = corr_matrix
        return final_results
