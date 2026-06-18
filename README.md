# 🧠 AI Data Intelligence System

An LLM-powered analytics platform that transforms raw CSV datasets into structured insights through automated statistical analysis, agentic workflows, and natural language reporting.

Built using **Python, FastAPI, LangGraph, OpenAI, and Ollama**.

---

# 🚀 Overview

The system implements an AI-driven analytics workflow consisting of:

- Automatic schema inference
- Dataset classification and routing
- Statistical trend analysis
- Correlation discovery
- Anomaly detection
- Agentic planning using LangGraph
- Hybrid local + cloud LLM reasoning
- Structured insight generation
- Conversational analytics interface

---

# 🧩 System Architecture

```text
CSV Dataset
      |
      v
Schema Inference
      |
      v
Dataset Routing
      |
      v
Analytics Pipeline
 ├── Summary Metrics
 ├── Trend Analysis
 ├── Correlation Analysis
 └── Anomaly Detection
      |
      v
Planner Agent (Ollama)
      |
      v
Report Synthesis (OpenAI)
      |
      v
Structured Analytics Report
```

---

# ⚙️ Core Features

## 📊 Statistical Analytics Engine

- Automatic dataset schema detection
- Numerical and business-oriented data analysis
- Structured analytics aggregation
- Dataset-aware processing pipelines

---

## 📈 Trend Analysis

- Rolling average trend computation
- Percentage growth and decline detection
- Time-series behavior analysis

---

## 🔗 Correlation Analysis

- Pearson correlation computation
- Positive and negative relationship detection
- Correlation strength classification
- High-impact insight extraction

---

## 🚨 Anomaly Detection

- Z-score based outlier detection
- Severity classification
- Direction-aware anomaly explanations

---

## 🤖 Agentic Workflow with LangGraph

Graph-based orchestration for:

- Dataset routing
- Analytics execution
- Planning and prioritization
- Report generation

---

# 🧠 Hybrid LLM Architecture

## Local Models (Ollama)

Used for:

- Analytics planning
- Finding high-priority insights
- Lightweight reasoning

## Cloud Models (OpenAI)

Used for:

- High-quality report synthesis
- Natural language explanations
- Structured business insights

This hybrid architecture reduces API cost while maintaining high-quality output.

---

# 🌐 API Service

## Available Endpoints

### Analyze Dataset

```
POST /analyze
```

Uploads a CSV file and returns:

- Schema information
- Statistical analytics
- AI-generated summary report

---

# 🛠️ Tech Stack

| Category          | Technologies      |
| ----------------- | ----------------- |
| Languages         | Python            |
| Backend           | FastAPI           |
| Data Processing   | Pandas, NumPy     |
| LLM Orchestration | LangGraph         |
| LLM Providers     | OpenAI, Ollama    |
| Local Models      | Gemma             |
| Frontend          | React, TypeScript |

---

# 📁 Project Structure

```text
.
├── backend/
│   ├── agents/
│   │   ├── graph.py
│   │   ├── router.py
│   │   ├── state.py
│   │   └── nodes/
│   │       ├── trends.py
│   │       ├── correlations.py
│   │       ├── anomalies.py
│   │       ├── summary.py
│   │       ├── planner_agent.py
│   │       └── llm_analysis.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── llm/
│   │   ├── openai_client.py
│   │   ├── ollama_client.py
│   │   └── prompts.py
│
├── frontend/
│   ├── components/
│   └── services/
│
└── README.md
```

---

# ⚙️ Setup

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

---

## 2. Create Environment

```bash
conda create -n ai-data-intelligence python=3.11
conda activate ai-data-intelligence
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# 🦙 Ollama Setup

Install Ollama.

Pull the Gemma model:

```bash
ollama pull gemma4:e2b
```

Start the Ollama server:

```bash
ollama serve
```

---

# 🚀 Running the Application

## Start Backend

```bash
uvicorn api.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

## Example API Request

```bash
curl -X POST "http://127.0.0.1:8000/analyze" \
     -F "file=@sample_dataset.csv"
```

---

# 📌 Current Capabilities

- Automated CSV analytics
- Multi-stage LangGraph workflows
- Hybrid local/cloud LLM pipeline
- AI-generated analytical reports
- Interactive conversational analytics
- Modular and extensible architecture

---

# 📚 Key Engineering Learnings

- Structured statistical preprocessing improves LLM reasoning accuracy
- Separating planning from generation improves insight prioritization
- Hybrid local/cloud architectures reduce inference cost
- Graph-based workflows improve modularity and extensibility
- Domain-aware prompts improve analytical quality

---

# 🔮 Future Improvements

- PostgreSQL/SQLite session persistence
- Conversation history and memory management
- Advanced domain-specific routing
- Data visualization dashboard
- PDF report generation
- Multi-dataset comparison

---

# 📄 License

MIT License
