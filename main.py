from fastapi import FastAPI
from api.endpoints.symlink import router as symlink_router
from docs.openapi import anchor_api


tags_metadata = [
    {
        "name": "symlink",
        "description": "Operations with symlinks for media files.",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

app.openapi = lambda: anchor_api(app)
app.include_router(symlink_router)
