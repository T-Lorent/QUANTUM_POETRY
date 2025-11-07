from fastapi import FastAPI

# Create the FastAPI app with default docs enabled and OpenAPI version 3.0.0
app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}