import Sword;

class Module():
    _key = '';

    def __init__(self, mod: Sword.SWModule):
        self.swmod = mod;
        self.key = mod.getKey().getText();

    def __iter__(self):
        mod = self.swmod;
        ret = {
            'About': mod.getConfigEntry('About'),
            'Description': mod.getDescription(),
            'Encoding': mod.getConfigEntry('Encoding'),
            'Feature': mod.getConfigEntry('Feature'),
            'Key': self.key,
            'Language': mod.getConfigEntry('Lang'),
            'Module': mod.getName(),
            'SourceType': mod.getConfigEntry('SourceType'),
            'Type': mod.getType(),
            'Version': mod.getConfigEntry('Version'),
        };
        for x,y in ret.items():
            yield(x, y);

    def getKey(self):
        return self._key;

    def renderText(self, key: Sword.SWKey):
        mod = self.swmod;
        mod.setKey(key);
        mod.renderText();
        return mod.getRawEntry();

    def setKey(self, v: str):
        self._key = v;

    key = property(getKey, setKey);