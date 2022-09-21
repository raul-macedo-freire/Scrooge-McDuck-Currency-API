[![Test](https://github.com/raul-macedo-freire/currency-challenge-bravo-api/actions/workflows/Tests.yml/badge.svg)](https://github.com/raul-macedo-freire/currency-challenge-bravo-api/actions/workflows/Tests.yml)

[![Python 3.10.6](https://img.shields.io/badge/python-3.10.6-blue.svg)](https://www.python.org/downloads/release/python-3106/)

<p align="center">
  <img src="https://gifs.eco.br/wp-content/uploads/2021/09/imagens-e-gifs-do-tio-patinhas-5.gif" alt="!LET'S MAKE SOME MONEY LAD/LASS!(read with scottish accent)"/>
</p>

# 🦆 💲**SCROOGE MCDUCK CURRENCY FLASK API- CURRENCY CHALLENGE BRAVO**💲 🦆

</br>

ScroogeMcDuckCurrencyApi es una aplicación compatible con varias monedas que permite al usuario:

-   Convertir cantidades de una moneda a otras
-   Crea su propia moneda basada en el tipo de cambio del dólar
-   Ejecute métodos RestFull básicos, como: Buscar, actualizar y eliminar.

Esta API fue construida con[APLICACIÓN Matraz](https://flask.palletsprojects.com/en/2.2.x/) and [Matraz-restx](https://flask-restx.readthedocs.io/en/latest/), por lo que se puede utilizar integrado con[Swagger.ui](https://swagger.io/tools/swagger-ui/)interfaz.

## 📖**Documentos Idiomas disponibles:**

-   [inglés](README.md)
-   [portugués](README.pt.md)
-   [español](README.es.md)

## 👷**Servicio de terceros - OpenExchangeAPI**

</br>

Dado que las proporciones de divisas se actualizan constantemente, no es posible que un ser humano siga actualizando todos los datos de divisas para convertir cantidades dinámicamente. Por esa razón, ScroogeMcDuckCurrencyApi está integrado con[API de intercambio abierto](https://openexchangerates.org/)Servicio de moneda Api gratuito.</br> 
Howerver, once the user checks for a currency or whatever methods, ScroogeMcDuckCurrencyApi will not directly consult OpenExchange, but it's own database. Data that comes from OpenExchange is dynamically updated according to system scheduling configuration, to be explained in [configuración](#api-configuration)sección.

## 💵**Tasa de conversión del dólar**

Scrooge McDuck Currency Api funciona en función de la tasa de conversión del dólar, por lo que cada moneda debe convertirse de su valor a dólar, antes de convertirse a otra moneda.

Hagamos un ejemplo:

Si desea convertir la propia moneda de Scrooge McDuck en BRL (la moneda brasileña), debe tener la tasa de conversión de dólares de la moneda de McDuck, o cuántas monedas de McDuck necesita para convertirla en una muñeca.

Digamos que la tasa de conversión de dólares de McDuck es 2 (lo cual no es posible ya que es demasiado rico), entonces necesitas 2 monedas de McDuck para hacer un dólar. Hoy en día (y esto es impresionantemente aterrador), la tasa de conversión del dólar de BRL a USD (identificador universal del dólar) es de 5,22. Para convertir 5 McDuck's en Reales, hacemos:

(5/2)\*5,22 = 13,05 reales

<p align="center">
  <img src="https://images.gr-assets.com/hostedimages/1576518017ra/28622252.gif" alt="Math is fantastic!"/>
</p>

## 💉**Inyección de dependencia**

Para usar conceptos y herramientas de inyección de dependencia, esta API usa python[Inyector](https://injector.readthedocs.io/en/latest/). Tuve que encontrar algunas lógicas para que funcionara bien, lo que funcionó,~~En mi humilde opinión~~~, muy bien y se ve bastante bien.

## ⌚**programador**

ScroogeMcDuckCurrencyApi realiza operaciones cronológicas para actualizar la base de datos con OpenExchange api.</br>A pesar de que python tiene muchas bibliotecas para programar y poner en cola, como:[calendario](https://github.com/dbader/schedule),[cronista](https://github.com/kiorky/croniter)o[matraz-cronjob](https://pypi.org/project/flask-crontab/), este servicio no utiliza tales herramientas, con la intención de buscar un enfoque más eficiente.

## 📔**Almacenamiento de datos**

</br>

ScroogeMcDuckCurrencyApi tiene un[MongoDb](https://www.mongodb.com/en-us)base de datos para almacenar datos de OpenExchange e ingresados ​​por los usuarios.</br>El uso de mongo facilita el uso de la fantástica[otro motor](https://docs.mongoengine.org/tutorial.html)paquete ORM de python, ya que proporciona una vista mucho mejor del código con modelos de objetos.

## ❗❗**Descargo de responsabilidad**

</br>
ScroogeMcDuckCurrencyApi has a pretty nice interface and performs just fine given it's objective, however it does not perform automatic updates for  currencies that are not provided by OpenExchange API, in that way, in order to update custom currencies, the user must keep it up to date manually or create a provider to perform updates on the API from its source. 

</br>
</br>

El código fuente de ScroogeMcDuckCurrencyApi tiene algunos comentarios que vale la pena buscar y que puede verificar buscando`NOTES:`

## ⚙️**Configuración API**

</br>

A pesar de que esta aplicación solo utiliza recursos gratuitos, la vida no siempre es un camino de rosas, tenemos algunos secretos que esconder 🕵️ y algunas configuraciones que hacer.
De hecho, solo tenemos un secreto, que se explica a continuación.</br>

#### <u>ID de aplicación de OpenExchange</u>

</br>

OpenExchange proporciona una API de uso gratuito, pero, para usar esta API, debe tener una cuenta en Open Exchange. Para eso:

-   Ir[Página de inicio de sesión de OpenExchange](https://openexchangerates.org/signup/free)
-   Crea tu cuenta
-   Verifique su ID de aplicación en[Página ID de la aplicación](https://openexchangerates.org/account/app-ids)
-   Reemplazar el campo`{YOUR_OPENEXCHANGE_APP_ID_COMES_HERE}`a[archivo docker-compose](docker-compose.yml)

    **Obs:**Si tiene la intención de ejecutar esta aplicación usando un IDE, simplemente guarde su ID de aplicación de Open Exchange como una variable de entorno con nombre`OPENEXCHANGE_APP_ID`.

#### <u>Programador de actualización de base de datos</u>

</br>

Por defecto, la API actualiza la base de datos con openExchange api cada 10 minutos, pero si desea aumentar o disminuir (¿quién sabe?) este retraso, simplemente reemplace el valor de`UPDATE_CURRENCIES_MINUTES_SCHEDULE`a[archivo docker-compose](docker-compose.yml)

**Obs:**Al igual que el[sección previa](#uopenexchange-app-idu), si está ejecutando la API localmente en su IDE, actualice la variable de entorno`UPDATE_CURRENCIES_MINUTES_SCHEDULE`.

## 🏃**Ejecutando la aplicación**

En primer lugar, clone el repositorio:

    git clone git@github.com:raul-macedo-freire/currency-challenge-bravo-api.git

Para ejecutar la API, tiene dos opciones:

-   Ejecutar con docker-compose
-   Ejecutar con un IDE

#### <b>Ejecutar con docker-compose</b>

Si no estás acostumbrado a trabajar con docker, echa un vistazo a la[documentos](https://docs.docker.com/get-started/overview/)e instalar[docker-compose](https://docs.docker.com/compose/).

Después de acostumbrarse a docker, configure el archivo docker-compose, de acuerdo con el[Sección de configuración de API](#api-configuration)

En la carpeta del proyecto, ejecute:

```bash
docker compose up
```

Verifique la interfaz de la aplicación en: https&#x3A;//localhost:5000/swagger

### <b>Ejecutar con un IDE</b>

Guarde las variables de entorno de acuerdo con el[Observaciones de configuración de API](#api-configuration).

Si no está utilizando un administrador de dependencias, le recomiendo usar algo como[pytest](https://docs.pytest.org/en/latest/getting-started.html#install-pytest).

Si no desea usar pyenv e instalar dependencias en el entorno global de python (¿quién sabe?), salte a[Instalación de dependencias](#uinstalling-dependenciesu)sección.

#### <u>Configurar el entorno de Python:</u>

Este proyecto usa python 3.10.6, consideraré que está usando pyenv para la administración de versiones de python, si no lo está, verifique la configuración del administrador de dependencias y siga los pasos a continuación de manera equivalente.

Compruebe la versión de Python:

```bash
python --version
```

Si no estás usando la versión 3.10.6, verifica si la tienes instalada, con:

```bash
pyenv versions
```

Si no lo hace, instale la versión con:

```bash
pyenv install -v 3.10.6
```

Luego configure la versión localmente:

```bash
pyenv local 3.10.6
```

En el directorio raíz de la API, cree un nuevo entorno de python:

```bash
python -m venv <virtual-env-name>
```

Activar el entorno virtual

```bash
source <virtual-env-name>/bin/activate
```

si está usando Windows, acceda al entorno virtual con:

```bash
 .\venv\Scripts\activate
```

#### <u>Instalación de dependencias:</u>

    pip install -r requirements.txt

### <u>Ejecutando la aplicación:</u>

si estás usando[VSCODE](https://code.visualstudio.com/), ya he proporcionado un script de ejecución con un[iniciar archivo](./.vscode/launch.json), así que si es el caso:

-   Guarde las variables de entorno en un`.env`expediente
-   Run the `run application`secuencia de comandos con el atajo F5.

Si no está utilizando VSCODE,~~empieza a usarlo~~, eche un vistazo a la configuración de su IDE y ejecute la aplicación desde el`run.py`archivo raíz y no olvide guardar las variables de entorno en la configuración.

Verifique la interfaz de la aplicación en: https&#x3A;//localhost:5000/swagger

**!!!¡¡¡NOTA!!!:**Si ejecuta la aplicación de esta manera, no podrá ejecutar solicitudes de API, ya que la base de datos no se ejecutará.

## 🧪<b>Ejecución de pruebas</b>

### <u>Pruebas unitarias</u>

Para ejecutar todas las pruebas unitarias, utilice:

```bash
python -m pytest
```

### <u>Pruebas de estrés</u>

Esta aplicación utiliza la herramienta k6.io para realizar pruebas de estrés.
Comprobar el[documentación k6](https://k6.io/docs/getting-started/installation/)para instalar la herramienta.

Para ejecutar la prueba, desde la raíz de la aplicación, ingrese a la carpeta de pruebas:

```bash
cd ./tests
```

Y ejecuta la prueba:

```bash
k6 run sovietic_attack.js 
```

**Obs1:**No olvide tener la aplicación funcionando antes de ejecutar la prueba.

**Obs2:**Para realizar pruebas más precisas para la API, cada punto final debe probarse individualmente, siguiendo las[consideraciones](https://k6.io/blog/how-to-generate-a-constant-request-rate-with-the-new-scenarios-api/), si quieres probar cada endpoint, descomenta el endpoint y comenta el resto (o no, nadie te manda`¯\_(ツ)_/¯`).

</br>

## 😎**Consideraciones finales**

Si eres muy malo con los ejemplos y no sabes cómo empezar a probar la API, echa un vistazo a[cartero_ejemplos](postman_examples/ScroogeMcDuckCurrencyApi.postman_collection.json). Si no conoce al cartero, le recomiendo encarecidamente que[darle una oportunidad](https://www.postman.com/):D

# Documentación resumida:

-   [penv](http://blog.abraseucodigo.com.br/instalando-qualquer-versao-do-python-no-linux-macosx-utilizando-pyenv.html)
-   [Pytest](https://docs.pytest.org/en/latest/getting-started.html#install-pytest)
-   [Matraz](https://flask.palletsprojects.com/en/2.2.x/)
-   [Matraz-Restx](https://flask-restx.readthedocs.io/en/latest/)
-   [El motor](https://docs.mongoengine.org/tutorial.html)
-   [API de intercambio abierto](https://openexchangerates.org/)
-   [Docker-Componer](docker-compose.yml)
-   [ksh](https://k6.io/docs/)

# 

## Estructura del proyecto

```
currency-challenge-bravo-api
├─ .github
│  └─ workflows
│     ├─ readme.yml
│     └─ Tests.yml
├─ .gitignore
├─ .vscode
│  ├─ launch.json
│  └─ settings.json
├─ app
│  ├─ api.py
│  ├─ config
│  │  ├─ config.ini
│  │  └─ config_helper.py
│  ├─ controllers
│  │  ├─ base_controller.py
│  │  ├─ currencies_controller.py
│  │  ├─ currency_controller.py
│  │  ├─ currency_converter_controller.py
│  │  └─ __init__.py
│  ├─ core
│  │  ├─ entities
│  │  │  ├─ currency.py
│  │  │  └─ __init__.py
│  │  ├─ exceptions
│  │  │  ├─ base_exceptions.py
│  │  │  ├─ client_errors
│  │  │  │  ├─ currency_not_found.py
│  │  │  │  ├─ parameters_missing_error.py
│  │  │  │  ├─ validation_error.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ server_errors
│  │  │  │  ├─ configuration_error.py
│  │  │  │  ├─ external_service_error.py
│  │  │  │  ├─ infra_service_unauthorized.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ infra
│  │  ├─ models
│  │  │  ├─ currency_model.py
│  │  │  └─ __init__.py
│  │  ├─ repositories
│  │  │  ├─ currency_repository.py
│  │  │  ├─ interfaces
│  │  │  │  ├─ abstract_currency_repository.py
│  │  │  │  └─ __init__.py
│  │  │  └─ __init__.py
│  │  ├─ services
│  │  │  ├─ interfaces
│  │  │  │  ├─ abstract_external_currency_service.py
│  │  │  │  └─ __init__.py
│  │  │  ├─ open_exchanges_api_service.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ ioc.py
│  ├─ middleware
│  │  ├─ exception_middleware.py
│  │  └─ __init__.py
│  ├─ models
│  │  ├─ input_model
│  │  │  ├─ base_input_model.py
│  │  │  ├─ currency_converter_query_parameters_input_model.py
│  │  │  ├─ currency_input_model.py
│  │  │  ├─ update_currency_input_model.py
│  │  │  └─ __init__.py
│  │  ├─ view_model
│  │  │  ├─ base_view_model.py
│  │  │  ├─ get_currencies_view_model.py
│  │  │  ├─ get_currency_view_model.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ scheduler.py
│  ├─ services
│  │  ├─ converter_service.py
│  │  ├─ currency_service.py
│  │  ├─ interfaces
│  │  │  ├─ abstract_converter_service.py
│  │  │  ├─ abstract_currency_service.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ update_db_worker.py
│  └─ __init__.py
├─ docker-compose.yml
├─ Dockerfile
├─ LICENSE
├─ mongo-init.js
├─ README.es.md
├─ README.md
├─ README.pt.md
├─ requirements.txt
├─ run.py
└─ tests
   ├─ app
   │  ├─ core
   │  │  ├─ entities
   │  │  │  ├─ test_currency.py
   │  │  │  └─ __init__.py
   │  │  └─ __init__.py
   │  ├─ infra
   │  │  ├─ repositories
   │  │  │  ├─ test_currency_repository.py
   │  │  │  └─ __init__.py
   │  │  ├─ services
   │  │  │  ├─ test_open_exchanges_api_service.py
   │  │  │  └─ __init__.py
   │  │  └─ __init__.py
   │  ├─ services
   │  │  ├─ test_converter_service.py
   │  │  ├─ test_currency_service.py
   │  │  └─ __ini__.py
   │  └─ __init__.py
   ├─ sovietic_attack.js
   ├─ tests_helper
   │  ├─ factory
   │  │  ├─ factory.py
   │  │  └─ __init__.py
   │  ├─ requests_mock.py
   │  └─ __init__.py
   └─ __init__.py

```
