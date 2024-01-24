import uvicorn
from fastapi import FastAPI

from app.adapter.incoming.web.root import router

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

def create_app():
    app = FastAPI(description=description)
    app.include_router(router)


    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    return app


app = create_app()
