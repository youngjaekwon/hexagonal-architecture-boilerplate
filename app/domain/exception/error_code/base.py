from enum import IntEnum, Enum
from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T", bound=IntEnum)
V = TypeVar("V", bound=Enum)


class CustomError(BaseModel, Generic[T, V]):
    code: T
    message: V

    @classmethod
    def generate_error_responses_content(cls):
        return {
            "application/json": {
                "examples": cls.Config.json_schema_extra["examples"]
            }
        }

    class Config:
        json_schema_extra = {
            "examples": {
            }
        }

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        code_enum_class = cls.__fields__["code"].annotation
        message_enum_class = cls.__fields__["message"].annotation
        if type(code_enum_class) == TypeVar or type(message_enum_class) == TypeVar:
            return
        if (
                isinstance(code_enum_class, type)
                and issubclass(code_enum_class, IntEnum)
                and isinstance(message_enum_class, type)
                and issubclass(message_enum_class, Enum)
        ):
            if code_enum_class.__members__.keys() == message_enum_class.__members__.keys():
                cls.Config.json_schema_extra["examples"] = {
                    err.name: {
                        "summary": err.name,
                        "value": {
                            "code": code_enum_class[err.name].value,
                            "message": err.value,
                        }
                    } for err in message_enum_class
                }
            else:
                raise TypeError("message must be Enum and have same keys with code")
        else:
            raise TypeError("code and message must be Enum")
