from datetime import datetime

import pandas as pd
from slugify import slugify

from app.storage_manager import StorageManager


class Recommender(object):
    def __init__(self, path):
        self.path = path

    def _read(self, path):
        """Fetches data with the help of StorageManager and creates DataFrame
        
        Arguments:
            path {str} -- Path of JSON file
        
        Returns:
            df -- Data of JSON file as a DataFrame
        """
        storage = StorageManager(path)
        df = pd.DataFrame([x for x in storage.fetch()])
        return df

    def clean(self, df):
        # Change data types as per necessity
        df = df.astype({'timestamp': int})

        # Add date column using timestamp
        df['date'] = df.apply(lambda x: datetime.fromtimestamp(x.timestamp),
                              axis=1)

        # Add slugified content column to remove duplicates, case mismatches
        df['clean_content'] = df.apply(lambda x: slugify(x.content,
                                                         separator='|'),
                                       axis=1)

        # Sort data by date
        df = df.sort_values('date', ascending=True)
        return df

    def get(self):

        # Read data
        df = self._read(self.path)

        # Clean data
        df = self.clean(df)

        recommendations = pd.DataFrame([{'url': 'asd', 'tags': ''}])
        return df
