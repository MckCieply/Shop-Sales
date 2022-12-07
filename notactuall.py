#program to check whether its old sale and whether it has to be removed
import sqlite3 as sql
conn = sql.connect('sales.db')
cur = conn.cursor()
def db_select():
    #query for all present sales, to be able to compare it with current sales, and be able to remove old ones from db
    old_sales = []
    query = cur.execute("""SELECT product_id from sales""")
    for element in query:
        old_sales.append(element[0])
    return old_sales

def checkOnSale(old_sales, new_sales):
    result = list(set(old_sales) - set(new_sales))
    return result
