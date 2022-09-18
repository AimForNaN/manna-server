import asyncio;
from hypercorn.asyncio import serve;
from hypercorn.config import Config;
from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;

from .config import MannaConfig;
from .. import index, install, modules, repositories, structure, text;

class Server():
    def __init__(self):
        self.App = FastAPI();
        self.Config = MannaConfig();

        self.App.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        );

        self.App.include_router(index.router);

        if self.Config['Permissions']['InstallManager']:
            self.App.include_router(install.router);

        self.App.include_router(modules.router);
        self.App.include_router(structure.router);
        self.App.include_router(text.router);
        self.App.include_router(repositories.router);

    def run(self):
        hc = self.Config.get('hypercorn', {});
        config = Config();
        config.from_mapping(hc);
        # from_mapping doesn't handle properties!
        config.bind = hc.get('bind', ["localhost:4815"]);

        asyncio.run(serve(self.App, config));