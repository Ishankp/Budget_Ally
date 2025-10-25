Budget Ally - Quick Start

How to run (Windows / PowerShell)
================================

1) Backend (Flask + SQLite)
---------------------------
Open PowerShell, go to the Backend folder, create & activate a venv, install deps, and start the app:

```powershell
cd 'C:\Users\Ishan Patel\Downloads\Hackathon\Budget_Ally\Backend'
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

The backend listens on http://localhost:5000 (or http://127.0.0.1:5000).

2) Frontend — two options
-------------------------

Option A — Quick static demo (no Node/npm required)

```powershell
cd 'C:\Users\Ishan Patel\Downloads\Hackathon\Budget_Ally\Frontend'
python -m http.server 5173
```

Open: http://localhost:5173/auth.html

This serves the static `auth.html` demo which uses the backend endpoints directly.

Option B — React app (recommended for development)

Prerequisite: Node.js (includes npm). Download/install from https://nodejs.org/ if you haven't.

In PowerShell:

```powershell
cd 'C:\Users\Ishan Patel\Downloads\Hackathon\Budget_Ally\Frontend'
npm install
npm run dev
```

Open the URL printed by Vite (usually http://localhost:5173/) — open the root URL to load the React app (index.html → src/main.jsx → App).

Troubleshooting tips
--------------------
- If `npm` or `node` is not recognized, close and re-open PowerShell after installing Node.js, or reinstall Node and make sure Add to PATH is selected.
- If `npm install` fails with peer dependency errors, run:

```powershell
npm install --legacy-peer-deps
```

I adjusted `package.json` to use a Vite 4.x release compatible with the installed `@vitejs/plugin-react`. If you still see issues, paste the terminal errors here and I will fix them.

Verifying the React app
-----------------------
- The React entry is `index.html` (loads `/src/main.jsx`) and mounts into `<div id="root"></div>`.
- If you see a blank page or the UI loads then disappears, stop the dev server, close editors that might hold files, then run `npm run dev` again and check the browser console and the terminal logs for errors.

Features
--------
- Register and login forms (credentials stored in SQLite)
- After login, see a personalized Hello message
- Token-based authentication

If you'd like, I can also add one-line Run commands to PowerShell scripts or provide a small BAT file to start backend + frontend together.
