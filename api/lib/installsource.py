import Sword

from api.lib.module import Module

from .factory import Factory;
from .repository import Repository;

Statuses = {
    1: 'outdated',
    2: 'installed',
    4: 'update',
    8: 'new',
    18: '',
    24: '',
    56: '',
};

class InstallRemoteSource():
    def __init__(self, source: Sword.InstallSource, repo: Sword.SWMgr):
        self.source = source;
        self.repo = repo;

    def __iter__(self):
        source = self.source;
        ret = {
            'Location': str(source.source),
            'Modules': [dict(mod) for mod in self.getModules()],
            'Source': str(source.caption),
            'Type': str(source.type),
        };

        for x,y in ret.items():
            yield(x, y);

    def getModules(self):
        ret = [];
        mgr = self.source.getMgr();
        install = Factory.getInstall(self.repo);
        diff = install.getModuleStatus(self.repo, mgr);
        for x,y in diff.items():
            x = Module(x);
            x.Status = Statuses[y];
            ret.append(x)

        ret.sort(key=lambda mod: mod.getName());
        return ret;