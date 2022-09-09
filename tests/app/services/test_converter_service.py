from unittest import TestCase, mock
from faker import Faker
from app.core.exceptions.client_errors.currency_not_found import CurrencyNotFound

from app.services.converter_service import ConverterService
from tests.tests_helper.factory.factory import Factory


class TestConverterService(TestCase):
    def setUp(self,):
        self.factory = Factory()
        self.faker = Faker()
        self.__mock_repo = mock.MagicMock()
        self.service = ConverterService(self.__mock_repo)

    def test_convert_currency(self):
        currency1 = self.factory.factory_currency()
        currency1.dollar_conversion_rate = 4
        currency2 = self.factory.factory_currency()
        currency2.dollar_conversion_rate = 2

        amount = 40
        expected_result = 20
        self.__mock_repo.find.side_effect = [currency1, currency2]

        result = self.service.convert_currency(
            currency1.id, currency2.id, amount)

        self.assertEqual(result, expected_result)
        self.assertEqual(self.__mock_repo.find.call_count, 2)

    def test_convert_currency_convert_to_same_currency(self,):
        currency = self.factory.factory_currency()
        currency.dollar_conversion_rate = 2

        self.__mock_repo.find.side_effect = [currency, currency]
        amount = 20
        expected_result = 20

        result = self.service.convert_currency(
            currency.id, currency.id, amount)

        self.assertEqual(result, expected_result)
        self.__mock_repo.find.assert_called_with(currency.id)

    def test_convert_currency_raises_when_first_currency_doesnt_exist(self,):
        from_currency = self.factory.factory_id()
        to_currency = self.factory.factory_id()
        amount = self.faker.pyfloat(positive=True)

        currency = self.factory.factory_currency()
        currency.id = from_currency
        self.__mock_repo.find.side_effect = [None, currency]

        self.assertRaises(
            CurrencyNotFound, self.service.convert_currency, *(from_currency, to_currency, amount))

        self.__mock_repo.find.assert_called_once_with(from_currency)

    def test_convert_currency_raises_when_second_currency_doesnt_exist(self,):
        currency = self.factory.factory_currency()

        self.__mock_repo.find.side_effect = [currency, None]

        from_currency = self.factory.factory_id()
        to_currency = self.factory.factory_id()
        amount = self.faker.pyfloat(positive=True)

        self.assertRaises(
            CurrencyNotFound, self.service.convert_currency, *(from_currency, to_currency, amount))
        self.__mock_repo.find.assert_called()
        self.assertEqual(self.__mock_repo.find.call_count, 2)
