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
        mod = self.swmod;
        key = mod.getKey();
        key = Sword.TreeKeyIdx_castTo(key.clone());
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