from app.storage_manager import StorageManager
import unittest
import os

from config import BASE_DIR


class TestCasesStorageManager(unittest.TestCase):
    def test_valid_file(self):
        path = os.path.join(BASE_DIR, "sample_data.json")
        storage = StorageManager(path)
        data = storage.fetch()

        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], dict)
        self.assertGreaterEqual(len(data), 1)

    def test_invalid_file(self):
        path = os.path.join(BASE_DIR, "invalid_data_file.json")
        storage = StorageManager(path)

        self.assertRaises(FileNotFoundError, lambda: storage.fetch())
