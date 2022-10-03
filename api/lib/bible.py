import Sword;
from .module import Module;

class Bible(Module):
    def getStructure(self):
        mod = self.swmod;
        ret = [];

        key = Sword.VerseKey(mod.getKey());
        # key.setVersificationSystem(mod.getConfigEntry('Versification'));
        for x in [1,2]:
            key.setTestament(x);
            for y in range(1, key.getBookMax()):
                key.setBook(y);
                bookName = key.getBookName();
                ret.append({
                    'Name': bookName,
                    'Children': [{ 'Name': ch, 'Key': '{book}.{chapter}'.format(book = bookName, chapter = ch) } for ch in range(1,key.getChapterMax()+1)],
                    'Index': ord(key.getBook()),
                    'Testament': ord(key.getTestament()),
                    'Type': self.getType(),
                });

        return ret;

    def getText(self):
        ret = [];
        mod = self.swmod;
        key = Sword.VerseKey(mod.getKey());
        lk = key.parseVerseList(self.key, None, True);

        for i in range(lk.getCount()):
            el = Sword.VerseKey(lk.getElement(i));
            upper = el.getUpperBound();
            while not upper.equals(el):
                ret.append(self.renderText(el));
                el.increment();

            ret.append(self.renderText(el));
        
        return ret;

    def renderText(self, key: Sword.VerseKey):
        return {
            'Book': key.getBookName(),
            'Chapter': key.getChapter(),
            'Text': super().renderText(key),
            'Verse': key.getVerse(),
        };