from typing import Optional, Annotated, Any, Union

from bson import ObjectId
from pydantic import BaseModel, Field, BeforeValidator, ConfigDict
from pydantic_core import core_schema


## https://stackoverflow.com/questions/76686888/using-bson-objectid-in-pydantic-v2/77105412#77105412
class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.chain_schema([
                    core_schema.str_schema(),
                    core_schema.no_info_plain_validator_function(cls.validate),
                ])
            ]),
            serialization=core_schema.to_string_ser_schema(),
        )

    @classmethod
    def validate(cls, value) -> ObjectId:
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid ObjectId")

        return ObjectId(value)


class ToDo(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    estimated_time: int
    creation_time: Optional[str] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)
