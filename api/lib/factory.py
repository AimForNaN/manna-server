import tomli;
import Sword;
from .bible import Bible;
from .module import Module;

class Factory():
    @staticmethod
    def getIni():
        try:
            with open('manna.ini') as conf:
                ret = tomli.load(conf);
                conf.close();
                return ret;
        except:
            return {};

    @staticmethod
    def getRepository(repo: str):
        mgr = None;
        if repo.lower() == 'default':
            mgr = Sword.SWMgr();
        else:
            ini = Factory.getIni();
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