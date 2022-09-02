import asyncio;
from hypercorn.asyncio import serve;
from hypercorn.config import Config;
from fastapi import FastAPI, Response;
from fastapi.middleware.cors import CORSMiddleware;
from fastapi.responses import HTMLResponse;

# HACK: Apparently, makes relative imports work!? Useful for testing, at least!
__package__ = __name__;

from api import install, modules, repositories;
from api.lib.config import MannaConfig;

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
);

app.include_router(install.router);
app.include_router(modules.router);
app.include_router(repositories.router);

@app.get('/', response_class=HTMLResponse)
async def get_Index(response: Response):
    response.status_code = 422;

if __name__ == '__main__':
    ini = MannaConfig();

    hc = ini.get('hypercorn', {});
    config = Config();
    config.from_mapping(hc);
    # from_mapping doesn't handle properties!
    config.bind = hc.get('bind', ["localhost:4815"]);

    asyncio.run(serve(app, config));
