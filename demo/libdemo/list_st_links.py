import requests
from bs4 import BeautifulSoup

#WEBSITE = "http://www.srikanthtechnologies.com"
WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
contents = resp.text
bs = BeautifulSoup(contents, "html.parser")

for a in bs.find_all("a"):
    href = a['href']
    if href == "#":
        continue

    if not href.startswith("http"):  # found relative url
        href = WEBSITE + "/" + href   # get absolute url

    print(href)


