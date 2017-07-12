from ..cache import BaseCache
from tinyxbmc import hay


class HayCache(BaseCache):
    def __init__(self, directory, maxrecords=5000):
        self.hay = hay.stack(directory, "null", 0, maxrecords)

    def get(self, key):
        data = self.hay.find(key).data
        if data == {}:
            data = None
        return data

    def set(self, key, value):
        self.hay.throw(key, value)

    def delete(self, key):
        self.hay.lose(key)

    def close(self):
        print 3333333333333333333
        self.hay.close()
