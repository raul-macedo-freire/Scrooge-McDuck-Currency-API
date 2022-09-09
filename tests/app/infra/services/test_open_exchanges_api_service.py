from configparser import ConfigParser
from unittest import TestCase, mock

from app.core.exceptions import InfraOperationUnauthorized, ExternalServiceError, ConfigurationError
from app.infra.services.open_exchanges_api_service import OpenExchangesApiService
from tests.tests_helper.requests_mock import RequestsMock
from tests.tests_helper.factory.factory import Factory

static_response_success = Factory().factory_open_exchange_response()


class TestOpenExchangesApiService(TestCase):

    def __init__(self, *args, **kwargs):
        self.__config = {'DEFAULT': {
            'OPENEXCHANGE_APP_ID': '123'}}
        self.__service = OpenExchangesApiService(self.__config)
        super(TestOpenExchangesApiService, self).__init__(*args, **kwargs)

    @ staticmethod
    def requests_side_effect_return_value(*args, **kwargs):
        return RequestsMock(200, static_response_success)

    @ mock.patch('requests.get', side_effect=requests_side_effect_return_value)
    def test_get_all_latest_currencies(self, _):
        resp = self.__service.get_all_latest_currencies()

        for key, value in resp.items():
            self.assertEqual(value, static_response_success['rates'][key])

    @ staticmethod
    def requests_side_effect_return_null(*args, **kwargs):
        return RequestsMock(401, "nothing good my friend, you've been blocked D:")

    @ mock.patch('requests.get', side_effect=requests_side_effect_return_null)
    def test_get_all_latest_currencies_raises_infra_operation_unauthorized_error(self, _):

        self.assertRaises(InfraOperationUnauthorized,
                          self.__service.get_all_latest_currencies)

    @ staticmethod
    def requests_side_effect_return_some_error(*args, **kwargs):
        return RequestsMock(432, "Some client error")

    @ mock.patch('requests.get', side_effect=requests_side_effect_return_some_error)
    def test_get_all_latest_currencies_raises_external_service_error(self, _):
        self.assertRaises(ExternalServiceError,
                          self.__service.get_all_latest_currencies)

    def test_get_all_latest_currencies_raises_configuration_error(self,):
        self.__config['DEFAULT']['OPENEXCHANGE_APP_ID'] = '$OPENEXCHANGE_APP_ID'
        self.assertRaises(ConfigurationError,
                          self.__service.get_all_latest_currencies)
