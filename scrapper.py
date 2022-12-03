from bs4 import BeautifulSoup
import sqlite3 as sql
import requests
#https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30


def find_last_page():
    last_page = 0
    return last_page

def main():
    counter = 1
    URL = "https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content , 'html5lib')
    div = soup.find_all("div", {'class': 'product col-6 col-sm-4 pt-3 pb-md-3'})
    for element in div:
        a = element.find('a', {'class':'product__icon d-flex justify-content-center align-items-center'})
        href = a['href']
        sale = element.find("div", {'class': 'product__yousavepercent'}).text.strip()
        first_price = element.find('del', {"class": "price --max"}).text
        sale_price = element.find('strong', {'class' : 'price --max-exists'}).text
        print(f"{counter}. {first_price} {sale} = {sale_price}")
        counter += 1

main()