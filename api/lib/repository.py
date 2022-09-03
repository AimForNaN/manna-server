import Sword;
from .module import Module;

class Repository():
    def __init__(self, mgr: Sword.SWMgr):
        self.swmgr = mgr;

    def __iter__(self):
        mgr = self.swmgr;
        yield('Modules', [dict(mod) for mod in self.getModules()]);
        yield('Path', mgr.prefixPath);

    def getModules(self):
        mgr = self.swmgr;
        modules = [];
        for name, mod in mgr.getModules().items():
            mod = Module(mod);
            modules.append(mod);

        return modules;