from abc import ABC, abstractmethod


class AbstractConverterService(ABC):
    @abstractmethod
    def convert_currency(self, from_currency: str, to_currency: str, amount: float) -> float:
        ...
