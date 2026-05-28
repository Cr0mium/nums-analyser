# src/engine/metrics_engine.py

from backend.src.metrics.basic import BasicStats
from backend.src.metrics.distribution import DistributionMetric
from backend.src.metrics.categories import CategoryMetric
from backend.src.metrics.correlations import CorrelationMetric
from backend.src.metrics.trends import TrendMetric
from backend.src.metrics.anomalies import AnomalyMetric

class MetricsEngine:

    def __init__(self):
        self.metrics = [
            BasicStats(),
            DistributionMetric(),
            CategoryMetric(),
            CorrelationMetric(),
            TrendMetric(),
            AnomalyMetric()
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
        return final_results
            


    