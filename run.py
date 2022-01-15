import json 
import requests 
import math



def checkPrice(tokenAddress):
    tokenprice = 'https://deep-index.moralis.io/api/v2/erc20/' + tokenAddress + '/price?chain=bsc' 
    headers = {
        'x-api-key': 'ytipLdzPd60Qe8nNCp3bBJrTGy8vJCdLUZGOsCHuk8MG3vXWL5KgOgpdSvQSvhCa'
        }
    response = requests.request("GET", tokenprice, headers=headers)
    resp = response.json()  
    price = resp['usdPrice'] 
    return price

print("{:.10f}".format(checkPrice(X)) + "USD")
