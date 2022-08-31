import Sword;
from fastapi import APIRouter, Response;
from .lib.factory import Factory;
from .lib.module import Module;

router = APIRouter();

@router.get('/{repo}/{mod}')
async def get_Module(response: Response, repo: str, mod: str, key: str = None):
    mgr = Factory.getRepository(repo);
    mod = mgr.getModule(mod);
    
    if mod is not None:
        mod = Factory.fromModule(mod);

        if key is not None:
            mod.key = key;
            
        return dict(mod);
    
    response.status_code = 404;
    return None;
