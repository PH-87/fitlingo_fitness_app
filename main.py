from fastapi import FastAPI

app = FastAPI(title="FITLINGO API")


@app.get("/")
def read_root():
    return {"message": "FITLINGO API가 살아있어요!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
