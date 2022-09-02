from pathlib import Path;
from fastapi import APIRouter, Body, Response;
from .lib.config import MannaConfig;
from .lib.factory import Factory;
from .lib.repository import Repository;

router = APIRouter();

@router.get('/{repo}/')
async def get_Repository(response: Response, repo: str):
    """Retrieve data on a local repository."""
    repo = Factory.getRepository(repo);
    if repo is not None:
        repo = Repository(repo);
        return dict(repo);
    else:
        response.status_code = 404;


@router.post('/{repo}/')
async def post_Repository(response: Response, repo: str, path: str = Body(embed=True)):
    """Register a local repository."""
    ini = MannaConfig();
    paths = ini.get('IncludePaths', []);
    modpath = Path(path, 'mods.d');

    for x in paths:
        x = Path(x).resolve();
        if not modpath.is_relative_to(x):
            response.status_code = 422;
            return;

    modpath.mkdir(parents=True, exist_ok=True);
    ini['Repositories'][repo] = path;
    ini.save();