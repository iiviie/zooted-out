# Reddit Scraper API

A FastAPI-based service for scraping Reddit data using the official Reddit API.

## Features

- Get posts from any subreddit (hot, new, top, rising)
- Search posts within a subreddit
- Configurable post limit
- Docker support

## Project Structure

```
app/
├── api/
│   └── routes.py          # API endpoints
├── config/
│   └── settings.py        # Configuration settings
├── models/
│   └── ...               # Database models (if needed)
├── schemas/
│   └── reddit.py         # Pydantic models
├── services/
│   └── reddit_service.py # Reddit scraping logic
└── main.py              # FastAPI application
```

## Prerequisites

1. Python 3.11+
2. Reddit API credentials (client ID and client secret)
   - Create a Reddit account
   - Go to https://www.reddit.com/prefs/apps
   - Create a new application (script)
   - Note down the client ID and client secret

## Setup and Running

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Reddit API credentials
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

### Using Docker

1. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Reddit API credentials
```

2. Build the Docker image:
```bash
docker build -t reddit-scraper .
```

3. Run the container:
```bash
docker run -p 8000:8000 --env-file .env reddit-scraper
```

The API will be available at http://localhost:8000

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI) at http://localhost:8000/docs
- Alternative API documentation (ReDoc) at http://localhost:8000/redoc

## Available Endpoints

### GET /api/v1/reddit/{subreddit}
Get posts from a subreddit
- Parameters:
  - subreddit: Name of the subreddit
  - category: Sort category (hot, new, top, rising)
  - limit: Number of posts to retrieve (1-100)

### POST /api/v1/reddit/{subreddit}/search
Search posts in a subreddit
- Parameters:
  - subreddit: Name of the subreddit
  - search_request:
    - query: Search query
    - sort: Sort method (relevance, hot, top, new, comments)
    - limit: Number of posts to retrieve (1-100)

## Security Note

Make sure to never commit your `.env` file containing Reddit API credentials. The `.env.example` file is provided as a template. 