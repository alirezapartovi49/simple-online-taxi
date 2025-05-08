from fastapi import FastAPI

from .modules.user.routes import router as user_router


app = FastAPI(title="taxi online")
app.include_router(user_router)

@app.get("/", include_in_schema=False)
async def root():
    return "hello world!"
