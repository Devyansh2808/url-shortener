# URL Shortener API

A REST API to convert long URLs into short, shareable links with click tracking built with FastAPI.

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

Interactive API documentation: `http://127.0.0.1:8000/docs`

## Features

- Create shortened URLs from long links
- Automatic redirect with click tracking
- View all shortened URLs
- Get details about specific shortened URLs
- Delete shortened URLs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/shorten` | Create a new shortened URL |
| GET | `/s/{short_url}` | Redirect to original URL and track clicks |
| GET | `/urls` | List all shortened URLs |
| GET | `/urls/{short_url}` | Get details of a specific shortened URL |
| DELETE | `/urls/{short_url}` | Delete a shortened URL |

## Examples

### Create a shortened URL

```bash
POST /shorten

Request body:
{
  "original_url": "https://www.github.com/some/very/long/repository/path/that/is/annoying/to/share"
}

Response:
{
  "original_url": "https://www.github.com/some/very/long/repository/path/that/is/annoying/to/share",
  "short_url": "aBc7Xy",
  "created_at": "2026-05-06T12:30:45.123456",
  "clicks": 0
}
```

### Redirect to original URL

Visit `http://127.0.0.1:8000/s/aBc7Xy` in your browser — you'll be redirected to the original URL and the click count will increase.

### View all shortened URLs

```bash
GET /urls

Response:
[
  {
    "original_url": "https://www.github.com/...",
    "short_url": "aBc7Xy",
    "created_at": "2026-05-06T12:30:45.123456",
    "clicks": 5
  },
  ...
]
```

### Get details of a specific shortened URL

```bash
GET /urls/aBc7Xy

Response:
{
  "original_url": "https://www.github.com/...",
  "short_url": "aBc7Xy",
  "created_at": "2026-05-06T12:30:45.123456",
  "clicks": 5
}
```

### Delete a shortened URL

```bash
DELETE /urls/aBc7Xy

Response: Returns the deleted URL object
```

## How it works

- Each shortened URL gets a random 6-character code
- The original URL is stored and retrieved when someone clicks the short link
- Click counts are incremented each time the short URL is accessed
- All data is stored in memory (resets when the server restarts)