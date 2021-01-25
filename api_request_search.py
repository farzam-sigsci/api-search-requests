import requests
import json
import csv
import sys
from pprint import pprint

url = "https://dashboard.signalsciences.net/api/v0/corps/YOUR_CORP/sites/YOUR_SITE/requests?limit=1000&page=1&q=tag%3Aforcefulbrowsing%20from%3A-1d"

payload={}
headers = {
  'x-api-user': 'FILL IN',
  'x-api-token': 'FILL IN',
  'Content-Type': 'application/json',
  'from': '-1d'
}

response = requests.request("GET", url, headers=headers, data=payload)

with open('data_daily.json', 'w') as outfile:
  sys.stdout = outfile
  pprint(response.json())
