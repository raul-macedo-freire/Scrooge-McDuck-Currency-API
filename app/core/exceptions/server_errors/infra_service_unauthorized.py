
from app.core.exceptions import InternalError


class InfraOperationUnauthorized(InternalError):
    def __init__(self, message: str):
        super().__init__(message)
