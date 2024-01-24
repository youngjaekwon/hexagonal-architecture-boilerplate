import uvicorn

from app.dependency.db import get_engine
from app.domain.entity.article import Article
from app.domain.entity.base import Base

if __name__ == "__main__":
    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        proxy_headers=True,
        forwarded_allow_ips="*",
    )
