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
    return modules;

@router.get('/{repo}/{mod}')
async def get_Module(response: Response, repo: str, mod: str, key: str = None):
    mgr = Factory.getRepository(repo);
    mod = mgr.getModule(mod);
    if mod is not None:
        return dict(Factory.fromModule(mod));
    return None;
