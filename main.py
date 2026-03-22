from fastapi import FastAPI
from api.timur.courses import router

app = FastAPI()          # creezi aplicația
app.include_router(router)  # apoi incluzi routerul

@app.get("/")
def home():
    return {"message": "FastAPI works on Vercel!"}