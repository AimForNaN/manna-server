import Sword;
from .module import Module;

class Bible(Module):
    def __iter__(self):
        ret = super().__iter__();

        for x,y in ret:
            yield(x, y);
        
        yield('Books', self.getBooks());

    def getBooks(self):
        mod = self.swmod;
        ret = [];

        key = Sword.VerseKey(mod.getKey());
        key.setVersificationSystem(mod.getConfigEntry('Versification'));
        for x in [1,2]:
            key.setTestament(x);
            for y in range(1, key.getBookMax()):
                key.setBook(y);
                ret.append({
                    'Book': key.getBookName(),
                    'Chapters': key.getChapterMax(),
                    'Index': ord(key.getBook()),
                    'Testament': ord(key.getTestament()),
                });

        return ret;
