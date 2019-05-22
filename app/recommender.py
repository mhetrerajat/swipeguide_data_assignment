import pandas as pd

from app.storage_manager import StorageManager


class Recommender(object):
    def __init__(self, path):
        self.df = self._read(path)
        self.path = path

    def _read(self, path):
        storage = StorageManager(path)
        df = pd.DataFrame([x for x in storage.fetch()])
        return df

    def get(self):
        recommendations = pd.DataFrame([{'url': 'asd', 'tags': ''}])
        return recommendations