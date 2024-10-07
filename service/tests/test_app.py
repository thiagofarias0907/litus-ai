from pymongo.results import InsertOneResult, DeleteResult

from src import app
from src import ToDo

from bson.objectid import ObjectId
from fastapi.testclient import TestClient

import unittest
from unittest.mock import patch
import json
import os


client = TestClient(app)

test_dir = os.path.dirname(__file__)

mock_todo = ToDo(_id=ObjectId('6702a8aa30dad4c71f9cb4af'), title='Testing insert', creation_time='2024-10-06T10:00:00Z',
                 estimated_time=15)


class ToDoResponseTestCase(unittest.TestCase):

    def test_read_base_data(self):
        with patch('src.database.Database.list_all') as mock_database_list:
            mock_database_list.return_value = [mock_todo]

            expected_response = [{'_id': '6702a8aa30dad4c71f9cb4af', 'title': 'Testing insert', 'creation_time': '2024-10-06T10:00:00Z', 'estimated_time': 15}]

            response = client.get("/todos")
            self.assertEqual(200, response.status_code)
            self.assertEqual(expected_response, response.json())

    def test_insert_one(self):
        expected_response= '{"_id": "6702a8aa30dad4c71f9cb4af", "title": "Testing insert", "estimated_time": 15, "creation_time": "2024-10-06T10:00:00Z"}'

        with patch('src.database.get_current_timestamp') as mock_get_current_timestamp,\
                patch("src.database.create_id") as mock_create_id,\
                patch("src.database.Database._insert_todo") as mock_insert_one:
            mock_get_current_timestamp.return_value = '2024-10-06T10:00:00Z'
            mock_create_id.return_value = ObjectId('6702a8aa30dad4c71f9cb4af')
            mock_insert_one.return_value = InsertOneResult(inserted_id=ObjectId('6702a8aa30dad4c71f9cb4af'), acknowledged=True)

            response = client.post("/todos/insert",json={"title":"Testing insert","estimated_time": 15})
            self.assertEqual(201, response.status_code)
            self.assertEqual(json.loads(expected_response), response.json())

    def test_insert_one_missing_fields_satus_code(self):
        response = client.post("/todos/insert",json={"estimated_time": 15})
        self.assertEqual(422, response.status_code)

        response = client.post("/todos/insert",json={"title":"Testing insert"})
        self.assertEqual(422, response.status_code)

        response = client.post("/todos/insert",json={})
        self.assertEqual(422, response.status_code)

    def test_delete_by_id(self):
        with patch("src.database.Database._delete_todo") as mock_delete_todo:
            mock_delete_todo.side_effect = [
                DeleteResult(raw_result={'n':1},acknowledged=True),
                DeleteResult(raw_result={'n':0},acknowledged=True),
            ]

            response = client.delete("/todos/delete/6702a8aa30dad4c71f9cb4af")
            self.assertEqual(204, response.status_code)


            response = client.delete("/todos/delete/6702a8aa30dad4c71f9cb4af")
            self.assertEqual(404, response.status_code)




if __name__ == '__main__':
    unittest.main()
