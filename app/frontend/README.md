# Frontend Setup

This folder contains a Streamlit frontend for the existing FastAPI backend.

## Run the frontend

1. Install dependencies:
   ```bash
   pip install -r app/frontend/requirements.txt
   ```
2. Start the backend if it is not already running:
   ```bash
   uvicorn app.backend.main:app --reload
   ```
3. Launch the frontend from the project root:
   ```bash
   streamlit run app/frontend/app.py
   ```

The UI sends prediction requests to http://127.0.0.1:8000/predict.
