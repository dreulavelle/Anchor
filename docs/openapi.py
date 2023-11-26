from fastapi.openapi.utils import get_openapi

def anchor_api(app):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Anchor API",
        version="1.0.0",
        description="API Documentation for Anchor",
        routes=app.routes,
        tags=[{"name": "symlink", "description": "Operations with symlinks."}],
        # You can add more metadata here as needed.
    )

    app.openapi_schema = openapi_schema
    return app.openapi_schema
