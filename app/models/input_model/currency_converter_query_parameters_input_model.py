from pydantic import Field
from pydantic.dataclasses import dataclass
from app.models.input_model.base_input_model import BaseInputModel


@dataclass(config=dict(validate_assignment=True))
class CurrencyConverterQueryParametersInputModel(BaseInputModel):
    from_currency: str = Field(..., max_length=10)
    to_currency: str = Field(..., max_length=10)
    amount: float = Field(...)

    def schema_model():
        raise NotImplementedError('Method not implemented')
