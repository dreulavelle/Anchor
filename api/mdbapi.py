import httpx
from api.models.movies import MDBMetadata
from api.models.series import SeriesMDBMetadata
from pydantic import ValidationError
import os


MDB_API_KEY = os.environ.get('MDB_API_KEY', None)

async def fetch_movie_metadata(imdb_id: str) -> MDBMetadata:
    url = f"https://mdblist.com/api/?apikey={MDB_API_KEY}&i={imdb_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        try:
            return MDBMetadata(**response.json())
        except ValidationError as e:
            print(f"Validation error: {e}")
            return None

async def fetch_series_metadata(imdb_id: str) -> SeriesMDBMetadata:
    url = f"https://mdblist.com/api/?apikey={MDB_API_KEY}&i={imdb_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        try:
            return SeriesMDBMetadata(**response.json())
        except ValidationError as e:
            print(f"Validation error: {e}")
            return None