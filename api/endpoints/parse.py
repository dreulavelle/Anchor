from fastapi import APIRouter, HTTPException, Query
from utils.logger import get_logger
from api.models.ptn import PTN
import os

logger = get_logger(__name__, level=os.environ.get('LOG_LEVEL', 'INFO'))
router = APIRouter()

@router.get("/parse",
            response_model=PTN,  # Using PTN class directly as response model
            tags=["Parsing"], 
            summary="Parse Torrent Filename",
            description="Parses a torrent filename to extract details like resolution, audio, HDR, codec, and extras.")
async def parse_filename(filename: str = Query(..., example="Good.Trouble.S01.1080p.DTS-HD.MA.7.1.x264-GalaxyTV[TGx]")):
    logger.info(f"Parsing filename: {filename}")
    parsed_data = PTN(filename=filename)
    return parsed_data
