import re
from configparser import ConfigParser
from flask import Flask
from flask_restx import Api, Resource
from mongoengine.connection import connect
from app.controllers import CONTROLLERS
from app.ioc import IoC
from flask_injector import FlaskInjector


from app.middleware.exception_middleware import ExceptionMiddleware


class ScroogeMcDuckCurrencyApi(Api):
    def __init__(self, app: Flask, config: ConfigParser, **kwargs):
        self.__config = config
        self.__app = app
        ioc = IoC(self.__config)

        super().__init__(self.__app, **kwargs)
        self.__add_resources()
        self.__register_middleware()
        self.__connect_db()
        flask_injector = FlaskInjector(app=self.__app, modules=[ioc.configure])
        self.ApiInjector = flask_injector.injector

    def __register_middleware(self,):
        self.app.wsgi_app = ExceptionMiddleware(self.app.wsgi_app)

    def __add_resources(self,):
        for controller in CONTROLLERS:
            route_path = self.__format_controller_name(controller)
            self.add_resource(controller,
                              f"/{route_path}/")
            if controller.models:
                for model in controller.models:
                    self.models[model.name] = model

    def __format_controller_name(self, controller: Resource):
        class_name: str = controller.__name__
        names = re.findall('[a-zA-Z][^A-Z]*', class_name)
        names.remove('Controller')
        names_in_lower = [name.lower() for name in names]
        return '_'.join(names_in_lower)

    def __connect_db(self,):
        connect(self.__config['DEFAULT']['DATABASE_NAME'],
                host=self.__config['DEFAULT']['HOST'],
                username=self.__config['DEFAULT']['USERNAME'],
                password=self.__config['DEFAULT']['PASSWORD'],
                authentication_source='admin',
                alias="currency",
                connect=False)
