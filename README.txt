Budget Ally - Quick Start

Backend (Flask + SQLite)
------------------------
1. Open PowerShell and run:
	```powershell
	cd 'C:\Users\Ishan Patel\Downloads\Hackathon\Budget_Ally\Backend'
	python -m venv .venv
	. .\.venv\Scripts\Activate.ps1
	pip install -r requirements.txt
	python app.py
	```
	The backend will run at http://127.0.0.1:5000

Frontend (choose one)
---------------------
Option A: Static demo (no Node/npm required)
1. In a new PowerShell window:
	```powershell
	cd 'C:\Users\Ishan Patel\Downloads\Hackathon\Budget_Ally\Frontend'
	python -m http.server 5173
	```
2. Open http://localhost:5173/auth.html in your browser.

Option B: React app (requires Node/npm)
1. Install Node.js if not already installed (https://nodejs.org/en/download/)
2. In PowerShell:
	```powershell
	cd 'C:\Users\Ishan Patel\Downloads\Hackathon\Budget_Ally\Frontend'
	npm install
	npm run dev
	```
3. Open the URL printed by Vite (usually http://localhost:5173)

Features
--------
- Register and login forms (credentials stored in SQLite)
- After login, see a personalized Hello message
- Token-based authentication

For more details, see Backend/README.md and Frontend/README.md
Quick start

- Backend (Flask + SQLite):

	Open PowerShell and run:

	```powershell
	cd Backend; python -m venv .venv; . .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
	```

	The backend listens on http://localhost:5000.

- Frontend (React):

	From the project root or `Frontend` folder run your usual React commands (e.g. `npm install` then `npm start`). The sample `Frontend/src/App.js` fetches data from the backend at http://localhost:5000/api/items.
