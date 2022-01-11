import requests


# ACCESS_KEY  =


class ExchangeRateApi:

    def __init__(self):
        self.url = f"http://api.exchangeratesapi.io/v1/latest?access_key={ACCESS_KEY}"
        self.exchange_rates = self.fetch_latest_rates()

    def fetch_latest_rates(self):
        response = requests.get(self.url)
        return response.json()


class CurrencyCalculator:

    def __init__(self, exchange_api):
        self.exchange_api = exchange_api

    def convert_from_euro(self, to_currency, amount):
        exchange_rate = self.exchange_api.exchange_rates["rates"][to_currency]

        return round(exchange_rate * amount, 2)

    def convert_to_euro(self, from_currency, amount):
        exchange_rate = self.exchange_api.exchange_rates["rates"][from_currency]

        return round(amount / exchange_rate, 2)

    def convert(self, from_currency, to_currency, amount):
        euros = self.convert_to_euro(from_currency, amount)
        return self.convert_from_euro(to_currency, euros)
