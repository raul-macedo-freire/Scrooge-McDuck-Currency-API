from typing import List
from flask_restx import Resource
from flask_restx import Model


class BaseController(Resource):
    models: List[Model] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
