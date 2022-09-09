from app.core.exceptions import ClientError


class ValidationError(ClientError):

    def __init__(self, message: str, status_code: int):
        super().__init__(
            message, status_code)
