from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.services.reddit_service import RedditService
from app.schemas.reddit import SubredditResponse, SearchRequest, SubredditPost

reddit_router = APIRouter()
reddit_service = RedditService()

@reddit_router.get(
    "/reddit/{subreddit}",
    response_model=SubredditResponse,
    summary="Get posts from a subreddit"
)
async def get_subreddit_posts(
    subreddit: str,
    category: str = Query("hot", enum=["hot", "new", "top", "rising"]),
    limit: int = Query(10, ge=1, le=100)
):
    """
    Get posts from a specific subreddit.
    
    - **subreddit**: Name of the subreddit
    - **category**: Sort category (hot, new, top, rising)
    - **limit**: Number of posts to retrieve (1-100)
    """
    try:
        posts = reddit_service.get_subreddit_posts(
            subreddit_name=subreddit,
            category=category,
            limit=limit
        )
        return SubredditResponse(
            subreddit=subreddit,
            category=category,
            posts=posts
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@reddit_router.post(
    "/reddit/{subreddit}/search",
    response_model=SubredditResponse,
    summary="Search posts in a subreddit"
)
async def search_subreddit(
    subreddit: str,
    search_request: SearchRequest
):
    """
    Search for posts in a specific subreddit.
    
    - **subreddit**: Name of the subreddit
    - **search_request**: Search parameters
        - query: Search query
        - sort: Sort method (relevance, hot, top, new, comments)
        - limit: Number of posts to retrieve (1-100)
    """
    try:
        posts = reddit_service.search_subreddit(
            subreddit_name=subreddit,
            query=search_request.query,
            sort=search_request.sort,
            limit=search_request.limit
        )
        return SubredditResponse(
            subreddit=subreddit,
            category=f"search: {search_request.query}",
            posts=posts
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 