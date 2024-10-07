import os

from pymongo import MongoClient
from bson.objectid import ObjectId

from typing import List

from src.exceptions.database_exception import DataBaseException, RegistryNotFound
from src.models import ToDo

from datetime import datetime, timezone

import yaml
from yaml import CLoader

config = None
with open(os.path.dirname(__file__) + '/dev_config.yml', 'r', encoding='utf8') as file:
    config = yaml.load(file, Loader=CLoader)

class Database():

    def get_database(self):

        client = MongoClient(config['host'])

        return client[config['database']]

    def list_all(self) -> List[ToDo]:
        return self._find_all()

    def insert(self, todo: ToDo) -> ToDo:
        todo.creation_time = get_current_timestamp()
        todo.id = create_id()

        result = self._insert_todo(todo)

        if (result is None) or (result.inserted_id is None):
            raise DataBaseException(operation='insert', id=str(todo.id), obj=todo)

        return todo

    def delete(self, id: str) -> id:
        result = self._delete_todo(id)

        if (result is None) or (result.deleted_count is None):
            raise DataBaseException(operation='delete', id=str(id), obj=None)

        if result.deleted_count == 0:
            raise RegistryNotFound(operation='delete', id=str(id), obj=None)

        return id

    def _find_all(self) -> List[ToDo]:
        try:
            results = self.get_database()[config['collection']].find()
            mapped = [ToDo.model_validate(x) for x in results]
            return mapped
        except Exception as error:
            raise DataBaseException(operation='find', id=str(id), obj=None)

        return []

    def _insert_todo(self, todo: ToDo):
        try:
            return self.get_database()['tickets'].insert_one(todo.model_dump(by_alias=True))
        except:
            raise DataBaseException(operation='insert_one', id=todo.id, obj=todo)

    def _delete_todo(self, id:str):
        try:
            return self.get_database()['tickets'].delete_one({"_id": ObjectId(id)})
        except:
            raise DataBaseException(operation='delete_one', id=str(id), obj=None)



def create_id() -> ObjectId:
    return ObjectId()


def get_current_timestamp():
    return datetime.now(timezone.utc).isoformat(timespec='seconds').replace("+00:00", "Z")

