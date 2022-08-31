import Sword;
from .module import Module;

class Repository():
    def __init__(self, mgr: Sword.SWMgr):
        self.swmgr = mgr;

    def __iter__(self):
        mgr = self.swmgr;
        yield('modules', [dict(Module(mod)) for mod in self.getModules()]);
        yield('path', mgr.configPath);

    def getModules(self):
        mgr = self.swmgr;
        modules = [];
        for name, mod in mgr.getModules().items():
            modules.append(mod);

        return modules;