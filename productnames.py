#Scrpit scrapping all product names and create table to stick 'em to prod IDs
##https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455
from bs4 import BeautifulSoup
import requests
import sqlite3 as sql
from allproducts import find_last_page
import time
import re
start_time = time.time()
#import allproducts


conn = sql.connect('shopsales/sales.db')
cur = conn.cursor()

def first_db_innit():
    cur.execute("""CREATE TABLE names(
                product_id INTEGER UNIQUE PRIMARY KEY,
                name TEXT,
                brand TEXT)""")

def db_query(prod_id, name, brand):
    try:
        cur.execute("""INSERT INTO names (product_id, name, brand)
                    VALUES (?,?,?)""", (prod_id, name, brand))
    except sql.IntegrityError: pass    

def main():
    for page in range(0, last_page):
        URL = f"https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455&counter={page}"
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html5lib')
        div = soup.find_all("div", {"class" : re.compile(r"\bproduct col-6 col-sm-4 pt-3 pb-md-3\b")})
        for element in div:
            a = element.find("a", {"class" : "product__icon d-flex justify-content-center align-items-center"})
            href = a['href']
            prod_id = a['data-product-id']
            try:
                name = a['title']
                brand = a['data-brand']
            except:
                name = brand = "missing"            #Products that are unavalible (out of stock) dont have those params

            db_query(prod_id, name, brand)
    
    print("Commiting..")
    conn.commit()
if __name__ == "__main__":
    #first_db_innit()
    last_page = find_last_page()
    main()
    print(f"--- {round(time.time() - start_time, 2)} seconds ---")
