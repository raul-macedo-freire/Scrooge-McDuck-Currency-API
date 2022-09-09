from http import HTTPStatus
from requests.exceptions import HTTPError
from requests import Response


class RequestsMock:
    def __init__(self, status_code, json):
        self.status_code = status_code
        self.__json = json

    def json(self,):
        return self.__json

    def raise_for_status(self,):
        if self.status_code >= 400:
            error = HTTPError("dang my friend, that's an error")
            response = Response()
            response.status_code = self.status_code
            error.response = response
            raise error
