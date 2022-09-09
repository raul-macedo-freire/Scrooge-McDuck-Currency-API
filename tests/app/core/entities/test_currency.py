from datetime import datetime
from unittest import TestCase, mock
from faker import Faker

from app.core.entities.currency import Currency
from tests.tests_helper.factory.factory import Factory


class TestCurrency(TestCase):
    def setUp(self,):
        self.faker = Faker()
        self.factory = Factory()

    @mock.patch('datetime.datetime',  wraps=datetime)
    def test_create(self, mock_datetime):  # sourcery skip: avoid-builtin-shadow
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        id = self.factory.factory_id()
        name = self.faker.name(),
        dollar_conversion_rate = self.faker.pyfloat(positive=True)

        entity = Currency.create(
            id,
            dollar_conversion_rate, name)

        self.assertEqual(id, entity.id)
        self.assertEqual(name, entity.name)
        self.assertEqual(dollar_conversion_rate, entity.dollar_conversion_rate)
        self.assertEqual(fake_date_now, entity.created_at)
        self.assertIsNone(entity.updated_at)
        self.assertIsNone(entity.deleted_at)

    @mock.patch('datetime.datetime',  wraps=datetime)
    # sourcery skip: avoid-builtin-shadow
    def test_create_without_name(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        id = self.factory.factory_id()
        dollar_conversion_rate = self.faker.pyfloat(positive=True)

        entity = Currency.create(
            id,
            dollar_conversion_rate)

        self.assertEqual(id, entity.id)
        self.assertIsNone(entity.name)
        self.assertEqual(dollar_conversion_rate, entity.dollar_conversion_rate)
        self.assertEqual(fake_date_now, entity.created_at)
        self.assertIsNone(entity.updated_at)
        self.assertIsNone(entity.deleted_at)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_update(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, False)

        name = self.faker.name()
        conversion_rate = self.faker.pyfloat(positive=True)
        entity.update(name, conversion_rate)

        self.assertEqual(entity.updated_at, fake_date_now)
        self.assertEqual(entity.name, name)
        self.assertEqual(entity.dollar_conversion_rate, conversion_rate)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_update_only_name(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, False)
        entity_before = entity
        name = self.faker.name()

        entity.update(name)

        self.assertEqual(entity.name, name)
        self.assertEqual(entity.dollar_conversion_rate,
                         entity_before.dollar_conversion_rate)
        self.assertEqual(entity.updated_at, fake_date_now)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_update_only_conversion_rate(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, False)
        entity_before = entity
        conversion_rate = self.faker.pyfloat(positive=True)

        entity.update(dollar_conversion_rate=conversion_rate)

        self.assertEqual(entity.name, entity_before.name)
        self.assertEqual(entity.dollar_conversion_rate,
                         conversion_rate)
        self.assertEqual(entity.updated_at, fake_date_now)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_delete(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, False)
        entity_before = entity

        entity.delete()

        self.assertEqual(entity.deleted_at, fake_date_now)
        self.assertEqual(entity.updated_at, entity_before.updated_at)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_recreate(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, True)
        entity_before = entity
        name = self.faker.name()
        conversion_rate = self.faker.pyfloat(positive=True)

        entity.recreate(name, conversion_rate)

        self.assertEqual(entity.name, name)
        self.assertEqual(entity.dollar_conversion_rate, conversion_rate)
        self.assertEqual(entity.created_at, entity_before.created_at)
        self.assertEqual(entity.updated_at, fake_date_now)
        self.assertIsNone(entity.deleted_at)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_recreate_with_name(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, True)
        entity_before = entity
        name = self.faker.name()

        entity.recreate(name)

        self.assertEqual(entity.name, name)
        self.assertEqual(entity.dollar_conversion_rate,
                         entity_before.dollar_conversion_rate)
        self.assertEqual(entity.created_at, entity_before.created_at)
        self.assertEqual(entity.updated_at, fake_date_now)
        self.assertIsNone(entity.deleted_at)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_recreate_with_conversion_rate(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, True)
        entity_before = entity
        conversion_rate = self.faker.pyfloat(positive=True)

        entity.recreate(dollar_conversion_rate=conversion_rate)

        self.assertEqual(entity.name, entity_before.name)
        self.assertEqual(entity.dollar_conversion_rate,
                         conversion_rate)
        self.assertEqual(entity.created_at, entity_before.created_at)
        self.assertEqual(entity.updated_at, fake_date_now)
        self.assertIsNone(entity.deleted_at)

    @ mock.patch('datetime.datetime',  wraps=datetime)
    def test_recreate_with_nothing(self, mock_datetime):
        fake_date_now = self.faker.date_time()
        mock_datetime.now.return_value = fake_date_now

        entity = self.factory.factory_currency(True, True)
        entity_before = entity

        entity.recreate()

        self.assertEqual(entity.name, entity_before.name)
        self.assertEqual(entity.dollar_conversion_rate,
                         entity_before.dollar_conversion_rate)
        self.assertEqual(entity.created_at, entity_before.created_at)
        self.assertEqual(entity.updated_at, fake_date_now)
        self.assertIsNone(entity.deleted_at)
