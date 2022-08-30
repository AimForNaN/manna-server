import uvicorn;
from fastapi import FastAPI, Response;
from fastapi.middleware.cors import CORSMiddleware;
from fastapi.responses import HTMLResponse;

from api import modules;

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
);

app.include_router(modules.router);

@app.get('/', response_class=HTMLResponse)
async def get_Index(response: Response):
    response.status_code = 422;

if __name__ == '__main__':
    uvicorn.run('main:app', port=4815, log_level='info');
