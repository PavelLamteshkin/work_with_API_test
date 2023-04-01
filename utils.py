import requests
import json
from datetime import datetime

def get_currency_rate(base):

    """будет запрашивать курс валюты от API и возвращать его в виде float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"

    headers = {
        "apikey": "PqLpB9dXCVJgapkHKxKCJOfz9CUXIgLt"
    }

    response = requests.get(url, headers=headers, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data):

    """будет сохранять данные в JSON-файл"""

    pass


def main():

    """будет запрашивать у пользователя название валюты, выводить курс валюты в консоль,
    сохранять данные в json файл и предлагать пользователю выбрать действие: продолжить или выйти."""

    while True:
        currency = input("Введите название валюты USD или EUR: ")
        if currency not in ('USD', 'EUR'):
            print("Некорректный ввод")
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

        print(f"Курс {currency} к рублю {rate}")

        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Что дальше? 1 - продолжить, 2 - завершить ')
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print('Нужно ввести 1 или 2')


if __name__ == "__main__":
    main()
    # get_currency_rate('USD')
