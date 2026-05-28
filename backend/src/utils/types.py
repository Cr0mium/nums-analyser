def to_python_type(x):
    """
    Convert numpy types to native Python types
    """
    if hasattr(x, "item"):
        return x.item()
    return x


def clean_dict(d):
    if isinstance(d, dict):
        return {k: clean_dict(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [clean_dict(v) for v in d]
    else:
        return to_python_type(d)
    

def to_column_view(results):

    column_results = {}

    global_correlations = []
    global_anomalies = []

    for metric_name, metric_data in results.items():

        # metrics that return dicts per-column
        if isinstance(metric_data, dict):

            for col, values in metric_data.items():

                if col not in column_results:
                    column_results[col] = {}

                column_results[col][metric_name] = values

        # special global metrics
        elif isinstance(metric_data, list):

            if metric_name == "CorrelationMetric":
                global_correlations.extend(metric_data)

            elif metric_name == "AnomalyMetric":
                global_anomalies.extend(metric_data)

    return {
        "columns": column_results,
        "correlations": global_correlations,
        "anomalies": global_anomalies
    }