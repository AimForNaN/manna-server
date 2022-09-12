import Sword;
from typing import Optional

from .config import MannaConfig;
from .bible import Bible;
from .module import Module;

class Factory():
    @staticmethod
    def getInstall(repo: Sword.SWMgr) -> Sword.InstallMgr:
        install = Sword.InstallMgr(repo.prefixPath);
        # People should already know what they're doing!
        install.setUserDisclaimerConfirmed(True);
        install.setTimeoutMillis(60000);
        return install;

    @staticmethod
    def getRepository(repo: str) -> Optional[Sword.SWMgr]:
        mgr = None;
        if repo.lower() == 'default':
            mgr = Sword.SWMgr();
        else:
            ini = MannaConfig();
            paths = ini.get('Repositories', []);
            if repo in paths:
                mgr = Sword.SWMgr(paths[repo]);

        return mgr;

    @staticmethod
    def fromModule(mod: Sword.SWModule):
        if mod.getType() == 'Biblical Texts':
            return Bible(mod);
        # if mod.getType() == 'Commentaries':
        #     return Commentary(mod);
        # if mod.getType() == 'Lexicons / Dictionaries':
        #     return Lexicon(mod);

        return Module(mod);