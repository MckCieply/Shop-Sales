#Program to temporary fix issues with products being on sale BUT NOT BEING IN SHOP STOCK?

import sqlite3 as sql

conn = sql.connect("shopsales/sales.db")
cur = conn.cursor()

query = cur.execute("SELECT product_id, link from sales WHERE product_id NOT IN (SELECT product_id FROM stock)")

for element in query:
    print(element[1])