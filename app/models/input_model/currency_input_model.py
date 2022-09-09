from pydantic import Field

from app.models.input_model.base_input_model import BaseInputModel
from flask_restx import Model, fields


class CurrencyInputModel(BaseInputModel):
    id: str = Field(..., max_length=10)
    name: str = Field(..., max_length=50)
    dollar_conversion_rate: float = Field(
        ..., description="How many of the currency is necessay to make a dollar")

    @staticmethod
    def schema_model() -> Model:
        return Model('CreateCurrency', {
            'id': fields.String(max_length=10, description='Universal identifier of the currency'),
            'name': fields.String(max_length=50, description='Name of the currency'),
            'dollar_conversion_rate': fields.Float(description='How many of the currency is necessay to make a dollar')
        })
