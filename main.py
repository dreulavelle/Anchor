from fastapi import FastAPI
from api.endpoints import symlink, parse
from docs.openapi import anchor_api


tags_metadata = [
    {
        "name": "symlink",
        "description": "Operations with symlinks for media files.",
    }
]

app = FastAPI(openapi_tags=tags_metadata)
app.openapi = lambda: anchor_api(app)

# Include routers from endpoints
app.include_router(symlink.router)
app.include_router(parse.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Anchor API"}