def generate_insights(results):
    insights = []

    correlations = results.get("correlations", [])
    # # sort strongest first

    correlations = sorted(correlations, key=lambda x: abs(x["value"]), reverse=True)


    for c in correlations[:5]:  # top 3
        col1 = c["col1"]
        col2 = c["col2"]
        strength = c["strength"]
        direction = c["type"]

        insights.append(
            f"{col1} and {col2} show a {strength} {direction} correlation ({c['value']})"
        )

    return insights