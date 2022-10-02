import Sword;
from .module import Module

class GenBook(Module):
    def __init__(self, mod: Sword.SWModule):
        super().__init__(mod);

        key = mod.getKey();
        key = Sword.TreeKeyIdx_castTo(key.clone());
        if key.firstChild():
            self.setKey(key.getText());

    def getStructure(self):
        mod = self.swmod;
        key = mod.getKey();
        key = Sword.TreeKeyIdx_castTo(key.clone());
        key.root();
        return self.pullStructure(key);

    def getText(self):
        return [{
            'Text': self.renderText(),
        }];

    def pullStructure(self, tk: Sword.TreeKey, parent: str = None):
        ret = [];
        if tk.firstChild():
            while True:
                key = tk.getText();
                name = str(key).split('/').pop();
                ret.append({
                    'Key': key,
                    'Name': name,
                    'Parent': parent,
                });

                if tk.hasChildren():
                    ret = ret + self.pullStructure(tk, key);
                
                if not tk.nextSibling():
                    break;
            
            tk.parent();
        
        return ret;