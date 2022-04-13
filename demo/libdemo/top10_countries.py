import requests

resp = requests.get("https://restcountries.com/v3.1/all")
countries = resp.json()

for c in sorted(countries, key=lambda cnt: cnt['population'], reverse=True)[:10]:
    name = c['name']['common']
    population = c['population']
    area = c['area']
    print(f"{name:30}  {population:10}  {area:10.0f} {population // area:5.0f}")
