# src/engine/metrics_engine.py

from src.metrics.basic import BasicStats
from src.metrics.distribution import DistributionMetric
from src.metrics.categories import CategoryMetric

class MetricsEngine:

    def __init__(self):
        self.metrics = [
            BasicStats(),
            DistributionMetric(),
            CategoryMetric(),
        ]

    def run(self, df, schema):
        results = {}

        for metric in self.metrics:
            name = metric.__class__.__name__
            results[name] = metric.compute(df, schema)

        return results