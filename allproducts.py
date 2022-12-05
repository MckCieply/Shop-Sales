#Scrapping and storing all relevent procucts
#Aiming to compare 'old' prices with 'sales' prices
#therefore gotta scrape all stock and store in separate db/table
#https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455
from bs4 import BeautifulSoup
import sqlite3 as sql
import requests

def find_last_page():
    URL = "https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content , 'html5lib')
    ul = soup.find('ul', {'class': 's_paging__item pagination mb-2 mb-sm-3'})
    li = ul.find_all('li', {'class' : 'pagination__element --item'})
    last_page = int(li[-1].text)
    return last_page

last_page = find_last_page