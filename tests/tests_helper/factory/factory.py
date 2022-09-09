from random import shuffle
import string
from app.core.entities.currency import Currency
from faker import Faker

from app.infra.models.currency_model import CurrencyModel


class Factory():
    def __init__(self,):
        self.faker = Faker()

    def factory_currency(self, create_updated=False, create_deleted=False) -> Currency:
        """Creates an domain Currency entity with faked parameters"""

        return Currency(
            id=self.factory_id(),
            name=self.faker.text(50),
            dollar_conversion_rate=self.faker.pyfloat(positive=True),
            created_at=self.faker.date_time(),
            updated_at=self.faker.date_time() if create_updated else None,
            deleted_at=self.faker.date_time() if create_deleted else None
        )

    def factory_currency_model(self, create_updated=False, create_deleted=False) -> CurrencyModel:
        """Creates an infrastructure Currency model with faked parameters """
        return CurrencyModel(
            id=self.factory_id(),
            currency_name=self.faker.text(50),
            dollar_conversion_rate=self.faker.pyfloat(positive=True),
            created_at=self.faker.date_time(),
            updated_at=self.faker.date_time() if create_updated else None,
            deleted_at=self.faker.date_time() if create_deleted else None
        )

    def factory_id(self, id_size=3):
        letters = list(string.ascii_uppercase)
        shuffle(letters)
        return ''.join(letters[:id_size])

    def factory_open_exchange_response(self, rates_quantity=3):
        rates = {self.factory_id(): self.faker.pyfloat(positive=True)
                 for _ in range(rates_quantity)}

        return {
            "disclaimer": self.faker.url(),
            "license": self.faker.url(),
            "timestamp": 123,
            "base": "FOO",
            "rates": rates,
        }
