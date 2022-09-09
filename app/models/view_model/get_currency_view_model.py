from datetime import datetime
from dataclasses import dataclass

from flask_restx import Model, fields

from app.models.view_model.base_view_model import BaseViewModel


@dataclass
class GetCurrencyViewModel(BaseViewModel):
    id: str
    name: str
    dollar_conversion_rate: float
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime = None

    @staticmethod
    def schema_model():
        return Model('Currency', {
            'id': fields.String(max_length=10, description='Universal identifier of the currency'),
            'name': fields.String(max_length=50, description='Name of the currency'),
            'dollar_conversion_rate': fields.Float(description='How many of the currency is necessay to make a dollar'),
            'updated_at': fields.DateTime(),
            'created_at': fields.DateTime()
        })

    def to_response_json(self):
        return super().to_response_json()
