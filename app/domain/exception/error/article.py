from enum import IntEnum, Enum

from app.domain.exception.error.base import BaseError


class ArticleErrorCodeEnum(IntEnum):
    ARTICLE_LIST_READ_FAILED = 1000
    ARTICLE_LIST_READ_FAILED2 = 1001


class ArticleErrorMessagesEnum(str, Enum):
    ARTICLE_LIST_READ_FAILED = "failed to read article list"
    ARTICLE_LIST_READ_FAILED2 = "failed to read article list2"


class ArticleError(BaseError[ArticleErrorCodeEnum, ArticleErrorMessagesEnum]):
    pass
