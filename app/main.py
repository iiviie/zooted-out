from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import reddit_router
from app.config.settings import Settings

settings = Settings()
app = FastAPI(title="Reddit Scraper API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(reddit_router, prefix="/api/v1", tags=["reddit"])

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 