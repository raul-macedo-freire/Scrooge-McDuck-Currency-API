from abc import ABC, abstractmethod
from typing import Union
from typing import List

from app.core.entities.currency import Currency


class AbstractCurrencyRepository(ABC):
    @abstractmethod
    def save(self, currency: Currency) -> Currency:
        ''' Saves or update document  :class:`~app.infra.models.currency_model.CurrencyModel` given a currency entity
            :param currency: The object :class: `app.core.entities.currency.Currency` to be saved
        '''
        ...

    @abstractmethod
    def save_many(self, currencies: List[Currency]) -> List[Currency]:
        ''' Saves os update many documents CurrencyModel given an List of entities'''
        ...

    @abstractmethod
    def delete(self, id: str):
        ''' Deletes a currency if find's it, otherwise does nothing'''
        ...

    @abstractmethod
    def find(self, id: str) -> Union[Currency, None]:
        ''' Returns a currency entity if find's it by it's identifier, otherwise, returns nothing'''
        ...

    @abstractmethod
    def find_all(self, size=10, page=1) -> Union[List[Currency], None]:
        ''' Returns many entities and allows pagination
        :param int size:(optional) size of the document to be returned 
        :param int page:(optional) number of the page'''
        ...
