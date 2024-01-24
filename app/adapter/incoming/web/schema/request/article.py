from pydantic import BaseModel


class RequestArticleCreate(BaseModel):
    title: str
    content: str
