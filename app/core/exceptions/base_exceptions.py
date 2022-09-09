class InternalError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ClientError(Exception):
    def __init__(self, message: str, status_code: int):
        self.status_code = status_code
        self.message = message
        super().__init__(message)
