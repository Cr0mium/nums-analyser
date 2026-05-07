# api/main.py

import os
import tempfile

import pandas as pd

from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv

from src.core.detector import detect_schema
from src.engine.metrics_engine import MetricsEngine
from src.llm.generator import OpenAIAnalyzer


load_dotenv()

app = FastAPI(
    title="NumInsight API",
    description="LLM-powered CSV analytics engine",
    version="0.1.0"
)


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "NumInsight API running"
    }


@app.post("/analyze")
async def analyze_csv(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are supported"
        )

    try:

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".csv"
        ) as tmp:

            contents = await file.read()
            tmp.write(contents)

            temp_path = tmp.name

        # Load dataframe
        df = pd.read_csv(temp_path)

        # Schema inference
        schema = detect_schema(
            df,
            dataset_name=file.filename
        )

        # Metrics engine
        engine = MetricsEngine()

        analytics_result = engine.run(
            df,
            schema
        )

        # LLM analysis
        analyzer = OpenAIAnalyzer(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        report = analyzer.analyze(
            analytics_result
        )

        return {
            "dataset": file.filename,
            "schema": {
                "time_col": schema.time_col,
                "numeric_cols": schema.numeric_cols,
                "categorical_cols": schema.categorical_cols,
                "mode": schema.mode
            },
            "analytics": analytics_result,
            "report": report
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )