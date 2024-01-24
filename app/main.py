import uvicorn
from fastapi import FastAPI

from app.adapter.incoming.web.root import router


def create_app():
    app = FastAPI()
    app.include_router(router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app


app = create_app()
