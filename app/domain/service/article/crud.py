from fastapi import Depends
from sqlalchemy.orm import Session

from app.adapter.outbound.repository.article import ArticleCRUDRepositoryAdapter
from app.dependency.db import get_db
from app.domain import schema
from app.port.incoming.usecase.article.crud import ArticleCRUDUsecase
from app.port.outbound.repository.article import ArticleCRUDRepositoryPort


class ArticleCRUDService(ArticleCRUDUsecase):
    def __init__(
        self,
        db: Session = Depends(get_db),
        article_crud_repository: ArticleCRUDRepositoryPort = Depends(ArticleCRUDRepositoryAdapter),
    ):
        self.db = db
        self.article_crud_repository = article_crud_repository

    async def read_articles(self) -> list[schema.Article]:
        results = await self.article_crud_repository.fetch_articles()
        return [schema.Article.model_validate(article) for article in results]

    async def read_article(self, article_id: int) -> schema.Article:
        article = await self.article_crud_repository.fetch_article_by_id(article_id)
        return schema.Article.model_validate(article)

    async def create_article(
        self, article_create: schema.ArticleCreate
    ) -> schema.Article:
        article = await self.article_crud_repository.create_article(article_create)
        self.db.add(article)
        self.db.commit()
        return schema.Article.model_validate(article)

    async def update_article(
        self, article_id: int, article_update: schema.ArticleUpdate
    ) -> schema.Article:
        article = self.article_crud_repository.fetch_article_by_id(article_id)
        article = await self.article_crud_repository.update_article(article, article_update)
        self.db.commit()
        return schema.Article.model_validate(article)

    async def delete_article(self, article_id: int) -> None:
        article = await self.article_crud_repository.fetch_article_by_id(article_id)
        await self.article_crud_repository.delete_article(article)
        self.db.commit()
