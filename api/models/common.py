from pydantic import BaseModel
from typing import Optional

class Review(BaseModel):
    updated_at: Optional[str] = None
    author: str
    rating: Optional[int] = None
    provider_id: int
    content: str

class Keyword(BaseModel):
    id: int
    name: str

class Stream(BaseModel):
    id: int
    name: str

class Rating(BaseModel):
    source: str
    value: Optional[float] = None
    score: Optional[int] = None
    votes: Optional[int] = None
    popular: Optional[int] = None
    url: Optional[str] = None

class WatchProvider(BaseModel):
    id: int
    name: str