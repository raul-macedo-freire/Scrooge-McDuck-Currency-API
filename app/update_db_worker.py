from datetime import datetime
from injector import inject

from app.services.interfaces.abstract_currency_service import AbstractCurrencyService


class UpdateDbWorker:
    """This worker is suposed to call only a run function to perform database update"""
    @inject
    def __init__(self, service: AbstractCurrencyService):
        self.__service = service

    def run(self,):
        # NOTE: Again, logging would be better for printing information, but it doesn't seems to be interesting for such application
        print(f"INFO: Starting db update: {datetime.now()}")

        self.__service.update_batch_currencies()

        print(f"INFO: Finishing db update {datetime.now()}")
