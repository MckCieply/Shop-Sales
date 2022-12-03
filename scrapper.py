from bs4 import BeautifulSoup
import sqlite3 as sql
import requests
#https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30


def find_last_page():
    URL = "https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content , 'html5lib')
    ul = soup.find('ul', {'class': 's_paging__item pagination mb-2 mb-sm-3'})
    li = ul.find_all('li', {'class' : 'pagination__element --item'})
    last_page = li[-1].text
    return last_page

def main(last_page):
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

last_page = find_last_page()
main(last_page)
