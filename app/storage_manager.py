import json


class StorageManager(object):
    def __init__(self, path, **kwargs):
        self.path = path

    def fetch(self):
        f = open(self.path, 'r')
        data = json.loads(f.read())
        return data