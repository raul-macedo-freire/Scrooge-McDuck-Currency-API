from abc import ABC, abstractmethod
from typing import List

from app.core.entities.currency import Currency


class AbstractCurrencyService(ABC):
    @abstractmethod
    def create_currency(
            self,
            currency_id: str,
            currency_dollar_conversion_rate: float,
            currency_name: str = None) -> Currency | None:
        """ Creates a currency. If it already exists, return None
        :param currency_id: currency three digits identifier
        :param currency_dollar_conversion_rate: how many times the currency has to be multiplied to reach dollar value
        :param currency_name: The name of the currency"""
        ...

    @abstractmethod
    def buscar_currencies(self,  size=100, page=1
                          ) -> List[Currency]: ...

    @abstractmethod
    def buscar_currency(
        self, id: str
    ) -> Currency: ...

    @abstractmethod
    def update_currency(
        self,
        currency_id: str,
        currency_dollar_convertion_rate: float = None,
        currency_name: str = None) -> Currency: ...

    @abstractmethod
    def update_batch_currencies(self,): ...

    @abstractmethod
    def delete_currency(self, currency_id: str):
        """Set an deletion date to a currency, given it's identifier"""
        ...
