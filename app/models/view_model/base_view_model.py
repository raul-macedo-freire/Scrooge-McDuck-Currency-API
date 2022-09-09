from abc import ABC, abstractmethod, abstractstaticmethod
from flask import jsonify, Response
from flask_restx import Model, marshal


class BaseViewModel(ABC):
    @abstractstaticmethod
    def schema_model() -> Model: ...

    @abstractmethod
    def to_response_json(self,) -> Response:
        return jsonify(marshal(self, self.schema_model()))
