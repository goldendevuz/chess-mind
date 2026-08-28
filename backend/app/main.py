from fastapi import FastAPI


app = FastAPI(title="ChessMind API")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

