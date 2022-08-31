import Sword;

class Module():
    def __init__(self, mod: Sword.SWModule):
        self.swmod = mod;

    def __iter__(self):
        mod = self.swmod;
        ret = {
            'About': mod.getConfigEntry('About'),
            'Description': mod.getDescription(),
            'Encoding': mod.getConfigEntry('Encoding'),
            'Feature': mod.getConfigEntry('Feature'),
            'Language': mod.getConfigEntry('Lang'),
            'Module': mod.getName(),
            'Type': mod.getType(),
            'Version': mod.getConfigEntry('Version'),
        };
        for x,y in ret.items():
            yield(x, y);