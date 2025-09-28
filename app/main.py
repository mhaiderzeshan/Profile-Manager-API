from fastapi import FastAPI
from app.routes import profiles
app = FastAPI(title="Profile Manager API")

app.include_router(profiles.router)


@app.get("/")
def root():
    return {"message": "Welcome to Profile Manager Crud API Project"}
