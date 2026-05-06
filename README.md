# URL Shortener API

A simple REST API to shorten long URLs and track click counts built with FastAPI.

## Setup

1. Clone the repo and navigate to the project directory
2. Create a virtual environment:
```bash
   python -m venv venv
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

## Running the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Interactive docs: `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/shorten` | Create a shortened URL |
| GET | `/s/{short_url}` | Redirect to original URL (increments clicks) |
| GET | `/urls` | List all shortened URLs |
| GET | `/urls/{short_url}` | Get details of a shortened URL |
| DELETE | `/urls/{short_url}` | Delete a shortened URL |

## Creating a shortened URL

Send a POST request to `/shorten` with:
```json
{
  "original_url": "https://www.example.com/very/long/url/path"
}
```

Response:
```json
{
  "original_url": "https://www.example.com/very/long/url/path",
  "short_url": "abc123",
  "created_at": "2026-05-06T12:00:00",
  "clicks": 0
}
```

## Using the shortened URL

Visit `http://127.0.0.1:8000/s/abc123` in your browser — it will redirect to the original URL and increment the click counter.

## Getting URL details

Check how many times a shortened URL has been clicked: