from pydantic import BaseModel
from typing import List, Optional
from .common import Review, Keyword, Stream, Rating, WatchProvider


class MDBMetadata(BaseModel):
    title: str
    year: int
    released: str
    description: str
    runtime: int
    score: int
    score_average: int
    imdbid: str
    traktid: int
    tmdbid: int
    type: str
    ratings: List[Rating] = None
    streams: List[Stream] = None
    watch_providers: List[WatchProvider] = None
    reviews: List[Review] = None
    keywords: List[Keyword] = None
    language: str
    spoken_language: str
    country: str
    certification: str
    commonsense: Optional[int] = None
    age_rating: Optional[int] = None
    status: str
    trailer: Optional[str] = None
    poster: str
    backdrop: str
    response: bool
    apiused: int

class MovieSymlinkRequest(BaseModel):
    filename: str
    imdb_id: str
    library_name: str
