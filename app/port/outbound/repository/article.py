import abc

from app.domain import entity, schema


class ArticleCRUDRepositoryPort(abc.ABC):
    @abc.abstractmethod
    async def fetch_article_by_id(self, article_id: int) -> entity.Article:
        pass

    @abc.abstractmethod
    async def fetch_articles(self) -> list[entity.Article]:
        pass

    @abc.abstractmethod
    async def create_article(
            self, article_create: schema.ArticleCreate
    ) -> entity.Article:
        pass

    @abc.abstractmethod
    async def update_article(
            self, article: entity.Article, article_update: schema.ArticleUpdate
    ) -> entity.Article:
        pass

    @abc.abstractmethod
    async def delete_article(self, article: entity.Article) -> None:
        pass
