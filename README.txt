CDC-MAS -  Clinical Decision Support- Multi-Agent System
1. Project Overview


CDS-MAS is an AI-powered Clinical Decision Support System (CDSS) designed for low-resource healthcare settings. The platform combines Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and a multi-agent workflow to assist healthcare professionals with patient triage, evidence-based clinical guidance, and automated clinical documentation.

The system is intended to support—not replace—clinical decision making. It generates recommendations based on patient information and medical knowledge while leaving final decisions to qualified healthcare professionals.

2. Key Features

Multi-agent AI workflow
Clinical triage support
Evidence-based knowledge retrieval (RAG)
Automated clinical note generation
Offline-capable local LLM inference
REST API
Modern React frontend
Modular architecture
PostgreSQL / SQLite support
ChromaDB vector search
3. System Architecture
reports/system_architecture_diagram
docs/images/system_architecture_diagram

4. Technology Stack
Component	Technology
Frontend	React + TypeScript + Tailwind CSS
Backend	FastAPI
AI Workflow	LangGraph
Language Model	Phi-3 / Llama (Ollama)
Vector Database	ChromaDB
Database	PostgreSQL / SQLite
ORM	SQLAlchemy
Documentation	pdoc / Sphinx
Testing	Pytest
Deployment	Docker (planned)
5. Repository Structure


CDS-MAS/

├── ai/
│   ├── agents/
│   ├── models/
│   ├── services/
│   ├── workflows/
│   └── rag/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── models/
│   │   └── main.py
│
├── frontend/
│
├── tests/
│
├
│
├── docs/
│
└── README.md

6. Installation
Clone
git clone https://github.com/simplazbluda/CDS-MAS.git


Create environment
python -m venv newvenv

Activate

Windows

newvenv\Scripts\activate

Install
Dependencies: requirements.txt
pip install -r requirements.txt

7. Running the Backend
uvicorn backend.app.main:app --reload

Swagger

http://localhost:8000/docs

8. Running the Frontend
cd frontend

npm install

npm run dev
9. Running the Tests
pytest

Generate HTML report

pytest --html=reports/tests.html --self-contained-html
10. API Endpoints

Endpoint	Description
POST /clinical/workflow	Runs complete AI workflow
GET /patients	Retrieve patients
POST /patients	Register patient
11. AI Workflow

The workflow.

Patient

↓

Clinical API

↓

Workflow Engine

↓

Triage Agent

↓

Knowledge Agent

↓

Documentation Agent

↓

Clinical Recommendation

12. Dataset

Current Dataset

The prototype currently uses:

Synthetic patient encounters
Public clinical guideline documents
WHO guidance
NICE guidelines
Open medical literature

Future Datasets

Zimbabwe Ministry of Health clinical protocols
MIMIC-IV (licensed)
PhysioNet
Hospital EMR integrations

13. Documentation

Generated using

pdoc

Documentation
Visit the folder: 
docs/ai
docs/index

14. Database Schema

reports/database_schema.png

15. Future Work
Offline-first Android application
Voice-based consultation
Multilingual support
Hospital interoperability (FHIR)
Explainable AI
Clinical audit dashboard

16. Contributors

Lead Developer

Simplicio Bachelor Sithole

Medical Expert 

Dr Tafadzwa Chadenganga

17. License

MIT License