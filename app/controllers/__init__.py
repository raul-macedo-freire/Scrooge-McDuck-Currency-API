from typing import List
from app.controllers.base_controller import BaseController
from app.controllers.currency_converter_controller import CurrencyConverterController
from app.controllers.currency_controller import CurrencyController
from app.controllers.currencies_controller import CurrenciesController

CONTROLLERS: List[BaseController] = [CurrencyConverterController,
                                     CurrencyController, CurrenciesController]
