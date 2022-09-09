from configparser import ConfigParser
from injector import singleton
from app.update_db_worker import UpdateDbWorker
from app.infra.repositories.currency_repository import CurrencyRepository
from app.infra.repositories.interfaces.abstract_currency_repository import AbstractCurrencyRepository
from app.infra.services.interfaces.abstract_external_currency_service import AbstractExternalCurrencyService
from app.infra.services.open_exchanges_api_service import OpenExchangesApiService
from app.services.converter_service import ConverterService
from app.services.currency_service import CurrencyService
from app.services.interfaces.abstract_converter_service import AbstractConverterService
from app.services.interfaces.abstract_currency_service import AbstractCurrencyService


class IoC:
    def __init__(self, config: ConfigParser):
        self.__config = config

    def configure(self, binder):
        binder.bind(ConfigParser, to=self.__config, scope=singleton)

        binder.bind(AbstractCurrencyRepository,
                    to=CurrencyRepository, scope=singleton)

        binder.bind(AbstractExternalCurrencyService,
                    to=OpenExchangesApiService, scope=singleton)

        binder.bind(AbstractConverterService,
                    to=ConverterService, scope=singleton)

        binder.bind(AbstractCurrencyService,
                    to=CurrencyService, scope=singleton)

        binder.bind(UpdateDbWorker, scope=singleton)
