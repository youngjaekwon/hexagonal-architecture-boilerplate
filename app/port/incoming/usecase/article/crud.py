import abc

from app.domain import schema


class ArticleCRUDUsecase(abc.ABC):
    @abc.abstractmethod
    async def read_articles(self) -> list[schema.Article]:
        pass

    @abc.abstractmethod
    async def read_article(self, article_id: int) -> schema.Article:
        pass

    @abc.abstractmethod
    async def create_article(
            self, article_create: schema.ArticleCreate
    ) -> schema.Article:
        pass

    @abc.abstractmethod
    async def update_article(
            self, article_id: int, article_update: schema.ArticleUpdate
    ) -> schema.Article:
        pass

    @abc.abstractmethod
    async def delete_article(self, article_id: int) -> None:
        pass
