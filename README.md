[![Test](https://github.com/raul-macedo-freire/currency-challenge-bravo-api/actions/workflows/Tests.yml/badge.svg
)](https://github.com/raul-macedo-freire/currency-challenge-bravo-api/actions/workflows/Tests.yml)

[![Python 3.10.6](https://img.shields.io/badge/python-3.10.6-blue.svg)](https://www.python.org/downloads/release/python-3106/)


<p align="center">
  <img src="https://gifs.eco.br/wp-content/uploads/2021/09/imagens-e-gifs-do-tio-patinhas-5.gif" alt="!LET'S MAKE SOME MONEY LAD/LASS!(read with scottish accent)"/>
</p>

# 🦆 💲**SCROOGE MCDUCK CURRENCY FLASK API- CURRENCY CHALLENGE BRAVO**💲 🦆
</br>

ScroogeMcDuckCurrencyApi is a multi currency support application, that allows the user to:
-  Convert amounts from a  currencie to anothers
-  Creates it's own currency based on dollar exchange rate 
-  Execute basic RestFull methods, such as: Find, update, and delete.

This API was built with [Flask APP](https://flask.palletsprojects.com/en/2.2.x/) and [Flask-restx](https://flask-restx.readthedocs.io/en/latest/), therefore it can be used integrated with [Swagger.ui](https://swagger.io/tools/swagger-ui/) interface. 

## 📖**Docs Available Languages:**
- [English](README.md)
- [Portuguese](README.pt.md)
- [Spanish](README.es.md)



## 👷**Third-Party Service - OpenExchangeAPI**
</br>

Since Currency ratios are constantly getting updated, it is not possible for a humanbeeing to keep updating all currencies data, in order to convert amounts dynamically. For that reason, ScroogeMcDuckCurrencyApi is integrated with [OpenExchangeAPI](https://openexchangerates.org/) free Api currency service.</br> 
Howerver, once the user checks for a currency or whatever methods, ScroogeMcDuckCurrencyApi will not directly consult OpenExchange, but it's own database. Data that comes from OpenExchange is dynamically updated according to system scheduling configuration, to be explained in [configuration](#api-configuration) section.

## 💵 **Dollar conversion rate**

ScroogeMcDuckCurrencyApi works based on dollar conversion rate, thus every currency must be converted from its value to dollar, before getting converted into another currency.

Let's make an example:

If you want to convert Scrooge McDuck's own currency into BRL (Brazilian's currency), you must have McDuck's currency dollar conversion rate, or how many McDuck's coins you need to make it into a doller.

Let's say McDuck's dollar conversion rate is 2 (which is not possible since he is way too much rich), then you need 2 McDuck's coins to make a dollar. Nowadays (and this is impressively scary), the dollar conversion rate from BRL to USD(Dollar universal identifier) is 5.22. To convert 5 McDuck's into Reais, we do:

(5/2)*5.22 = 13.05 Reais

<p align="center">
  <img src="https://images.gr-assets.com/hostedimages/1576518017ra/28622252.gif" alt="Math is fantastic!"/>
</p>



## 💉**Dependency Injection**
In order to use dependency injection concepts and tools, this API uses python [Injector](https://injector.readthedocs.io/en/latest/). I had to come around with some logics to make it work fine wich performed, ~~IMHO~~, just fine and looks pretty well.  

## ⌚**Scheduler**

ScroogeMcDuckCurrencyApi perform cronologic operations to update the database with OpenExchange api.</br>
Dispite the fact that python has planty of libraries for scheduling and queueing, such as: [schedule](https://github.com/dbader/schedule),[Croniter](https://github.com/kiorky/croniter) or [flask-cronjob](https://pypi.org/project/flask-crontab/)
, this service does not use such tools, intenting to look for a leanest approach.

## 📔**Data storage**
</br>

ScroogeMcDuckCurrencyApi has a [mongoDb](https://www.mongodb.com/en-us) database to store data from OpenExchange and inputed by users.</br>
Using mongo makes easy to use the fantastic [mongoengine](https://docs.mongoengine.org/tutorial.html) python ORM package, since it provides a much better view of the code with object models.

## ❗❗ **Disclaimer**
</br>
ScroogeMcDuckCurrencyApi has a pretty nice interface and performs just fine given it's objective, however it does not perform automatic updates for  currencies that are not provided by OpenExchange API, in that way, in order to update custom currencies, the user must keep it up to date manually or create a provider to perform updates on the API from its source. 

</br>
</br>

ScroogeMcDuckCurrencyApi source code has some worth looking comments that you can check, by looking for `` NOTES: ``

## ⚙️ **Api Configuration**
</br>

Despite the fact that this application only uses free resources, life is not always a bed of roses, we have some secrets to hide 🕵️ and some config to do.
In fact, we only have one secret, to be explained as it follows. 
</br>

#### <u>OpenExchange APP ID</u>
</br>

OpenExchange provides a Free to use API, but, in order to use this API, you must have an account at open exchange. For that:
- Go to [OpenExchange Sign in Page](https://openexchangerates.org/signup/free) 
- Create your account
- Check for your APP ID at [APP IDs page](https://openexchangerates.org/account/app-ids)
- Replace the field `{YOUR_OPENEXCHANGE_APP_ID_COMES_HERE}` at [docker-compose file](docker-compose.yml)
 
 **Obs:** If you intent to run this application using a IDE, just save your Open Exchange app id as an environment variable with name ``OPENEXCHANGE_APP_ID``.

#### <u>Database Update Scheduler</u>
</br>

By default, the API updates the database with openExchange api every 10 minutes, but if you want to increase or decrease (who knows?) this delay, just replace the value of ``UPDATE_CURRENCIES_MINUTES_SCHEDULE`` at [docker-compose file](docker-compose.yml)

**Obs:** Just like the [previous section](#uopenexchange-app-idu), if you are running the api locally in your IDE, update the environment variable  ``UPDATE_CURRENCIES_MINUTES_SCHEDULE``.



## 🏃**Running the application**

First of all, clone the repository:
```
git clone git@github.com:raul-macedo-freire/currency-challenge-bravo-api.git
```

In order to run the api, you have two options:
- Run with docker-compose
- Run with an IDE

#### <b>Run with docker-compose</b>

If you are not used to work with docker, take a look at the [docs](https://docs.docker.com/get-started/overview/) and install [docker-compose](https://docs.docker.com/compose/).

After getting used to docker, configure the docker-compose file, according to the [Api Configuration Section](#api-configuration)

In the project Folder, run:

```bash
docker compose up
```

Check the application interface at : https://localhost:5000/swagger

### <b>Run with an IDE</b>

Save the environment variables according to the [Api Configuration Observations](#api-configuration).


If you are not using a dependency manager, I strongly recommend using something like [pytest](https://docs.pytest.org/en/latest/getting-started.html#install-pytest).

If you don't want to use pyenv and go for it installing dependencies into global python environment(who knows?), skip to [Installing Dependencies](#uinstalling-dependenciesu) section.


#### <u>Setup Python Environmnet:</u>

This project uses python 3.10.6, I'll consider that you're using pyenv for python version management, if you're not, check for you dependencies manager configuration and follow the steps below in a equivalent way.

Check the python version:
```bash
python --version
```
 
If you're not using version 3.10.6, check if you have it installed, with:
```bash
pyenv versions
```
If you don't, install the version with:
```bash
pyenv install -v 3.10.6
```
Then set the version locally:
```bash
pyenv local 3.10.6
```

In the API root directory, create a new python environment:

```bash
python -m venv <virtual-env-name>
```

Activate the virtual environment

```bash
source <virtual-env-name>/bin/activate
```

if you're using windows access the virtual environment with:
```bash
 .\venv\Scripts\activate
```

#### <u>Installing Dependencies:</u>

```
pip install -r requirements.txt
```

### <u>Running the app:</u>


If you're using [VSCODE](https://code.visualstudio.com/), I have already provided a Run script with a [launch file](./.vscode/launch.json), so if it's the case:
- Save the environment variables in a `.env` file 
- Run the `run application` script with F5 shortcut.

If you're not using VSCODE, ~~start using it~~, take a look at your IDE configuration and run the app from the `run.py` root file and don't forget to save the environment variables in configuration.

Check the application interface at : https://localhost:5000/swagger

**!!!NOTE!!!:** If you run the app like this, you won't be able to run api requests, since the database won't be running. 


## 🧪 <b> Running Tests</b>

### <u> Unit tests</u>

To run all unit tests, use:

```bash
python -m pytest
```

### <u> Stress tests</u>

This application uses k6.io tool to perform stress tests.
Check the [k6 documentation](https://k6.io/docs/getting-started/installation/) to install the tool. 

To run the test, from the application root, enter the tests folder:

```bash
cd ./tests
```
And run the test:

```bash
k6 run sovietic_attack.js 
```

**Obs1:** Don't forget to have the application up and running before running the test

**Obs2:** In order to performe more accurate  the tests for the API, each endpoint must be tested individually, following the [considerations](https://k6.io/blog/how-to-generate-a-constant-request-rate-with-the-new-scenarios-api/), if you want to test each endpoint, uncomment the endpoint and comment the rest (or not, nobody rules you `¯\_(ツ)_/¯` ).

</br>

## 😎 **Final Considerations**

If you are really bad with examples and don't know how to start trying the API, take a look at [postman_examples](postman_examples/ScroogeMcDuckCurrencyApi.postman_collection.json). If you don't know postman, I strongly advise you to [give it a try](https://www.postman.com/) :D 

# Summarized documentation:
- [Pyenv](http://blog.abraseucodigo.com.br/instalando-qualquer-versao-do-python-no-linux-macosx-utilizando-pyenv.html)
- [Pytest](https://docs.pytest.org/en/latest/getting-started.html#install-pytest)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/)
- [Mongoengine](https://docs.mongoengine.org/tutorial.html)
- [OpenExchangeAPI](https://openexchangerates.org/)
- [Docker-Compose](docker-compose.yml)
- [k6](https://k6.io/docs/)
  
#


## Project Structure

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
