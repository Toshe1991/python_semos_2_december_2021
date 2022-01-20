### DRIVER MODUL ###

from currency_calculator import ExchangeRateApi, CurrencyCalculator

e_api = ExchangeRateApi()
print(e_api.fetch_latest_rates())
# calculator = CurrencyCalculator(e_api)
#
# value = calculator.convert_from_euro("USD", 100)
# # print(value)
#
# value_euros = calculator.convert_to_euro("MKD", 6896)
# # print(value_euros)
#
# value_dollars = calculator.convert("USD", "AUD", 600)
# print(value_dollars)