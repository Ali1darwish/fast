from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Netlify!"}

handler = Mangum(app)
