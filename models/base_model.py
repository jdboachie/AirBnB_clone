#!usr/bin/python3
"""BaseModel module for all other classes to inherit from"""
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel class for all other classes to inherit from"""

    def __init__(self, **kwargs):
        """Initialize BaseModel class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = uuid4()
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def __str__(self, ):
        """Return string representation of BaseModel instance

        Returns:
            str: string representation of BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self, ):
        """Update updated_at attribute with current datetime
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self, ):
        """Return dictionary representation of BaseModel instance

        Returns:
            dict: dictionary representation of BaseModel instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict
