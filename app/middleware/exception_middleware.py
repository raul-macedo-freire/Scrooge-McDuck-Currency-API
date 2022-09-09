import traceback
from werkzeug.wrappers import Response
from pydantic.error_wrappers import ValidationError as PydanticValidationError
from app.core.exceptions import InternalError, ClientError


class ExceptionMiddleware():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        try:
            return self.app(environ, start_response)

        except ClientError as ex:
            res = Response(ex.message, status=ex.status_code)
            return res(environ, start_response)

        except InternalError as ex:
            res = Response(ex.message, mimetype='text/plain', status=500)
            return res(environ, start_response)

        except PydanticValidationError as ex:
            res = Response(
                ex.json(), content_type='application/json', status=400)
            return res(environ, start_response)

        except Exception as ex:
            # NOTE: Using logging for this one would be nicier, however i'll just let print() for practical purposes
            print(f"ERROR: {traceback.format_exc()}")
            res = Response(
                u'An unexpected error has ocurred. Please contact suport', status=500)
            return res(environ, start_response)
