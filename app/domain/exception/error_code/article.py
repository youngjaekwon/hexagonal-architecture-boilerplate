from enum import IntEnum, Enum

from app.domain.exception.error_code.base import CustomError


class ErrorCodeEnum(IntEnum):
    ARTICLE_LIST_READ_FAILED = 1000
    ARTICLE_LIST_READ_FAILED2 = 1001


class ErrorMessagesEnum(str, Enum):
    ARTICLE_LIST_READ_FAILED = "failed to read article list"
    ARTICLE_LIST_READ_FAILED2 = "failed to read article list2"


class ArticleError(CustomError[ErrorCodeEnum, ErrorMessagesEnum]):
    pass
