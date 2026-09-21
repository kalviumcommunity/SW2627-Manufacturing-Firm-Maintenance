from fastapi import FastAPI

app = FastAPI(
    title="Manufacturing Floor Assistant API",
    description="Backend scaffold for the Manufacturing Floor Assistant.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
