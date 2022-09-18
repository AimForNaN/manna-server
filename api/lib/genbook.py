import Sword;
from .module import Module

class GenBook(Module):
    def __init__(self, mod: Sword.SWModule):
        super().__init__(mod);

        key = mod.getKey();
        key = Sword.TreeKeyIdx_castTo(key.clone());
        if key.firstChild():
            self.setKey(key.getText());

    def __iter__(self):
        ret = dict(super().__iter__());
        ret['Text'] = self.getText();

        for x in sorted(ret.keys()):
            yield(x, ret[x]);

    def getStructure(self):
        mod = self.swmod;
        key = mod.getKey();
        key = Sword.TreeKeyIdx_castTo(key.clone());
        key.root();
        return self.pullStructure(key);

    def pullStructure(self, tk: Sword.TreeKey):
        ret = [];
        if tk.firstChild():
            while True:
                ret.append(tk.getText());

                if tk.hasChildren():
                    ret = ret + self.pullStructure(tk);
                
                if not tk.nextSibling():
                    break;
            
            tk.parent();
        
        return ret;