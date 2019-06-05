import unittest

import os

import pandas as pd
from datetime import datetime

from config import BASE_DIR
from app.recommender import Recommender


class TestCasesRecommender(unittest.TestCase):
    def test_clean(self):
        path = os.path.join(BASE_DIR, "sample_data.json")
        r = Recommender(path)
        df = r._read()
        df = r.clean(df)

        # Check if it returns dataframe
        self.assertIsInstance(df, pd.DataFrame)

        # Check if columns are present
        self.assertIn('clean_content', df.columns)
        self.assertIn('date', df.columns)

        # Check datatype of newly added date column
        self.assertIsInstance(df.date[0], datetime)

    def test_get(self):
        path = os.path.join(BASE_DIR, "sample_data.json")
        r = Recommender(path)
        df = r.get()

        self.assertIsInstance(df, pd.DataFrame)

        # Check if it has required columns
        for item in ['tags', 'url']:
            self.assertIn(item, df.columns)

        # Check for valid output
        row = df.iloc[0]
        self.assertEqual('mobile,google phone', row.tags)
        self.assertEqual('https://example.sg.nl/pixel-3a', row.url)
