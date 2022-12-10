#File to temporary show products on sales and last recorded prices w/o sale, to see whether sales are real
import sqlite3 as sql
conn = sql.connect('sales.db')
cur = conn.cursor()

query = cur.execute("""SELECT sales.product_id, stock.price as beforeprice, sales.old_price, sales.sale_percent, sales.new_price, sales.link, names.name 
                    FROM sales, stock, names WHERE sales.product_id == stock.product_id AND sales.product_id == names.product_id""")
legit = 0
false = 0
counter = 1
for element in query:
    product = list(element)
    if product[1] != product[2]:
        print(f"""
Sale nr: {counter}
--- SUSPICIOUS SALE ---
Produkt: {product[6]}
Poprzednia cena: {product[1]}
Cena skreślona przy promocji: {product[2]}
Domniemany procent promocji: -{product[3]}%
Cena po promocji: {product[4]}
Link: {product[5]}
""")
        false +=1
    else: 
        print(f"""
--- SALE ---
Sale nr: {counter}
Produkt: {product[6]}
Cena skreślona przy promocji: {product[2]}
Domniemany procent promocji: -{product[3]}%
Cena po promocji: {product[4]}
Link: {product[5]}
""")
        legit+=1
        
    counter +=1
print(f"Ilość pseudo promocji: {false}, ilość legit promocji {legit}")