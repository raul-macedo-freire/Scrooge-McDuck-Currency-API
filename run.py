import os
import threading
from flask import Flask
import configparser

from app.config.config_helper import EnvInterpolation
from app import ScroogeMcDuckCurrencyApi, cron_scheduler, UpdateDbWorker

config = configparser.ConfigParser(interpolation=EnvInterpolation())
config.read('./app/config/config.ini')
app = Flask(__name__)

api = ScroogeMcDuckCurrencyApi(
    app,
    config,
    title="Scrooge McDuck Currency API",
    default="currency",
    description="""
        This is a currency API. 
        Convert your currencies from any of the available in my base or create your own :D
        
        Don't forget to check for universal currencies codes: https://pt.iban.com/currency-codes""",
    default_label='',
    doc='/swagger')

worker = api.ApiInjector.get(UpdateDbWorker)


if __name__ == "__main__":
    # Runs the application in two threads
    # NOTE: I Believe creating my own SSL certificate would be a better approach, but for the purpose
    # of creating the API for challenge bravo, I believe that OpenSSL just do fine
    threading.Thread(
        target=lambda: app.run(
            host="0.0.0.0",
            port=os.environ.get('PORT'),
            debug=True,
            use_reloader=False,
            ssl_context='adhoc')).start()

    update_db_schedule = os.environ.get('UPDATE_CURRENCIES_MINUTES_SCHEDULE')

    if update_db_schedule:
        threading.Thread(
            target=lambda: cron_scheduler(worker.run, float(update_db_schedule))).start()
