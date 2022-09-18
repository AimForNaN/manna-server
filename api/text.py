from fastapi import APIRouter, Response;
from .lib.factory import Factory;

router = APIRouter();

@router.get('/{repo}/{mod}/text')
async def get_Module(response: Response, repo: str, mod: str, key: str):
    mgr = Factory.getRepository(repo);
    mod = mgr.getModule(mod);
    
    if mod is not None:
        mod = Factory.fromModule(mod);
        mod.setKey(key);
        return mod.getText();
    
    response.status_code = 404;
    return [];
