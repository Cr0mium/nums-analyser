# src/main.py

from src.core.loader import load_csv
from src.core.detector import detect_schema
from src.engine.metrics_engine import MetricsEngine
import json

def main():
    df = load_csv("input/data.csv")

    schema = detect_schema(df)

    print("Schema:")
    print(schema)

    engine= MetricsEngine()
    res=engine.run(df,schema)
    with open("output/output.json", "w") as f:
        json.dump(res, f, indent=2)

if __name__ == "__main__":
    main()