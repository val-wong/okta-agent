from fastapi import FastAPI
from scripts.api import router as api_router

app = FastAPI(
    title="Okta Terraform Agent API",
    version="1.0.0",
    description="REST API for triggering Terraform generation from Okta SSO data.",
)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {
        "message": "👋 Welcome to the Okta Terraform Agent API!",
        "docs": "Visit /docs to explore the API",
        "example": "/generate?url=...&group=..."
    }
