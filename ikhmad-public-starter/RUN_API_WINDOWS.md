# Run IKHMAD Public API on Windows

These instructions assume Windows and Python 3.11+.

## 1. Open the repository folder

In File Explorer, open the IKHMAD repository.

Right-click an empty area and choose **Open in Terminal**.

## 2. Create a virtual environment

```powershell
py -m venv .venv
```

## 3. Activate it

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## 5. Run automated tests

```powershell
pytest
```

You should see all tests pass.

## 6. Start the API

```powershell
uvicorn src.main:app --reload
```

## 7. Open the API documentation

In your browser:

- Swagger UI: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

## Suggested manual demo

Use Swagger UI to:

1. `POST /api/v1/incidents`
2. `GET /api/v1/incidents`
3. `PATCH /api/v1/incidents/{incident_id}/status`
4. `POST /api/v1/alerts`
5. `POST /api/v1/sos`
6. `GET /api/v1/sos`

This creates a real local technical demonstration of the public-safe IKHMAD workflow.

## Important

This API:
- uses memory only;
- loses data when restarted;
- has no real authentication;
- has no production authorization;
- has no proprietary decision engine;
- is not an emergency-service production system.
