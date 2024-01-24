from app.dependency.db import get_engine
from app.domain.entity import Article, Base

engine = get_engine()
tables = [Article.__table__]
Base.metadata.create_all(bind=engine, tables=tables)
