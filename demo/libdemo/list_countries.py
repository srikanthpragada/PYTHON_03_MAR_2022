
import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for c in countries:
    name = c['name']['common']
    capital = c.get('capital',[''])[0]
    population = c['population']
    print(f"{name:50} {capital:30} {population:10}")
