# Backend (Flask + SQLite)

Quick instructions to run the backend locally.

Prerequisites
- Python 3.10+ installed

Create a virtual environment, install requirements, and run:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
```

The API will be available at http://localhost:5000. Endpoints:
- GET /api/items
- GET /api/items/<id>
- POST /api/items  (JSON body: {name, amount, category})
- PUT /api/items/<id>
- DELETE /api/items/<id>
