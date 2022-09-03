import Sword;
from fastapi import APIRouter, Response;
from pydantic import BaseModel;

from .lib.factory import Factory;
from .lib.repository import Repository;

router = APIRouter();

class InstallModuleModel(BaseModel):
    Name: str;
    Source: str;

class InstallSourceModel(BaseModel):
    Source: str;

@router.get('/{repo}/install')
async def get_Install(response: Response, repo: str):
    """Retrieve install sources."""
    ret = [];
    repo = Factory.getRepository(repo);
    if repo is not None:
        install = Factory.getInstall(repo);
        sources = install.sources.items();

        if not len(sources):
            result = install.refreshRemoteSourceConfiguration();

            if result: # Non-zero result is an error!
                response.status_code = 500;
            else:
                sources = install.sources.items();

        if not len(sources):
            response.status_code = 204;
        else:
            for caption,source in sources:
                mgr = Repository(source.getMgr());
                ret.append({
                    'Location': str(source.source),
                    'Modules': mgr.getModules(),
                    'Source': str(caption),
                    'Type': str(source.type),
                });

    return ret;

@router.post('/{repo}/install')
async def post_Install(response: Response, repo: str, mod: InstallModuleModel):
    """Install module from remote source."""
    repo = Factory.getRepository(repo);
    if repo is not None:
        install = Factory.getInstall(repo);
        sources = install.sources.items();

        try:
            source = sources[mod.Source];
            result = install.installModule(repo, None, mod.Name, source);
            if result: # Non-zero result is an error!
                response.status_code = 500;
            else:
                return;
        except:
            pass;
            
    response.status_code = 422;

@router.patch('/{repo}/install')
async def patch_Install(response: Response, repo: str, source: InstallModuleModel):
    """Refresh remote source cache."""
    repo = Factory.getRepository(repo);
    if repo is not None:
        install = Factory.getInstall(repo);
        sources = install.sources.items();

        try:
            source = sources[source.Source];
            result = install.refreshRemoteSource(source);
            if result: # Non-zero result is an error!
                response.status_code = 500;
            else:
                return;
        except:
            pass;

    response.status_code = 422;
