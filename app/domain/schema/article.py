from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True


class ArticleCreate(BaseModel):
    title: str
    content: str


class ArticleUpdate(BaseModel):
    title: str | None
    content: str | None
