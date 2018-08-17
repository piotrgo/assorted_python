import json
import requests
from bs4 import BeautifulSoup


def get_investment_status():
    "This calculates investment value based on current share price and exch rate GBP/PLN"
    knos_url = 'summary/company-summary/GB00BZ0D6727GBGBXSSMM.html'
    starting_sp = 138
    starting_ex_rate = 5.80
    assets =
    inv_ini = assets*starting_ex_rate*starting_sp

    ex_rate = requests.get('http://api.fixer.io/latest?base=GBP&symbols=PLN')
    ex_rate = json.loads(ex_rate.text)
    ex_rate = ex_rate['rates']['PLN']
    knos_sp = requests.get('http://www.londonstockexchange.com/exchange/prices-and-markets/stocks/'+knos_url)
    soup = BeautifulSoup(knos_sp.text, 'html.parser')
    a = soup.find("td", class_="name")
    knos_sp = a.find_next("td").text

    inv_val = assets*float(knos_sp)*float(ex_rate)

    inv_status = [inv_ini/100, inv_val/100, (inv_val-inv_ini)/inv_ini*100]
    return inv_status

print(get_investment_status())