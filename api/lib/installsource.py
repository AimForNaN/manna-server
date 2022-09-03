import Sword;
from .repository import Repository;

class InstallRemoteSource():
    def __init__(self, source: Sword.InstallSource):
        self.source = source;

    def __iter__(self):
        source = self.source;
        mgr = Repository(source.getMgr());
        ret = {
            'Location': str(source.source),
            'Modules': [dict(mod) for mod in mgr.getModules()],
            'Source': str(source.caption),
            'Type': str(source.type),
        };

        for x,y in ret.items():
            yield(x, y);