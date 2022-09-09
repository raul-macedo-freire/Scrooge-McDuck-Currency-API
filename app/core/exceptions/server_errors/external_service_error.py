
from app.core.exceptions import InternalError


class ExternalServiceError(InternalError):
    def __init__(self,message:str):
        super().__init__(message)
