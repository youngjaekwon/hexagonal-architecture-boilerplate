from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from app.domain.entity.base import Base


class Article(Base):
    __tablename__ = "article"
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = Column(String, nullable=False)
    content: Mapped[str] = Column(String, nullable=False)
