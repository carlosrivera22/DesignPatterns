from typing import Any, Optional
from abc import ABC, abstractmethod

class Request:

    def __init__(self,description,value):
        self.value = value
        self.description = description
    
    def getValue(self):
        return self.value

    def getDescription(self):
        return self.description

    

