from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/square")
def square(x: float):
    return {"x": x, "x2": x*x}

@app.get("/")
def root():
    return {"ok": True}
