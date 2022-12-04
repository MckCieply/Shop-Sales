from bs4 import BeautifulSoup
import sqlite3 as sql
import requests
#https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30
#gotta make it show 100 sales per page to lower working time
#perhaps store in db old prices to see real sale
conn = sql.connect('sales.db')
cur = conn.cursor()
def first_db_innit():
    cur.execute("""CREATE TABLE sales(
                sale_id INT PRIMARY KEY,
                product_id INT,
                old_price INT,
                sale_percent INT,
                new_price INT,
                link TEXT)
                """)

def db_query(prod_id, old_price, sale_percent, sale_price):
    cur.execute("""INSERT INTO sales (product_id, old_price, sale_percent, new_price) 
                VALUES (?,?,?,?)""",)

def find_last_page():
    URL = "https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content , 'html5lib')
    ul = soup.find('ul', {'class': 's_paging__item pagination mb-2 mb-sm-3'})
    li = ul.find_all('li', {'class' : 'pagination__element --item'})
    last_page = int(li[-1].text)
    return last_page

def main(last_page):
    counter = 1
    for page in range(0,last_page):
        URL = f"https://www.ezebra.pl/pl/promotions/promocja.html?&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&filter_price=0-30&counter={page}"
        request = requests.get(URL)
        soup = BeautifulSoup(request.content , 'html5lib')
        div = soup.find_all("div", {'class': 'product col-6 col-sm-4 pt-3 pb-md-3'})
        for element in div:
            a = element.find('a', {'class':'product__icon d-flex justify-content-center align-items-center'})
            href = a['href']
            prod_id = div['data-id']
            sale = element.find("div", {'class': 'product__yousavepercent'}).text.strip()
            old_price = element.find('del', {"class": "price --max"}).text
            sale_price = element.find('strong', {'class' : 'price --max-exists'}).text
            print(f"{counter}. {old_price} {sale} = {sale_price}")
            counter += 1
#first_db_innit()
# last_page = find_last_page()
# main(last_page)
