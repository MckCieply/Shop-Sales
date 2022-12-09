#Scrpit scrapping all product names and create table to stick 'em to prod IDs
##https://www.ezebra.pl/pl/menu/makijaz-100.html?filter_producer=&search=&filter_node%5B1%5D=&filter_price=0-30&filter_traits%5B25445%5D=25451%2C25464%2C25461%2C25450%2C25455
from bs4 import BeautifulSoup
import requests
import sqlite3 as sql


conn = sql.connect('sales.db')
cur = conn.cursor()

def first_db_innit():
    cur.execute("""CREATE TABLE names(
                product_id INTEGER UNIQUE PRIMARY KEY,
                name TEXT,
                category TEXT,
                brand TEXT)""")

def db_query(prod_id, name, category, brand):
    cur.execute("""INSERT INTO names (product_id, name, category, brand)
                VALUES (?,?,?,?)""", (prod_id, name, category, brand))    
    
