from fastapi import APIRouter

from app.adapter.incoming.web import article

router = APIRouter()
router.include_router(article.router, prefix="/article", tags=["article"])
