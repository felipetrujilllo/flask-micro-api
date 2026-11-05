# Flask Micro-API

A minimal Flask JSON API built using Agile sprints (see `BACKLOG.md`).

## Endpoints
| Method | Route | Description |
|---|---|---|
| GET | `/` | Lists available endpoints |
| GET | `/hello` | Returns a welcome message |
| GET | `/data` | Returns sample items |
| POST | `/data` | Adds an item (`{"name": "...", "price": 0}`); `name` is required |

## Setup and run
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
The server runs at http://127.0.0.1:5001. Port 5001 is used because macOS reserves port 5000 for AirPlay.

## Test
With the server running, open a second terminal and run:
```bash
python test_api.py
```

Note: data is stored in memory and resets when the server restarts.
