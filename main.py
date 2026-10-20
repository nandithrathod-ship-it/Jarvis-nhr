from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "JARVIS Backend is live and running"}
