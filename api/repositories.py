from fastapi import APIRouter, Body, Response;
from .lib.factory import Factory;
from .lib.module import Module;
from .lib.repository import Repository;

router = APIRouter();

@router.get('/{repo}/')
async def get_Repository(response: Response, repo: str):
    repo = Factory.getRepository(repo);
    if repo is not None:
        repo = Repository(repo);
        return dict(repo);
    else:
        response.status_code = 404;


@router.post('/{repo}/')
async def post_Repository(response: Response, repo: str, path: str = Body(embed=True)):
    pass;