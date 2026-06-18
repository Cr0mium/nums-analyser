# api/main.py

import json
import tempfile

import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.agents.graph import graph
from backend.src.chat.chat import chat
from backend.src.core.detector import detect_schema
from backend.src.engine.metrics_engine import MetricsEngine
from backend.storage.session_manager import session_manager

load_dotenv()

app = FastAPI(
    title="NumInsight API",
    description="LLM-powered CSV analytics engine",
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    with open("backend/experiments/output.json") as f:
        data = json.load(f)
    return data


@app.post("/analyze")
async def analyze_csv(file: UploadFile = File(...)):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            contents = await file.read()

            tmp.write(contents)

            temp_path = tmp.name

        # Load dataframe
        df = pd.read_csv(temp_path)

        # Detect schema
        schema = detect_schema(df, dataset_name=file.filename)
        # Compute metrics
        engine = MetricsEngine()

        analytics_result = engine.run(df, schema)

        # Initial graph state
        initial_state = {
            "df_json": df.to_json(),
            "schema": {
                "rows": schema.rows,
                "columns": schema.cols,
                "time_col": schema.time_col,
                "numeric_cols": schema.numeric_cols,
                "categorical_cols": schema.categorical_cols,
                "mode": schema.mode,
                # "dataset_name": file.filename,
            },
            "mode": schema.mode,
            "metrics": analytics_result,
            "insights": "",
            "response": "",
            "error": None,
            "query": "",
        }
        # Run LangGraph
        result = graph.invoke(initial_state)
        session_id = session_manager.create_session()
        session_manager.save_analysis(
            session_id,
            {
                "df_json": df.to_json(),
                "dataset": file.filename,
                "schema": result["schema"],
                "analytics": result["metrics"],
                "report": result["insights"],
            },
        )

        print(list(session_manager.sessions.keys()))
        return {
            "session_id": session_id,
            "dataset": file.filename,
            "schema": result["schema"],
            "mode": result["mode"],
            "analytics": result["metrics"],
            "response": result["response"],
            "report": result["insights"],
            "error": result["error"],
        }

    except Exception as e:
        import traceback

        traceback.print_exc()

        raise HTTPException(status_code=500, detail=str(e))


class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):

    session = session_manager.get_session(request.session_id)

    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    response = chat(session, request.message)

    return {"response": response}
