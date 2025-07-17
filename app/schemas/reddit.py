from pydantic import BaseModel
from typing import Optional

class SubredditPost(BaseModel):
    id: str
    title: str
    author: str
    url: str
    score: int
    num_comments: int
    created_utc: float
    selftext: str
    is_self: bool

class SubredditResponse(BaseModel):
    subreddit: str
    category: str
    posts: list[SubredditPost]

class SearchRequest(BaseModel):
    query: str
    sort: Optional[str] = "relevance"
    limit: Optional[int] = 10 