import unittest
from unittest.mock import patch

import re

from bson import ObjectId
from pymongo.results import DeleteResult

from src import Database, create_id, get_current_timestamp
from src.exceptions.database_exception import RegistryNotFound


class TestDatabase(unittest.TestCase):

    def test_get_current_timestamp(self):
        result = get_current_timestamp()
        pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z'
        match = re.match(pattern, result)
        self.assertTrue(match)

    def test_create_id(self):
        result = create_id()
        self.assertTrue(isinstance(result, ObjectId))
        pattern = r'[0-9a-z]{24}'
        match = re.match(pattern, str(result))
        self.assertTrue(match)

    def test_delete_raise_exception(self):
        with self.assertRaises(expected_exception=RegistryNotFound), \
                patch("src.database.Database._delete_todo") as mock_delete_todo:
            mock_delete_todo.return_value = DeleteResult(raw_result={'n': 0}, acknowledged=True)
            Database().delete(id='a')