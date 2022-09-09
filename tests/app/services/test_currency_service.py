from unittest import TestCase, mock
from app.core.entities.currency import Currency
from app.core.exceptions.client_errors.currency_not_found import CurrencyNotFound

from app.services.currency_service import CurrencyService
from tests.tests_helper.factory.factory import Factory


class TestCurrencyService(TestCase):
    def setUp(self) -> None:
        self.factory = Factory()
        self.repo = mock.MagicMock()
        self.infra_service = mock.MagicMock()
        self.service = CurrencyService(self.repo, self.infra_service)
        self.__id = self.factory.factory_id()

        return super().setUp()

    def test_create_currency(self):
        currency = self.factory.factory_currency()

        self.repo.find.return_value = None
        self.repo.save.return_value = currency
        result = self.service.create_currency(
            currency.id, currency.dollar_conversion_rate, currency.name)

        self.repo.find.assert_called_once()
        self.repo.save.assert_called_once()
        self.assertEqual(result, currency)

    def test_create_currency_that_already_exist_return_none(self,):
        currency = self.factory.factory_currency()
        self.repo.find.return_value = currency

        result = self.service.create_currency(
            currency.id, currency.dollar_conversion_rate, currency.name)

        self.assertIsNone(result)
        self.repo.find.assert_called_once()
        self.repo.save.assert_not_called()

    def test_create_currency_that_is_deleted_recreate_it(self):
        currency = self.factory.factory_currency(create_deleted=True)

        recreated_currency = mock.MagicMock()
        recreated_currency.recreate.return_value = currency
        self.repo.find.return_value = recreated_currency

        self.repo.save.return_value = currency

        result = self.service.create_currency(
            currency.id, currency.dollar_conversion_rate, currency.name)

        self.assertEqual(result, currency)
        self.repo.save.assert_called_once()
        recreated_currency.recreate.assert_called_once()

    def test_find_all(self):
        """This test only calls infrastructure method wich is beeing already tested in infrastructure tests"""
        ...

    def test_find_currency_return_currency(self,):
        currency = self.factory.factory_currency()
        self.repo.find.return_value = currency

        result = self.service.buscar_currency(self.__id)

        self.repo.find.assert_called_once_with(self.__id)
        self.assertEqual(result, currency)

    def test_find_currency_raises_not_found(self,):
        self.repo.find.return_value = None

        self.assertRaises(CurrencyNotFound,
                          self.service.buscar_currency, *(self.__id,))

        self.repo.find.assert_called_once_with(self.__id)

    def test_update_currency_successfully(self,):
        currency_updated = self.factory.factory_currency(create_updated=True)
        currency = mock.MagicMock()

        self.repo.find.return_value = currency
        currency.update.return_value = currency_updated

        self.repo.save.return_value = currency_updated

        result = self.service.update_currency(
            currency_updated.id,
            currency_updated.dollar_conversion_rate,
            currency_updated.name)

        self.assertEqual(result, currency_updated)

        self.repo.find.assert_called_once()
        self.repo.save.assert_called_once()
        currency.update.assert_called_once()

    def test_update_currency_fail_for_currency_not_found(self,):
        currency_updated = self.factory.factory_currency(
            create_updated=True)
        currency = mock.MagicMock()

        self.repo.find.return_value = None
        currency.update.return_value = currency_updated

        self.assertRaises(CurrencyNotFound, self.service.update_currency, *(
            currency_updated.id,
            currency_updated.dollar_conversion_rate,
            currency_updated.name))

        self.repo.find.assert_called_once()
        self.repo.save.assert_not_called()

    def test_update_batch_currencies_successfully(self,):

        rates_quantity = 5
        new_ratios_dict = self.factory.factory_open_exchange_response(rates_quantity)[
            'rates']
        self.infra_service.get_all_latest_currencies.return_value = new_ratios_dict
        self.repo.find.return_value = None

        result = self.service.update_batch_currencies()

        self.assertIsNone(result)
        self.assertEqual(self.repo.save_many.call_count, 1)
        self.repo.save.assert_not_called()

    def test_delete_currency(self,):
        currency_deleted = self.factory.factory_currency(
            create_deleted=True)
        currency = mock.MagicMock()

        self.repo.find.return_value = currency
        currency.delete.return_value = currency_deleted

        self.repo.save.return_value = currency_deleted

        result = self.service.delete_currency(
            currency_deleted.id)

        self.assertEqual(result, currency_deleted)

        self.repo.find.assert_called_once()
        self.repo.save.assert_called_once()
        self.repo.delete.assert_not_called()
        currency.delete.assert_called_once()

    def test_delete_currency_fails_for_currency_not_found(self,):

        self.repo.find.return_value = None

        self.assertRaises(CurrencyNotFound,
                          self.service.delete_currency, *(self.__id,))

        self.repo.find.assert_called_once()
        self.repo.save.assert_not_called()
        self.repo.delete.assert_not_called()
