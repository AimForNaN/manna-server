import Sword;
from fastapi import APIRouter, Response

from api.lib.repository import Repository

from .lib.factory import Factory;

router = APIRouter();

@router.get('/{repo}/install')
async def get_Install(response: Response, repo: str):
    """Retrieve install sources."""
    ret = [];
    repo = Factory.getRepository(repo);
    if repo is not None:
        install = Factory.getInstall(repo);
        sources = install.sources.items();

        if len(sources) == 0:
            install.refreshRemoteSourceConfiguration();
            sources = install.sources.items();

        for caption,source in sources:
            mgr = Repository(source.getMgr());
            ret.append({
                'Name': str(caption),
                'Modules': mgr.getModules(),
                'Source': str(source.source),
                'Type': str(source.type),
            });

    return ret;