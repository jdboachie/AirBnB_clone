#!/usr/bin/python3

"""This module defines a class User"""

from models.base_model import BaseModel


class User(BaseModel):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
