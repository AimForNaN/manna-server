import Sword;
from fastapi import APIRouter, Response;
from .lib.factory import Factory;
from .lib.module import Module;

router = APIRouter();

@router.get('/{repo}/')
async def get_Modules(response: Response, repo: str):
    mgr = Factory.getRepository(repo);
    modules = [];
    for name, mod in mgr.getModules().items():
        modules.append(dict(Module(mod)));

    if len(modules) == 0:
        response.status_code = 204;

    return modules;

@router.get('/{repo}/{mod}')
async def get_Module(response: Response, repo: str, mod: str, key: str = None):
    mgr = Factory.getRepository(repo);
    mod = mgr.getModule(mod);
    
    if mod is not None:
        mod = Factory.fromModule(mod);
        return dict(mod);
    
    response.status_code = 404;
    return None;
