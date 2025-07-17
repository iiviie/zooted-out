from typing import List, Optional
import praw
from praw.models import Submission, Subreddit

from app.config.settings import Settings
from app.schemas.reddit import SubredditPost

class RedditService:
    def __init__(self):
        settings = Settings()
        self.reddit = praw.Reddit(
            client_id=settings.REDDIT_CLIENT_ID,
            client_secret=settings.REDDIT_CLIENT_SECRET,
            user_agent=settings.REDDIT_USER_AGENT
        )
    
    def get_subreddit_posts(
        self,
        subreddit_name: str,
        limit: int = 10,
        category: str = "hot"
    ) -> List[SubredditPost]:
        """
        Get posts from a specific subreddit.
        
        Args:
            subreddit_name: Name of the subreddit
            limit: Number of posts to retrieve
            category: One of 'hot', 'new', 'top', 'rising'
        
        Returns:
            List of posts from the subreddit
        """
        subreddit: Subreddit = self.reddit.subreddit(subreddit_name)
        
        if category == "hot":
            posts = subreddit.hot(limit=limit)
        elif category == "new":
            posts = subreddit.new(limit=limit)
        elif category == "top":
            posts = subreddit.top(limit=limit)
        elif category == "rising":
            posts = subreddit.rising(limit=limit)
        else:
            raise ValueError(f"Invalid category: {category}")
        
        return [
            SubredditPost(
                id=post.id,
                title=post.title,
                author=post.author.name if post.author else "[deleted]",
                url=post.url,
                score=post.score,
                num_comments=post.num_comments,
                created_utc=post.created_utc,
                selftext=post.selftext,
                is_self=post.is_self,
            )
            for post in posts
        ]
    
    def search_subreddit(
        self,
        subreddit_name: str,
        query: str,
        limit: int = 10,
        sort: str = "relevance"
    ) -> List[SubredditPost]:
        """
        Search for posts in a specific subreddit.
        
        Args:
            subreddit_name: Name of the subreddit
            query: Search query
            limit: Number of posts to retrieve
            sort: One of 'relevance', 'hot', 'top', 'new', 'comments'
        
        Returns:
            List of posts matching the search query
        """
        subreddit: Subreddit = self.reddit.subreddit(subreddit_name)
        posts = subreddit.search(query, limit=limit, sort=sort)
        
        return [
            SubredditPost(
                id=post.id,
                title=post.title,
                author=post.author.name if post.author else "[deleted]",
                url=post.url,
                score=post.score,
                num_comments=post.num_comments,
                created_utc=post.created_utc,
                selftext=post.selftext,
                is_self=post.is_self,
            )
            for post in posts
        ] 