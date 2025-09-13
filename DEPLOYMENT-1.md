
# Deployment Instructions for Steele's Casino 777 Backend

## Files
- app.py: Main Flask server
- requirements.txt: Python dependencies

## Deploying to Render
1. Go to https://render.com
2. Create a new Web Service
3. Connect your GitHub repo with these files
4. Set the start command to: `python app.py`
5. Choose Python environment and set build command: `pip install -r requirements.txt`

## Deploying to Replit
1. Go to https://replit.com
2. Create a new Python Repl
3. Upload app.py and requirements.txt
4. Open the Shell and run: `pip install -r requirements.txt`
5. Click "Run" to start the server

## API Endpoints
- POST /api/login → {email, password}
- GET /api/wallet?email=...
- POST /api/slot → {email, bet_amount}
