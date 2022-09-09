from http import HTTPStatus
from dataclasses import asdict
from flask_restx import Namespace
from flask import request
from injector import inject
from app.controllers.base_controller import BaseController
from app.core.exceptions.client_errors.validation_error import ValidationError
from app.services.interfaces.abstract_converter_service import AbstractConverterService
from app.models.input_model.currency_converter_query_parameters_input_model import CurrencyConverterQueryParametersInputModel
namespace = Namespace('Currency')


class CurrencyConverterController(BaseController):
    @inject
    def __init__(self, service: AbstractConverterService, **kwargs):
        self.__service = service
        super().__init__(**kwargs)

    @namespace.response(HTTPStatus.BAD_REQUEST.value, 'Missing fields or parameters validation issues')
    @namespace.response(HTTPStatus.NOT_FOUND.value, 'One of the given currencies were not found')
    @namespace.response(HTTPStatus.OK.value, "The amount converted")
    @namespace.param("amount", "Amount to convert", required=True, type=float)
    @namespace.param("to_currency", "Identifier of currency to convert TO, only three letters", required=True)
    @namespace.param("from_currency", "Identifier of currency to convert FROM, only three letters", required=True)
    async def get(self):
        params = self.__validate_request_parameters()
        return self.__service.convert_currency(
            **asdict(params)
        )

    def __validate_request_parameters(self,) -> CurrencyConverterQueryParametersInputModel:
        from_currency = request.args.get(
            'from_currency', type=str)
        to_currency = request.args.get(
            'to_currency', type=str)

        amount = request.args.get(
            'amount', type=float)

        return CurrencyConverterQueryParametersInputModel(
            from_currency=from_currency,
            to_currency=to_currency,
            amount=amount,
        )
