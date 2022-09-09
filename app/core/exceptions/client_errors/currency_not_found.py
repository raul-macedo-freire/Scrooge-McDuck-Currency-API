
from http import HTTPStatus
from app.core.exceptions import ClientError


class CurrencyNotFound(ClientError):
    def __init__(self, currency_id: str):
        super().__init__(
            f"No currency found with id: {currency_id}", HTTPStatus.NOT_FOUND)
