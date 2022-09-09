from injector import inject
from app.core.entities.currency import Currency
from app.core.exceptions import CurrencyNotFound
from app.infra.repositories.interfaces.abstract_currency_repository import AbstractCurrencyRepository
from app.infra.services.interfaces.abstract_external_currency_service import AbstractExternalCurrencyService
from app.services.interfaces.abstract_currency_service import AbstractCurrencyService


class CurrencyService(AbstractCurrencyService):
    @inject
    def __init__(self, repo: AbstractCurrencyRepository, infra_service: AbstractExternalCurrencyService):
        self.__repo = repo
        self.__infra_service = infra_service

    def create_currency(
            self,
            currency_id: str,
            currency_dollar_conversion_rate: float,
            currency_name: str = None):

        currency = self.__repo.find(currency_id)

        if not currency:
            currency = Currency.create(
                id=currency_id,
                dollar_conversion_rate=currency_dollar_conversion_rate,
                name=currency_name
            )
            return self.__repo.save(currency)

        elif currency.deleted_at is not None:
            currency.recreate(
                name=currency_name, dollar_conversion_rate=currency_dollar_conversion_rate)
            return self.__repo.save(currency)

        else:
            return

    def buscar_currencies(self,  size=100, page=1):
        return self.__repo.find_all(size=size, page=page)

    def buscar_currency(self, _id: str) -> Currency:
        if currency := self.__repo.find(_id):
            return currency
        else:
            raise CurrencyNotFound(_id)

    def update_currency(
            self,
            currency_id,
            currency_dollar_conversion_rate: float = None,
            currency_name: str = None):
        currency = self.__repo.find(currency_id)
        if not currency:
            raise CurrencyNotFound(currency_id)

        currency.update(
            name=currency_name,
            dollar_conversion_rate=currency_dollar_conversion_rate
        )

        return self.__repo.save(currency)

    def update_batch_currencies(self):
        new_rates = self.__infra_service.get_all_latest_currencies()
        currencies = []
        for rate_id, rate in new_rates.items():
            currency = self.__repo.find(rate_id)
            if not currency:
                currencies.append(Currency.create(
                    id=rate_id, dollar_conversion_rate=rate))

            elif not currency.deleted_at:
                currency.update(dollar_conversion_rate=rate)
                self.__repo.save(currency)

        if currencies:
            self.__repo.save_many(currencies)

    def delete_currency(self, currency_id: str):
        if currency := self.__repo.find(currency_id):
            currency.delete()
            return self.__repo.save(currency)

        raise CurrencyNotFound(currency_id)
