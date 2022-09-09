from typing import List
from dataclasses import dataclass
from flask_restx import Model, fields
from app.models.view_model.base_view_model import BaseViewModel

from app.models.view_model.get_currency_view_model import GetCurrencyViewModel


@dataclass
class GetCurrenciesViewModel(BaseViewModel):
    currencies: List[GetCurrencyViewModel]
    next_url: str = None

    @staticmethod
    def schema_model():
        return Model('Currencies', {
            'currencies': fields.Nested(GetCurrencyViewModel.schema_model()),
            'next_url': fields.String('next_url_resource')
        })

    def to_response_json(self):
        return super().to_response_json()
