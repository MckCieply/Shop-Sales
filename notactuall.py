#program to check whether its old sale and whether it has to be removed
import sqlite3 as sql
conn = sql.connect('shopsales/sales.db')
cur = conn.cursor()
def db_select():
    #query for all present sales, to be able to compare it with current sales, and be able to remove old ones from db
    old_sales = []
    query = cur.execute("""SELECT product_id from sales""")
    for element in query:
        old_sales.append(element[0])
    return old_sales

def checkOnSale(old_sales, new_sales):
    #check whether is there any not actuall sales, out of stock or ended
    results = list(set(old_sales) - set(new_sales))
    return results

def db_delete(results):
    #removing sales based on prievous results
    if not results:
        print("There is nothing to remove.")
    else:
        print(f"Removing products from sales...")
        for element in results:
            print(f"{element}...", end=" ")
            cur.execute('DELETE FROM sales WHERE product_id = ?', (element,))
            print("Done")
        conn.commit()
    