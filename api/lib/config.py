import tomli;
import tomli_w;
from wrapt import ObjectProxy;

class MannaConfig(ObjectProxy):
    Path = 'manna.ini';

    def __init__(self):
        super().__init__({});
        self.read();

    def read(self):
        with open(self.Path, 'rb') as conf:
            ini = tomli.load(conf);
            conf.close();
            self.__wrapped__ = ini;

    def save(self):
        with open(self.Path, 'wb') as conf:
            tomli_w.dump(self, conf);
            conf.close();