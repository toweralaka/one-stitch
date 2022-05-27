import pandas as pd
import requests
from bs4 import BeautifulSoup

class StoreItem:
   """
   A general class to store item data concisely.
   """

   def __init__(self, name, price, manufacturer):
       self.name = name
       self.price = price
       self.manufacturer = manufacturer

def web(page,WebUrl):
    items = list()
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'core'}):
            name = link.get('data-name')
            price = link.get('data-price')
            manufacturer = link.get('data-brand')
            item = StoreItem(name, price, manufacturer)
            items.append(item)
    df = pd.DataFrame(
        {
            "name": [item.name for item in items],
            "price": [item.price for item in items],
            "manufacturer": [item.manufacturer for item in items],
        }
    )
    df.to_csv("scaped.csv", index=False)

web(1,'https://www.jumia.com.ng/catalog/?q=mobile+phones')


