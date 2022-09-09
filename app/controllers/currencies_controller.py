from dataclasses import asdict
from http import HTTPStatus
from flask_restx import Namespace

from flask import request, Response
from flask import jsonify
from injector import inject
from app.controllers.base_controller import BaseController
from app.models.view_model.get_currencies_view_model import GetCurrenciesViewModel
from app.models.view_model.get_currency_view_model import GetCurrencyViewModel
from app.services.interfaces.abstract_currency_service import AbstractCurrencyService

namespace = Namespace('Currency')


class CurrenciesController(BaseController):
    @inject
    def __init__(self, service: AbstractCurrencyService, **kwargs):
        self.__service = service
        super().__init__(**kwargs)

    @namespace.response(HTTPStatus.INTERNAL_SERVER_ERROR.value, 'Internal server error')
    @namespace.response(HTTPStatus.NO_CONTENT.value, 'No content found')
    @namespace.response(HTTPStatus.OK.value, "The currency json")
    @namespace.param("page_number", type='integer', default=1)
    @namespace.param("page_size", type='integer', default=100)
    @namespace.doc(description="Get all currencies")
    async def get(self,):
        page_number = int(request.args.get('page_number', default=1))
        page_size = int(request.args.get('page_size', default=100))

        if currencies := self.__service.buscar_currencies(size=page_size, page=page_number):
            next_url = self.__define_next_url(page_number, page_size)

            currency_list_model_view = [GetCurrencyViewModel(
                **asdict(currency)) for currency in currencies]

            return GetCurrenciesViewModel(
                currency_list_model_view, next_url).to_response_json()

        else:
            return Response(jsonify('[]'), status=HTTPStatus.NO_CONTENT)

    def __define_next_url(self, page_number, page_size):
        return f"{request.base_url}?page_size={page_size}&page_number={page_number + 1}"
