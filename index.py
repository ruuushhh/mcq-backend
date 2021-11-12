from fastapi import FastAPI
from routes.mcq import mcq

app = FastAPI()
app.include_router(mcq)
