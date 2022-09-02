from fastapi import APIRouter, Response;
from fastapi.responses import HTMLResponse;

router = APIRouter();

@router.get('/', response_class=HTMLResponse)
async def get_Index(response: Response):
    response.status_code = 422;