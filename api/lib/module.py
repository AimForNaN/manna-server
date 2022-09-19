import Sword;

class Module():
    _key = None;
    _status = None;

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
            'SearchFramework': mod.hasSearchFramework(),
            'SourceType': mod.getConfigEntry('SourceType'),
            'Status': self.getStatus(),
            'Type': mod.getType(),
            'Version': mod.getConfigEntry('Version'),
        };
        for x,y in ret.items():
            yield(x, y);

    def getKey(self):
        return self._key;

    def getName(self):
        return self.swmod.getName();

    def getStructure(self):
        return [];

    def getText(self):
        return [self.renderText()];

    def getType(self):
        return self.swmod.getType();

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

    def getStatus(self):
        return self._status;

    def setStatus(self, status):
        self._status = status;

    key = property(getKey, setKey);
    Status = property(getStatus, setStatus);