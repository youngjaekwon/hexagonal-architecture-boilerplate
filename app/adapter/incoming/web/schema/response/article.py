from pydantic import BaseModel


class ResponseArticle(BaseModel):
    id: int
    title: str
    content: str
