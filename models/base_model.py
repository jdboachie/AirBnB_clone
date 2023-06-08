#!/usr/bin/python3
"""BaseModel class for AirBnB"""

from models import storage
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel class for AirBnB"""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize BaseModel
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            kwargs.pop("__class__", None)
            for attrib, value in kwargs.items():
                if attrib in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, attrib, value)

    def __str__(self) -> str:
        """__str__ method for BaseModel

        Returns:
            str: [BaseModel] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self) -> None:
        """save method for BaseModel
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """to_dict method for BaseModel

        Returns:
            dict: dictionary of BaseModel
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.created_at.isoformat()
        return obj_dict
