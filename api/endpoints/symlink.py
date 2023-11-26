from fastapi import APIRouter, HTTPException
from api.models.movies import MovieSymlinkRequest
from api.models.series import SeriesSymlinkRequest
from api.mdbapi import fetch_movie_metadata
from api.mdbapi import fetch_series_metadata
from utils.logger import get_logger
import os


logger = get_logger(__name__, level=os.environ.get('LOG_LEVEL', 'INFO'))
router = APIRouter()

# Fetch mount paths from environment variables
RCLONE_DIR = os.environ.get('RCLONE_DIR', '/mnt/rclone')
SYMLINK_DIR = os.environ.get('SYMLINK_DIR', '/mnt/symlink')

@router.post("/symlink/movie", tags=["symlink"])
async def create_movie_symlink(request: MovieSymlinkRequest):
    logger.info(f"Creating movie symlink for {request.filename}")
    source_file_path = None

    # Search for the file in the rclone directory
    for root, dirs, files in os.walk(RCLONE_DIR):
        if request.filename in files:
            source_file_path = os.path.join(root, request.filename)
            break

    # Before raising an exception
    if not source_file_path:
        logger.error(f"File not found in source path: {request.filename}")
        raise HTTPException(status_code=404, detail="File not found in source path")

    # Fetch metadata from MDBList
    metadata = await fetch_movie_metadata(request.imdb_id)

    # New title for the symlink
    new_title = f"{metadata.title} ({metadata.year}) {{{metadata.imdbid}}}"

    # Library and child folder paths, child folder named after new title
    library_path = os.path.join(SYMLINK_DIR, request.library_name)
    child_folder_path = os.path.join(library_path, new_title)

    # Ensure the library and child folder exist
    os.makedirs(child_folder_path, exist_ok=True)

    # Define the destination path with the file extension
    destination = os.path.join(child_folder_path, new_title + os.path.splitext(request.filename)[1])

    # Check if the symlink already exists and remove it if so
    if os.path.exists(destination) or os.path.islink(destination):
        os.remove(destination)

    # Create the symlink
    try:
        os.symlink(source_file_path, destination)
        logger.info(f"Successfully created symlink: {destination}")
        return {"status": "success", "source": source_file_path, "destination": destination}
    except OSError as e:
        logger.exception(f"Error creating symlink: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/symlink/series", tags=["symlink"])
async def create_series_symlink(request: SeriesSymlinkRequest):
    logger.info(f"Creating series symlink for {request.filename}")
    
    # Fetch series metadata from MDBList
    metadata = await fetch_series_metadata(request.imdb_id)

    # Define the parent folder name
    parent_folder_name = f"{metadata.title} ({metadata.year}) {{{metadata.imdbid}}}"
    parent_folder_path = os.path.join(SYMLINK_DIR, parent_folder_name)

    # Ensure the parent folder exists
    os.makedirs(parent_folder_path, exist_ok=True)

    # Define the symlink destination with the original folder/file name
    destination = os.path.join(parent_folder_path, os.path.basename(request.filename))

    # Create the symlink
    try:
        source_file_path = os.path.join(RCLONE_DIR, request.filename)
        os.symlink(source_file_path, destination)
        logger.info(f"Successfully created series symlink: {destination}")
        return {"status": "success", "source": source_file_path, "destination": destination}
    except OSError as e:
        logger.exception(f"Error creating series symlink: {e}")
        raise HTTPException(status_code=500, detail=str(e))
