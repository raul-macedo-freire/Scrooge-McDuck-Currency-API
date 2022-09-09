import json
from injector import inject
from http import HTTPStatus
from dataclasses import asdict
from flask_restx import Namespace
from flask import request, Response

from app.controllers.base_controller import BaseController
from app.core.exceptions.client_errors.validation_error import ValidationError
from app.services.interfaces.abstract_currency_service import AbstractCurrencyService
from app.models.view_model.get_currency_view_model import GetCurrencyViewModel
from app.models.input_model.update_currency_input_model import UpdateCurrencyInputModel
from app.models.input_model.currency_input_model import CurrencyInputModel

namespace = Namespace('Currency')


class CurrencyController(BaseController):
    models = [
        GetCurrencyViewModel.schema_model(),
        CurrencyInputModel.schema_model(),
        UpdateCurrencyInputModel.schema_model()
    ]

    @inject
    def __init__(self, service: AbstractCurrencyService, **kwargs):
        self.__service = service
        super().__init__(**kwargs)

    @namespace.response(HTTPStatus.INTERNAL_SERVER_ERROR.value, 'Internal server error')
    @namespace.response(HTTPStatus.NOT_FOUND.value, "Currency not found")
    @namespace.response(HTTPStatus.OK.value, "The currency json", model=GetCurrencyViewModel.schema_model())
    @namespace.param("currency_id", max_length=10, required=True)
    @namespace.doc(description="Get a currency by id")
    async def get(self):
        currency_id = self.__get_currency_id()
        currency = self.__service.buscar_currency(currency_id)
        return GetCurrencyViewModel(**asdict(currency)).to_response_json()

    @namespace.doc(description="Creates a currency", body=CurrencyInputModel.schema_model())
    @namespace.response(HTTPStatus.CREATED.value, 'Created currency')
    @namespace.response(HTTPStatus.CONFLICT.value, 'Currency already exists')
    @namespace.response(HTTPStatus.INTERNAL_SERVER_ERROR.value, "Internal server error")
    async def post(self):
        body = request.get_data()
        if not body:
            raise ValidationError('Request body is required')

        input_model = CurrencyInputModel(**json.loads(body))
        currency = self.__service.create_currency(
            currency_id=input_model.id, currency_name=input_model.name, currency_dollar_conversion_rate=input_model.dollar_conversion_rate)

        return Response(status=HTTPStatus.CREATED) if currency else Response(status=HTTPStatus.CONFLICT)

    @namespace.doc(description="Updates name or dollar convertion rate of given currency", body=UpdateCurrencyInputModel.schema_model())
    @namespace.response(HTTPStatus.NO_CONTENT.value, 'Currency Updated sucessfuly')
    @namespace.response(HTTPStatus.NOT_FOUND.value, 'Currency not found to update')
    @namespace.response(HTTPStatus.INTERNAL_SERVER_ERROR.value, 'Internal server error')
    async def patch(self,):
        body = request.get_data()
        if not body:
            raise ValidationError('Request body is required')

        input_model = UpdateCurrencyInputModel(**json.loads(body))
        self.__service.update_currency(
            currency_id=input_model.id, currency_name=input_model.name, currency_dollar_conversion_rate=input_model.dollar_conversion_rate)

    @namespace.doc(description="Deletes a currency")
    @namespace.param("currency_id", max_length=10, required=True)
    @namespace.response(HTTPStatus.NO_CONTENT.value, 'Currency deleted sucessfully')
    @namespace.response(HTTPStatus.NOT_FOUND.value, 'Currency to be deleted not found')
    @namespace.response(HTTPStatus.INTERNAL_SERVER_ERROR.value, 'Internal server error')
    async def delete(self,):
        currency_id = self.__get_currency_id()
        self.__service.delete_currency(currency_id)
        return Response(status=HTTPStatus.NO_CONTENT)

    def __get_currency_id(self,):
        currency_id = request.args.get('currency_id')
        if currency_id and len(currency_id) <= 10:
            return currency_id.upper()
        raise ValidationError(
            "The field currency_id is mandatory", HTTPStatus.BAD_REQUEST)
