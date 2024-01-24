from typing import Type

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.dependency.db import get_db
from app.domain import entity, schema
from app.port.outbound.repository.article import ArticleCRUDRepositoryPort


class ArticleCRUDRepositoryAdapter(ArticleCRUDRepositoryPort):
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    async def fetch_article_by_id(self, id: int) -> entity.Article:
        try:
            return self.db.execute(
                select(entity.Article).where(entity.Article.id == id)
            ).first()
        except NoResultFound:
            raise Exception

    async def fetch_articles(self) -> list[Type[entity.Article]]:
        return (
            self.db.query(entity.Article).order_by(entity.Article.id.desc()).all()
        )

    async def create_article(
        self, article_create: schema.ArticleCreate
    ) -> entity.Article:
        return entity.Article(**article_create.model_dump())

    async def update_article(
        self, article: entity.Article, article_update: schema.ArticleUpdate
    ) -> entity.Article:
        for k, v in article_update.model_dump().items():
            if v is not None and hasattr(article, k) and getattr(article, k) != v:
                setattr(article, k, v)
        return article

    async def delete_article(self, article: entity.Article) -> None:
        self.db.delete(article)
