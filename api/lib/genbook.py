import Sword;
from .module import Module

class GenBook(Module):
    def __iter__(self):
        ret = dict(super().__iter__());
        ret['Structure'] = self.getStructure();
        ret['Text'] = self.getText();

        for x in sorted(ret.keys()):
            yield(x, ret[x]);

    def getStructure(self):
        return [];