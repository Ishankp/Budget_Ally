This is a readme and a temp holder
 
Quick start

- Backend (Flask + SQLite):

	Open PowerShell and run:

	```powershell
	cd Backend; python -m venv .venv; . .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
	```

	The backend listens on http://localhost:5000.

- Frontend (React):

	From the project root or `Frontend` folder run your usual React commands (e.g. `npm install` then `npm start`). The sample `Frontend/src/App.js` fetches data from the backend at http://localhost:5000/api/items.
