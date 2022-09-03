import asyncio;
from hypercorn.asyncio import serve;
from hypercorn.config import Config;
from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;

from .config import MannaConfig;
from .. import index, install, modules, repositories;

class Server():
    def __init__(self):
        self.App = FastAPI();

        self.App.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        );

        self.App.include_router(index.router);
        self.App.include_router(install.router);
        self.App.include_router(modules.router);
        self.App.include_router(repositories.router);

    def run(self):
        ini = MannaConfig();

        hc = ini.get('hypercorn', {});
        config = Config();
        config.from_mapping(hc);
        # from_mapping doesn't handle properties!
        config.bind = hc.get('bind', ["localhost:4815"]);

        asyncio.run(serve(self.App, config));