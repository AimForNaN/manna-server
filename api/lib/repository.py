import Sword;
from .module import Module;

class Repository():
    def __init__(self, mgr: Sword.SWMgr):
        self.swmgr = mgr;

    def __iter__(self):
        mgr = self.swmgr;
        yield('Modules', [dict(mod) for mod in self.getModules()]);
        yield('Path', mgr.prefixPath);

    def getModule(self, mod):
        modules = self.getModulesMapped();
        return modules[mod];

    def getModules(self):
        mgr = self.swmgr;
        modules = [];
        for name, mod in mgr.getModules().items():
            mod = Module(mod);
            modules.append(mod);

        modules.sort(key=lambda mod: mod.getName());
        return modules;

    def getModulesMapped(self):
        modules = self.getModules();
        ret = {};
        for mod in modules:
            ret[mod.getName()] = mod;

        return ret;