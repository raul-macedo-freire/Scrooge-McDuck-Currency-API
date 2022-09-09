from abc import ABC, abstractmethod
from typing import Dict


class AbstractExternalCurrencyService(ABC):

    @abstractmethod
    def get_all_latest_currencies(self,) -> Dict[str, float]:
        """Returns a dict with currency_id as keys and currency rate as values"""
        ...
