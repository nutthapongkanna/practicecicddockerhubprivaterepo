from fastapi import FastAPI

app = FastAPI(title="Python Docker CI/CD Demo")

@app.get("/")
def root():
    return {"message": "hello from fastapi", "status": "ok"}

@app.get("/healthz")
def healthz():
    return {"ok": True}
