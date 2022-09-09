import datetime
from dataclasses import dataclass


@dataclass
class Currency:
    id: str
    name: str
    dollar_conversion_rate: float
    created_at: datetime
    updated_at: datetime = None
    deleted_at: datetime = None

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.dollar_conversion_rate = kwargs.get('dollar_conversion_rate')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        self.deleted_at = kwargs.get('deleted_at')

    @staticmethod
    def create(id: str,
               dollar_conversion_rate: float,
               name: str = None):

        currency = Currency()
        currency.id = id.upper()
        if name:
            currency.name = name
        currency.dollar_conversion_rate = dollar_conversion_rate
        currency.created_at = datetime.datetime.now()
        return currency

    def update(self,
               name: str = None,
               dollar_conversion_rate: float = None):
        self.name = name or self.name
        self.dollar_conversion_rate = dollar_conversion_rate or self.dollar_conversion_rate
        self.updated_at = datetime.datetime.now()

    def recreate(self,
                 name: str = None,
                 dollar_conversion_rate: float = None):
        self.deleted_at = None
        self.update(name, dollar_conversion_rate)

    def delete(self,):
        self.deleted_at = datetime.datetime.now()
