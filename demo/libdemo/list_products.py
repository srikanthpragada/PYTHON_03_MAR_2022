from bs4 import BeautifulSoup

with open("products.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, "xml")

for p in bs.find_all("product"):
    name = p.find("name").text
    price = p.find("price").text
    print(f"{name:20}  {price:10}")
