import requests

name = input("Enter username :")
resp = requests.get(f"https://api.github.com/users/{name}")

if resp.status_code != 200:
    print("Sorry! Could not get details.")
    exit()

details = resp.json()
print('Name          : ', details['name'])
print('Company       : ', details['company'])
print('No. of Repos  : ', details['public_repos'])

