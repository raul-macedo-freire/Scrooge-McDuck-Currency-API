[![Test](https://github.com/raul-macedo-freire/currency-challenge-bravo-api/actions/workflows/Tests.yml/badge.svg)](https://github.com/raul-macedo-freire/currency-challenge-bravo-api/actions/workflows/Tests.yml)

[![Python 3.10.6](https://img.shields.io/badge/python-3.10.6-blue.svg)](https://www.python.org/downloads/release/python-3106/)

<p align="center">
  <img src="https://gifs.eco.br/wp-content/uploads/2021/09/imagens-e-gifs-do-tio-patinhas-5.gif" alt="!LET'S MAKE SOME MONEY LAD/LASS!(read with scottish accent)"/>
</p>

# 🦆 💲**SCROOGE MCDUCK CURRENCY FLASK API- CURRENCY CHALLENGE BRAVO**💲 🦆

</br>

ScroogeMcDuckCurrencyApi é um aplicativo de suporte a várias moedas, que permite ao usuário:

-   Converter valores de uma moeda para outras
-   Cria sua própria moeda com base na taxa de câmbio do dólar
-   Execute métodos RestFull básicos, como: Localizar, atualizar e excluir.

Esta API foi construída com[APP Flask](https://flask.palletsprojects.com/en/2.2.x/)e[Flask-restx](https://flask-restx.readthedocs.io/en/latest/), portanto pode ser utilizado integrado com[Swagger.ui](https://swagger.io/tools/swagger-ui/)interface.

## 📖**Idiomas disponíveis do Documentos:**

-   [Inglês](README.md)
-   [Português](README.pt.md)
-   [Espanhol](README.es.md)

## 👷**Serviço de terceiros - OpenExchangeAPI**

</br>

Uma vez que as taxas de câmbio estão constantemente sendo atualizadas, não é possível para um ser humano continuar atualizando todos os dados de moedas, a fim de converter valores dinamicamente. Por esse motivo, ScroogeMcDuckCurrencyApi é integrado com[API do OpenExchange](https://openexchangerates.org/)serviço gratuito de moeda Api.</br>No entanto, uma vez que o usuário verifica uma moeda ou quaisquer métodos, ScroogeMcDuckCurrencyApi não consultará diretamente o OpenExchange, mas seu próprio banco de dados. Os dados provenientes do OpenExchange são atualizados dinamicamente de acordo com a configuração de agendamento do sistema, a ser explicado em[configuração](#api-configuration)seção.

## 💵**Taxa de conversão do dólar**

A API de moeda do Tio Patinhas funciona com base na taxa de conversão do dólar, portanto, cada moeda deve ser convertida de seu valor para dólar, antes de ser convertida em outra moeda.

Vamos fazer um exemplo:

Se você quiser converter a moeda do próprio Tio Patinhas para BRL (moeda brasileira), você deve ter a taxa de conversão da moeda do McDuck's dólar, ou seja, quantas moedas do McDuck você precisa para transformá-la em um doller.

Digamos que a taxa de conversão do dólar do McDuck seja 2 (o que não é possível, pois ele é muito rico), então você precisa de 2 moedas do McDuck para fazer um dólar. Hoje em dia (e isso é impressionantemente assustador), a taxa de conversão do dólar de BRL para USD (identificador universal do dólar) é de 5,22. Para converter 5 McDuck's em Reais, fazemos:

(5/2)\*5.22 = 13.05 Reais

<p align="center">
  <img src="https://images.gr-assets.com/hostedimages/1576518017ra/28622252.gif" alt="Math is fantastic!"/>
</p>

## 💉**Injeção de dependência**

Para usar conceitos e ferramentas de injeção de dependência, esta API usa python[injetor](https://injector.readthedocs.io/en/latest/). Eu tive que encontrar algumas lógicas para fazê-lo funcionar bem, o que funcionou,~~Na minha humilde opinião~~, muito bem e parece muito bem.

## ⌚**Agendador**

ScroogeMcDuckCurrencyApi executa operações cronológicas para atualizar o banco de dados com a API OpenExchange.</br>Apesar do fato de que o python possui muitas bibliotecas para agendamento e enfileiramento, como:[schedule](https://github.com/dbader/schedule),[cronista](https://github.com/kiorky/croniter)ou[flask-cronjob](https://pypi.org/project/flask-crontab/), este serviço não utiliza tais ferramentas, pretendendo buscar uma abordagem mais enxuta.

## 📔**Armazenamento de dados**

</br>

ScroogeMcDuckCurrencyApi tem um[mongoDb](https://www.mongodb.com/en-us)banco de dados para armazenar dados do OpenExchange e inseridos pelos usuários.</br>O uso do mongo facilita o uso do fantástico[outro motor](https://docs.mongoengine.org/tutorial.html)pacote ORM python, pois fornece uma visão muito melhor do código com modelos de objeto.

## ❗❗**Isenção de responsabilidade**

</br>
ScroogeMcDuckCurrencyApi has a pretty nice interface and performs just fine given it's objective, however it does not perform automatic updates for  currencies that are not provided by OpenExchange API, in that way, in order to update custom currencies, the user must keep it up to date manually or create a provider to perform updates on the API from its source. 

</br>
</br>

O código-fonte ScroogeMcDuckCurrencyApi tem alguns comentários que valem a pena procurar, que você pode verificar, procurando por`NOTES:`

## ⚙️**Configuração da API**

</br>

Apesar de esta aplicação utilizar apenas recursos gratuitos, a vida nem sempre é um mar de rosas, temos alguns segredos a esconder 🕵️ e algumas configurações a fazer.
Na verdade, só temos um segredo, a ser explicado a seguir.</br>

#### <u>ID do aplicativo OpenExchange</u>

</br>

O OpenExchange fornece uma API de uso gratuito, mas, para usar essa API, você deve ter uma conta no open exchange. Por isso:

-   Vá para[Página de login do OpenExchange](https://openexchangerates.org/signup/free)
-   crie sua conta
-   Verifique o seu APP ID em[página de IDs de APP](https://openexchangerates.org/account/app-ids)
-   Substitua o campo`{YOUR_OPENEXCHANGE_APP_ID_COMES_HERE}`no[arquivo docker-compose](docker-compose.yml)

    **Obs:**Se você pretende executar este aplicativo usando um IDE, basta salvar o ID do aplicativo Open Exchange como uma variável de ambiente com o nome`OPENEXCHANGE_APP_ID`.

#### <u>Agendador de atualização do banco de dados</u>

</br>

Por padrão, a API atualiza o banco de dados com a API openExchange a cada 10 minutos, mas se você quiser aumentar ou diminuir (quem sabe?) esse atraso, basta substituir o valor de`UPDATE_CURRENCIES_MINUTES_SCHEDULE`no[arquivo docker-compose](docker-compose.yml)

**Obs:**Assim como o[seção anterior](#uopenexchange-app-idu), se você estiver executando a API localmente em seu IDE, atualize a variável de ambiente`UPDATE_CURRENCIES_MINUTES_SCHEDULE`.

## 🏃**Executando o aplicativo**

Primeiro de tudo, clone o repositório:

    git clone git@github.com:raul-macedo-freire/currency-challenge-bravo-api.git

Para executar a API, você tem duas opções:

-   Executar com docker-compose
-   Executar com um IDE

#### <b>Executar com docker-compose</b>

Se você não está acostumado a trabalhar com docker, dê uma olhada no[documentos](https://docs.docker.com/get-started/overview/)e instalar[docker-compose](https://docs.docker.com/compose/).

Depois de se acostumar com o docker, configure o arquivo docker-compose, de acordo com o[Seção de configuração da API](#api-configuration)

Na pasta do projeto, execute:

```bash
docker compose up
```

Verifique a interface do aplicativo em: https&#x3A;//localhost:5000/swagger

### <b>Executar com um IDE</b>

Salve as variáveis ​​de ambiente de acordo com o[Observações de configuração da API](#api-configuration).

Se você não estiver usando um gerenciador de dependências, recomendo usar algo como[pytest](https://docs.pytest.org/en/latest/getting-started.html#install-pytest).

Se você não quiser usar o pyenv e instalar dependências no ambiente python global (quem sabe?), pule para[Instalando Dependências](#uinstalling-dependenciesu)seção.

#### <u>Configuração do ambiente Python:</u>

Este projeto usa python 3.10.6, vou considerar que você está usando pyenv para gerenciamento de versão python, caso não esteja, verifique a configuração do gerenciador de dependências e siga os passos abaixo de forma equivalente.

Verifique a versão do python:

```bash
python --version
```

Caso não esteja utilizando a versão 3.10.6, verifique se a possui instalada, com:

```bash
pyenv versions
```

Caso contrário, instale a versão com:

```bash
pyenv install -v 3.10.6
```

Em seguida, defina a versão localmente:

```bash
pyenv local 3.10.6
```

No diretório raiz da API, crie um novo ambiente python:

```bash
python -m venv <virtual-env-name>
```

Ative o ambiente virtual

```bash
source <virtual-env-name>/bin/activate
```

se estiver usando windows acesse o ambiente virtual com:

```bash
 .\venv\Scripts\activate
```

#### <u>Instalando Dependências:</u>

    pip install -r requirements.txt

### <u>Executando o aplicativo:</u>

Se você estiver usando[VSCODE](https://code.visualstudio.com/), já forneci um script de execução com um[lançar arquivo](./.vscode/launch.json), então se for o caso:

-   Salve as variáveis ​​de ambiente em um`.env`arquivo
-   Execute o`run application`script com atalho F5.

Se você não estiver usando o VSCODE,~~comece a usar~~, dê uma olhada na configuração do seu IDE e execute o aplicativo a partir do`run.py`root e não se esqueça de salvar as variáveis ​​de ambiente em configuration.

Verifique a interface do aplicativo em: https&#x3A;//localhost:5000/swagger

**!!!OBSERVAÇÃO!!!:**Se você executar o aplicativo dessa forma, não poderá executar solicitações de API, pois o banco de dados não estará em execução.

## 🧪<b>Testes de execução</b>

### <u>testes de unidade</u>

Para executar todos os testes de unidade, use:

```bash
python -m pytest
```

### <u>Testes de estresse</u>

Este aplicativo usa a ferramenta k6.io para realizar testes de estresse.
Verifica a[documentação do k6](https://k6.io/docs/getting-started/installation/)para instalar a ferramenta.

Para executar o teste, na raiz do aplicativo, entre na pasta de testes:

```bash
cd ./tests
```

E faça o teste:

```bash
k6 run sovietic_attack.js 
```

**Obs1:**Não se esqueça de ter o aplicativo instalado e funcionando antes de executar o teste

**Obs2:**Para tornar os testes mais precisos para a API, cada endpoint deve ser testado individualmente, seguindo as[considerações](https://k6.io/blog/how-to-generate-a-constant-request-rate-with-the-new-scenarios-api/), se você quiser testar cada endpoint, descomente o endpoint e comente o resto (ou não, ninguém manda em você`¯\_(ツ)_/¯`).

</br>

## 😎**Considerações Finais**

Se você é muito ruim com exemplos e não sabe como começar a experimentar a API, dê uma olhada em[carteiro_exemplos](postman_examples/ScroogeMcDuckCurrencyApi.postman_collection.json). Se você não conhece o carteiro, eu recomendo fortemente que você[De uma chance](https://www.postman.com/):D

# Documentação resumida:

-   [penv](http://blog.abraseucodigo.com.br/instalando-qualquer-versao-do-python-no-linux-macosx-utilizando-pyenv.html)
-   [Pytest](https://docs.pytest.org/en/latest/getting-started.html#install-pytest)
-   [Frasco](https://flask.palletsprojects.com/en/2.2.x/)
-   [Flask-Restx](https://flask-restx.readthedocs.io/en/latest/)
-   [outro motor](https://docs.mongoengine.org/tutorial.html)
-   [API do OpenExchange](https://openexchangerates.org/)
-   [Docker-Compose](docker-compose.yml)
-   [ksh](https://k6.io/docs/)

# 

## Estrutura do Projeto

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
