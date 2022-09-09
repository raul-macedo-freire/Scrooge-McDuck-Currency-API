from abc import ABC, abstractstaticmethod
from flask_restx import Model
from pydantic import BaseModel


class BaseInputModel(BaseModel, ABC):
    @abstractstaticmethod
    def schema_model() -> Model: ...
