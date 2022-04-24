from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "cafacd31356509b7058f"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()

    return data

def print_currencies(currencies):
    for name, currency  in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol","") #retourne le symbol ou chaîne vide
        print(f"{_id} - {name} - {symbol}")




data = get_currencies()
print_currencies(data)