from injector import inject
from app.core.entities.currency import Currency
from app.infra.repositories.interfaces.abstract_currency_repository import AbstractCurrencyRepository
from app.core.exceptions.client_errors.currency_not_found import CurrencyNotFound
from app.services.interfaces.abstract_converter_service import AbstractConverterService


class ConverterService(AbstractConverterService):
    @inject
    def __init__(self, currency_repo: AbstractCurrencyRepository):
        self.__repo = currency_repo

    def convert_currency(self, from_currency: str, to_currency: str, amount: float):
        currency_from: Currency = self.__repo.find(from_currency)
        if not currency_from:
            raise CurrencyNotFound(from_currency)
        currency_to: Currency = self.__repo.find(to_currency)
        if not currency_to:
            raise CurrencyNotFound(to_currency)
        in_dollars = self.__convert_to_dollar(currency_from, amount)
        return self.__convert_from_dollar(currency_to, in_dollars)

    def __convert_to_dollar(self, currency: Currency, value: float) -> float:
        return value/currency.dollar_conversion_rate

    def __convert_from_dollar(self, currency: Currency, value: float) -> float:
        return value*currency.dollar_conversion_rate
