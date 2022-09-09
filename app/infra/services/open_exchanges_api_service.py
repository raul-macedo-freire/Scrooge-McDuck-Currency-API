from injector import inject
from configparser import ConfigParser
from http import HTTPStatus
from requests.exceptions import HTTPError
from typing import Dict
import requests
from app.infra.services.interfaces.abstract_external_currency_service import AbstractExternalCurrencyService
from app.core.exceptions import InfraOperationUnauthorized, ConfigurationError, ExternalServiceError


class OpenExchangesApiService(AbstractExternalCurrencyService):
    @inject
    def __init__(self, config: ConfigParser):
        self.__config = config["DEFAULT"]

    def get_all_latest_currencies(self) -> Dict[str, float]:
        openexchange_app_id = self.__config["OPENEXCHANGE_APP_ID"]
        if openexchange_app_id == "$OPENEXCHANGE_APP_ID":
            raise ConfigurationError(
                "The OPENEXCHANGE_APP_ID info has not been defined. Check the application documentation and update the service")

        response = requests.get(
            url=f'https://openexchangerates.org/api/latest.json?app_id={openexchange_app_id}&show_alternative=1')

        try:
            response.raise_for_status()
            return response.json()["rates"]
        except HTTPError as ex:
            if ex.response.status_code == HTTPStatus.UNAUTHORIZED:
                raise InfraOperationUnauthorized(
                    "The OPEN EXCHANGE APP ID is not valid or has expired, contact the support for help") from ex

            else:
                raise ExternalServiceError(
                    "Something went wrong trying to get currencies fom OpenExchangeApi. Contact suport. ") from ex
        except:
            raise ex
