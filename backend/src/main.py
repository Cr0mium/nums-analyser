# src/main.py

import os
import json
import pandas as pd

from dotenv import load_dotenv

from backend.src.core.detector import detect_schema
from backend.src.engine.metrics_engine import MetricsEngine
from backend.src.llm.llm_analyser import OpenAIAnalyzer


load_dotenv()


df = pd.read_csv("input/data.csv")

schema = detect_schema(df=df)

engine = MetricsEngine()

results = engine.run(df, schema)

analyzer = OpenAIAnalyzer(
    api_key=os.getenv("OPENAI_API_KEY")
)

report = analyzer.analyze(results)

print(report)