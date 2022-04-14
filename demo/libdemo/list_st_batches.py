import requests
from bs4 import BeautifulSoup
from datetime import *

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
contents = resp.text
bs = BeautifulSoup(contents, "html.parser")

table = bs.find(id = "ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")
for row in rows[1:]:
    cols = row.find_all("td")
    course = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text   # in DD-MON format
    sysdate = datetime.now()
    # add current year to stdate
    stdate = f"{stdate}-{sysdate.year}"
    sd = datetime.strptime(stdate,"%d-%b-%Y")
    days = (sd - sysdate).days
    if days >= 0:
        print(f"{course:30} {timings:15} {days} to go")





