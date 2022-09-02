from api.lib.server import Server

# HACK: Apparently, makes relative imports work!? Useful for testing, at least!
__package__ = __name__;

if __name__ == '__main__':
    server = Server();
    server.run();
