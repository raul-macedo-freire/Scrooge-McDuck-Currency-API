from dataclasses import dataclass
from datetime import datetime
from mongoengine import (DateTimeField, Document,
                         StringField, FloatField)


@dataclass
class CurrencyModel(Document):

    id: str = StringField(required=True, max_length=10, primary_key=True)
    currency_name: str = StringField(max_length=50)
    dollar_conversion_rate: float = FloatField(required=True)
    created_at: datetime = DateTimeField()
    updated_at: datetime = DateTimeField()
    deleted_at: datetime = DateTimeField()

    meta = {'collection': 'currencies',
            'strict': False, 'db_alias': 'currency'}

    def __init__(self, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
