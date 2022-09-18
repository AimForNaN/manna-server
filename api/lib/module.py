import Sword;

class Module():
    _key = None;

    def __init__(self, mod: Sword.SWModule):
        self.swmod = mod;
        self._key = mod.getKey().getText();

    def __iter__(self):
        mod = self.swmod;
        ret = {
            'About': mod.getConfigEntry('About'),
            'Description': mod.getDescription(),
            'Encoding': mod.getConfigEntry('Encoding'),
            'Feature': mod.getConfigEntry('Feature'),
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

    def getStructure(self):
        return [];

    def getText(self):
        return self.renderText();

    def renderText(self, key: Sword.SWKey = None):
        mod = self.swmod;

        if key is None:
            if self._key is not None:
                mod.setKey(Sword.SWKey(self._key));
        else:
            mod.setKey(key);

        if mod.getKey().getText() is not None:
            mod.renderText();
            return mod.getRawEntry();

        return None;

    def setKey(self, v: str):
        self._key = v;

    key = property(getKey, setKey);