import requests
from bs4 import BeautifulSoup

url = "https://www.coingecko.com/en"  # change to whatever your url is
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

souptable = BeautifulSoup(page.text, "html.parser")

rows = soup.find("table", {"id": "gecko-table"}).find("tbody").find_all("tr")

for row in rows:
    currency =  row.find("span", {"class": "coin-content-name"})
    price =  row.find("span", {"class": "currency-exchangable"})
    output = str(currency.get_text()) + ", " + str(price.get_text())
    print output