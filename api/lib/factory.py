import configparser;
import Sword;
from .module import Module;

class Factory():
    @staticmethod
    def getRepository(repo: str):
        mgr = None;
        if repo.lower() == 'default':
            mgr = Sword.SWMgr();
        else:
            conf = configparser.ConfigParser();
            conf.read('manna.ini');
            paths = conf.get('Repositories', []);
            if repo in paths:
                mgr = Sword.SWMgr(paths[repo]);

        return mgr;

    @staticmethod
    def fromModule(mod: Sword.SWModule):
        return Module(mod);