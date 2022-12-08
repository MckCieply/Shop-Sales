#File to temporary show products on sales and last recorded prices w/o sale, to see whether sales are real
import sqlite3 as sql
conn = sql.connect('sales.db')
cur = conn.cursor()

query = cur.execute('SELECT sales.product_id, stock.price as beforeprice, sales.old_price, sales.sale_percent, sales.new_price, sales.link FROM sales, stock WHERE sales.product_id == stock.product_id')
legit = 0
false = 0
for element in query:
    
    product = list(element)
    if product[1] != product[2]:
        print(f"""
    Poprzednia cena: {product[1]}
    Cena skreślona przy promocji: {product[2]}
    Domniemany procent promocji: -{product[3]}%
    Cena po promocji: {product[4]}
    Link: {product[5]}
    """)
        false +=1
    else: legit+=1
print(f"Ilość pseudo promocji: {false}, ilość legit promocji {legit}")