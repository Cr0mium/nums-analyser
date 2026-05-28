🧠 AI Data Intelligence System

An LLM-powered analytics platform that automatically analyzes CSV datasets, detects patterns, identifies anomalies, and generates structured natural-language insights.

Built using Python, FastAPI, LangGraph, OpenAI, and Ollama.

⸻

🚀 Overview

This project implements an AI-driven analytics workflow with:

* Automatic schema inference
* Dataset mode detection
* Trend analysis
* Correlation analysis
* Anomaly detection
* Agentic planning using LangGraph
* Hybrid LLM architecture (Local + Cloud)
* Structured AI-generated reports
* FastAPI inference service

⸻

🧩 System Architecture

CSV Dataset
    ↓
Schema Inference
    ↓
Mode Detection & Routing
    ↓
Analytics Pipeline
 ├── Trends
 ├── Correlations
 ├── Anomalies
 └── Summary Metrics
    ↓
Planner Agent (Ollama)
    ↓
LLM Report Synthesis (OpenAI)
    ↓
Structured Analytics Report

⸻

⚙️ Features

🧠 Intelligent Analytics Pipeline

* Automatic schema inference
* Dataset-aware routing
* Statistical analysis pipeline
* Structured analytics generation
* AI-powered insight synthesis

⸻

📈 Trend Analysis

* Rolling average trend computation
* Percentage trend change detection
* Time-series behavior analysis

⸻

🔗 Correlation Analysis

* Pearson correlation analysis
* Positive/negative relationship detection
* Correlation strength classification
* Top insight extraction

⸻

🚨 Anomaly Detection

* Z-score based anomaly detection
* Outlier severity classification
* Direction-aware anomaly tagging

⸻

🤖 Agentic Workflow with LangGraph

Graph-based orchestration for:

* routing
* analytics execution
* planning
* report generation

⸻

🧩 Hybrid LLM Architecture

Local LLMs (Ollama)

Used for:

* planning
* prioritization
* lightweight reasoning

Cloud LLMs (OpenAI)

Used for:

* structured report synthesis
* insight generation
* high-quality summarization

This hybrid setup reduces cost while preserving report quality.

⸻

🌐 FastAPI Service

Endpoints

* /analyze → analyze uploaded CSV dataset

⸻

🛠️ Tech Stack

* Python
* FastAPI
* Pandas
* NumPy
* LangGraph
* OpenAI API
* Ollama
* Gemma

⸻

📦 Project Structure

.
├── agents/
│   ├── graph.py
│   ├── router.py
│   ├── state.py
│   └── nodes/
│       ├── anomalies.py
│       ├── correlations.py
│       ├── trends.py
│       ├── summary.py
│       ├── planner_agent.py
│       ├── llm_analysis.py
│       ├── general_mode.py
│       └── personal_mode.py
│
├── api/
│   └── main.py
│
├── src/
│   ├── core/
│   │   └── detector.py
│   │
│   └── llm/
│       ├── llm_analyser.py
│       ├── openai_client.py
│       ├── ollama_client.py
│       ├── prompt_builder.py
│       └── prompts.py
│
└── README.md

⸻

⚙️ Setup

1. Clone Repository

git clone <your-repo-url>
cd <repo-name>

⸻

2. Create Environment

conda create -n numanalyser python=3.11
conda activate numanalyser

⸻

3. Install Dependencies

pip install -r requirements.txt

⸻

4. Environment Variables

Create .env:

OPENAI_API_KEY=your_openai_key

⸻

🦙 Ollama Setup

Install Ollama:

urlOllama Official Websitehttps://ollama.com

Pull model:

ollama pull gemma4:e2b

Run Ollama:

ollama serve

⸻

🚀 Run API

uvicorn api.main:app --reload

API runs at:

http://127.0.0.1:8000

⸻

🧪 Example API Request

curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "file=@test.csv"

⸻

📊 Example Insights

Screen time strongly negatively correlates with productivity.
Calories and screen time are highly correlated.
Workout frequency positively impacts productivity.
Detected severe low-sleep anomaly.

⸻

📌 Current Capabilities

* Structured analytics pipeline
* Multi-node LangGraph orchestration
* Local + cloud LLM integration
* Automatic insight generation
* AI-generated markdown reports
* Dataset-aware routing
* Modular agent architecture

⸻

⚡ Key Learnings

* Structured analytics improves LLM reasoning quality
* Hybrid local/cloud LLM pipelines reduce operational cost
* Planner agents improve report prioritization
* LangGraph enables modular AI workflow orchestration
* Statistical preprocessing significantly improves report quality

⸻

🔮 Future Improvements

* Visualization layer
* Interactive frontend
* PDF report export
* Conversational analytics
* Multi-dataset comparison
* Streaming analytics
* Memory-aware workflows

⸻

📌 Notes

* Ollama used for local lightweight planning
* OpenAI used for final high-quality synthesis
* Designed for extensibility and experimentation
* Built with modular analytics agents

⸻

👨‍💻 Author

Built as part of a hands-on AI systems and data intelligence engineering journey.

⸻

📄 License

MIT License