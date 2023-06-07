#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel:
    
    def __init__(self, *args, **kwargs) -> None:
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            kwargs.pop("__class__", None)
            for attrib, value in kwargs:
                if attrib in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(attrib, value)
    
    def __str__(self) -> str:
        return "[{}] ({}) {}".format(
                                __class__.__name__,
                                self.id,
                                self.__dict__
                            )
    
    def save(self) -> None:
        self.updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["updated_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return obj_dict