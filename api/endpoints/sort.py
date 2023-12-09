from fastapi import APIRouter, HTTPException
from api.models.sort import SortRequest, Config
from api.models.ptn import PTN
import yaml
import os

router = APIRouter()

def load_config():
    with open("config.yml", "r") as f:
        return Config(**yaml.safe_load(f))

@router.post("/sort")
async def sort_media(request: SortRequest):
    config = load_config()
    parsed_data = PTN(filename=request.filename)

    # Default libraries
    default_movie_library = None
    default_show_library = None

    # Check for only one default movie and show library
    for library_name, library_config in config.libraries.items():
        if library_config.default_movie:
            if default_movie_library:
                raise HTTPException(status_code=400, detail="Multiple default movie libraries found")
            default_movie_library = library_name
        if library_config.default_show:
            if default_show_library:
                raise HTTPException(status_code=400, detail="Multiple default show libraries found")
            default_show_library = library_name

    # Validate that defaults are set
    if not default_movie_library or not default_show_library:
        raise HTTPException(status_code=400, detail="Default movie or show library not set")

    # Logic to determine the library
    # Use parsed_data and other metadata to determine the right library
    # This is a simplified example
    library = default_movie_library if parsed_data.type == 'movie' else default_show_library

    return {"filename": request.filename, "sorted_to": library}