#Scrapping and storing all relevent procucts
#Aiming to compare 'old' prices with 'sales' prices
#therefore gotta scrape all stock and store in separate db/table
#https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455
from bs4 import BeautifulSoup
import sqlite3 as sql
import requests
from datetime import date
import time
import re

start_time = time.time()
tdate = date.today()

conn = sql.connect('shopsales/sales.db')
cur = conn.cursor()
def first_db_innit():
    cur.execute("""CREATE TABLE stock(
                product_id INTEGER PRIMARY KEY,
                price INTEGER,
                link TEXT,
                updated DATE)
                """)

def db_query_stock(prod_id, price, link, tdate):
    try:
        cur.execute("""INSERT INTO stock (product_id, price, link, updated) 
                    VALUES (?,?,?,?)""", (prod_id, price, link, tdate))
    except sql.IntegrityError: pass
    
def db_query_names(prod_id, name, brand):
    try:
        cur.execute("""INSERT INTO names (product_id, name, brand)
                    VALUES (?,?,?)""", (prod_id, name, brand))
    except sql.IntegrityError: pass  

def find_last_page():
    URL = "https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content , 'html5lib')
    ul = soup.find('ul', {'class': 's_paging__item pagination mb-2 mb-sm-3'})
    li = ul.find_all('li', {'class' : 'pagination__element --item'})
    last_page = int(li[-1].text)
    return last_page

def main(last_page):
    counter = 0
    for page in range(0,last_page):
        URL = f"https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&counter={page}"
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html5lib')
        div = soup.find_all("div", {"class" :  re.compile(r"\bproduct col-6 col-sm-4 pt-3 pb-md-3\b")})
        for element in div:
            try:
                price = element.find("del", {'class':'price --max'}).text
            except:
                price = element.find('strong', {'class' : 'price'}).text

            a = element.find('a', {'class':'product__icon d-flex justify-content-center align-items-center'})
            href = "https://www.ezebra.pl" + a['href']
            prod_id = element['data-id']
            #print(f"ID: {prod_id} \n link: {href} \n Price: {price}")
            db_query_stock(prod_id, price, href, tdate)
            
            try:
                name = a['title']
                brand = a['data-brand']
            except:
                name = brand = "missing"
            db_query_names(prod_id, name, brand)
            
            counter += 1

    print(f"Commiting all of: {counter} products...")
    conn.commit()

#first_db_innit()

if __name__ == "__main__":
    last_page = find_last_page()
    main(last_page)
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")