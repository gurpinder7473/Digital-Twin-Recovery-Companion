# Digital-Twin Recovery Companion — Backend (Hackathon Deliverable)

This repository contains a complete backend scaffold for the **Digital-Twin Recovery Companion**:
a modular FastAPI-based backend with AI/ML stubs, authentication, ingestion endpoints, database schemas,
Docker support and a Streamlit demo.

> NOTE: This is a scaffold intended for hackathon use and local testing. For production/hospital deployment,
> follow the README sections about HIPAA compliance, managed DBs, and secure cloud deployment.

## Contents
- `app/` — FastAPI application code (routers, models, db, ml stubs).
- `alembic/` — Alembic skeleton for DB migrations.
- `docker-compose.yml` & `Dockerfile` — Containerization for local testing.
- `requirements.txt` — Python dependencies.
- `streamlit_app.py` — Optional Streamlit demo for predictions and visualization.
- `scripts/init_db.py` — Initialize local DB and create admin user.
- `.env.example` — Environment variables example.

## Quickstart (local)
1. Install Python 3.9+ and create a venv:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. For local quick testing we use SQLite by default. Initialize DB:
   ```bash
   python scripts/init_db.py
   ```
3. Run FastAPI:
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Visit docs at `http://127.0.0.1:8000/docs`

## Docker (optional)
Run with Docker Compose (Postgres):
```bash
docker-compose up --build
```
This will start the API and a PostgreSQL container.

## Streamlit Demo
To run the optional demo:
```bash
streamlit run streamlit_app.py
```

## Notes for Judges / Reviewers
- The AI model provided is a stub (PyTorch skeleton) for inference and demonstration. Replace with trained models later.
- OpenSim simulator calls are stubbed; replace with actual OpenSim integration for biomechanics simulation.
- This scaffold includes role-based JWT auth, ingestion endpoints for sensor data, a simulation endpoint, and sample DB models for patients and clinicians.
