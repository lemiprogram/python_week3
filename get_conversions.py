import requests
url = "https://api.currencyapi.com/v3/latest?apikey=cur_live_2793BMA5K43K5Z336MjHA9cHrwlbQkH5cuwGKheK&currencies=EUR%2CUSD%2CCAD%2CKES%2CRUB%2CJPY%2CKRW%2CCNY&base_currency=GBP"
response = requests.get(url)
data = response.json()
conversions = data["data"]
def get_conversions():
    return conversions
def calc_conversions(origin,conversion):
    return origin*conversions[conversion]["value"]