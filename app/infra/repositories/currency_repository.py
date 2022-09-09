from typing import List
from app.core.entities.currency import Currency
from app.infra.models.currency_model import CurrencyModel
from app.infra.repositories.interfaces.abstract_currency_repository import AbstractCurrencyRepository


class CurrencyRepository(AbstractCurrencyRepository):
    def __init__(self,):
        self.__model = CurrencyModel

    def save(self, currency: Currency):
        model = self.__map_to_model(currency)
        return self.__map_from_model(model.save())

    def save_many(self, currencies: List[Currency]):
        objects = [self.__map_to_model(entity) for entity in currencies]
        models = self.__model.objects.insert(objects)
        return [self.__map_from_model(obj) for obj in models]

    def delete(self, _id: str):
        if model := self.__model.objects(id=_id):
            model.delete()
        return

    def find(self, id: str) -> Currency | None:
        if model := self.__model.objects(id=id, deleted_at=None):
            return self.__map_from_model(model.first())
        return None

    def find_all(self, size=10, page=1) -> List[Currency] | None:
        offset = (page - 1) * size
        models = self.__model.objects(deleted_at=None).skip(offset).limit(size)
        return [self.__map_from_model(obj) for obj in models]

    def __map_from_model(self, model: CurrencyModel) -> Currency:
        return Currency(
            id=model.id,
            name=model.currency_name,
            dollar_conversion_rate=model.dollar_conversion_rate,
            created_at=model.created_at,
            updated_at=getattr(model, "updated_at", None),
            deleted_at=getattr(model, "deleted_at", None)
        )

    def __map_to_model(self, entity: Currency) -> CurrencyModel:
        return CurrencyModel(
            id=entity.id,
            currency_name=entity.name,
            dollar_conversion_rate=entity.dollar_conversion_rate,
            created_at=entity.created_at,
            updated_at=getattr(entity, "updated_at", None),
            deleted_at=getattr(entity, "deleted_at", None)

        )
