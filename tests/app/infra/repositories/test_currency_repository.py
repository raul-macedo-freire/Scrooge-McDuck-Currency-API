from unittest import TestCase
from mongoengine import connect, disconnect
from app.core.entities.currency import Currency
from app.infra.models import currency_model
from app.infra.models.currency_model import CurrencyModel
from app.infra.repositories.currency_repository import CurrencyRepository


from tests.tests_helper.factory.factory import Factory


class TestCurrencyRepository(TestCase):

    def __init__(self, *args, **kwargs):
        self.database_test_name = 'mongoenginetest'
        self.connection = connect(
            self.database_test_name, host='mongomock://localhost', alias='currency')
        self.repo = CurrencyRepository()
        self.__factory = Factory()
        super(TestCurrencyRepository, self).__init__(*args, **kwargs)

    def setUp(self):
        self.connection.drop_database(self.database_test_name)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_save(self):
        currency = self.__factory.factory_currency(False, False)

        entity_saved = self.repo.save(currency)

        fresh_currency = CurrencyModel.objects().first()
        self.__assert_currency_model_values(fresh_currency, currency)
        self.assertTrue(entity_saved != None)
        self.assertEqual(entity_saved, currency)

    def test_save_many(self):
        currency_list = [self.__factory.factory_currency(
            False, False) for _ in range(2)]

        entities_saved = self.repo.save_many(currency_list)

        fresh_currencies = CurrencyModel.objects()

        for i, fresh_currency in enumerate(fresh_currencies):
            self.__assert_currency_model_values(
                fresh_currency, currency_list[i])
            self.assertEqual(entities_saved[i], currency_list[i])

    def test_find(self,):
        currency_model = self.__factory.factory_currency_model(False, False)
        CurrencyModel.save(currency_model)

        found_currency = self.repo.find(currency_model.id)

        self.__assert_currency_values(found_currency, currency_model)

    def test_find_nothing_for_deleted_data(self,):
        currency_model = self.__factory.factory_currency_model(True, True)
        CurrencyModel.save(currency_model)
        found_currency = self.repo.find(currency_model.id)
        db_data = CurrencyModel.objects()
        self.assertIsNone(found_currency)
        self.assertTrue(len(db_data) > 0)

    def test_delete(self,):
        currency_model = self.__factory.factory_currency_model(False, False)
        CurrencyModel.save(currency_model)

        resp = self.repo.delete(currency_model.id)

        found = CurrencyModel.objects()
        self.assertIsNone(resp)
        self.assertEqual(len(found), 0)

    def test_delete_return_none_if_id_doesnt_exist(self,):
        try:
            resp = self.repo.delete('some_id')
        except Exception as ex:
            print(ex)
        found = CurrencyModel.objects()
        self.assertIsNone(resp)
        self.assertEqual(len(found), 0)

    def test_find_all(self,):
        currency_range = range(5)
        currency_models = [self.__factory.factory_currency_model(False, False)
                           for _ in currency_range]
        CurrencyModel.objects.insert(currency_models)

        currencies = self.repo.find_all()
        for i, currency in enumerate(currencies):
            self.__assert_currency_values(currency, currency_models[i])

    def test_find_all_doesnt_find_deleted_data(self,):
        currency_range = range(5)
        currency_models_deleted = [self.__factory.factory_currency_model(True, True)
                                   for _ in currency_range]
        currency_models = [self.__factory.factory_currency_model(False, False)
                           for _ in currency_range]

        CurrencyModel.objects.insert(currency_models_deleted+currency_models)

        currencies = self.repo.find_all()
        self.assertEqual(len(currencies), len(currency_range))
        for i, currency in enumerate(currencies):
            self.__assert_currency_values(currency, currency_models[i])

    def __assert_currency_model_values(self, fresh_currency_model: CurrencyModel, currency: Currency):
        self.assertTrue(type(currency), Currency)
        self.assertEqual(fresh_currency_model.id, currency.id)
        self.assertEqual(fresh_currency_model.currency_name, currency.name)
        self.assertEqual(fresh_currency_model.dollar_conversion_rate,
                         currency.dollar_conversion_rate)
        self.assertEqual(fresh_currency_model.created_at, currency.created_at)
        self.assertEqual(fresh_currency_model.deleted_at, currency.deleted_at)

    def __assert_currency_values(self, fresh_currency: Currency, currency_model: CurrencyModel):
        self.assertTrue(type(currency_model), CurrencyModel)
        self.assertEqual(fresh_currency.id, currency_model.id)
        self.assertEqual(fresh_currency.name, currency_model.currency_name)
        self.assertEqual(fresh_currency.dollar_conversion_rate,
                         currency_model.dollar_conversion_rate)
        self.assertEqual(fresh_currency.created_at, currency_model.created_at)
        self.assertEqual(fresh_currency.updated_at, currency_model.updated_at)
        self.assertEqual(fresh_currency.deleted_at, currency_model.deleted_at)
