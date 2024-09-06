from fastapi import FastAPI
from Demo.api.routers.items_routers import item_router

app = FastAPI()

app.include_router(item_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
