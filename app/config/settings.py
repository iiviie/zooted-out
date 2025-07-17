from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Reddit API Settings
    REDDIT_CLIENT_ID: str
    REDDIT_CLIENT_SECRET: str
    REDDIT_USER_AGENT: str = "RedditScraperBot/1.0"
    
    # API Settings
    API_V1_PREFIX: str = "/api/v1"
    
    class Config:
        env_file = ".env"
        case_sensitive = True 