from typing import Any


class DataBaseException(Exception):
    def __init__(self, operation:str, obj: Any, id: str):
        self.operation = operation
        self.obj = obj
        self.id = id

    def __str__(self):
        return f"Failure while processing {self.operation} in Database for object with id {self.id} - {self.obj}"


class RegistryNotFound(Exception):
    def __init__(self, operation:str, obj: Any, id: str):
        self.operation = operation
        self.id = id

    def __str__(self):
        return f"Couldn't process {self.operation} because there isn't object with the given id {self.id}"
