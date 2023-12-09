from typing import Dict, Optional
from pydantic import BaseModel

class LibraryConfig(BaseModel):
    default_movie: Optional[bool] = None
    default_show: Optional[bool] = None
    type: str = 'movie'
    anime: bool = False
    hdr: Optional[bool] = None
    remux: Optional[bool] = None
    kids: Optional[bool] = None
    regex: Optional[str] = None

class SortRequest(BaseModel):
    filename: str
    imdb_id: str

class Config(BaseModel):
    libraries: Dict[str, LibraryConfig]
