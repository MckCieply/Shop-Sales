from bs4 import BeautifulSoup
import sqlite3 as sql
import requests
#Rossman categories 
face = "8686"
makeup = "8528"
hair = "8655"
body = "8625"
perfumes = "8512"

def find_last_page(category):
    URL = f"https://www.rossmann.pl/promocje?CategoryId={category}&Page=1&PageSize=96"
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, 'html5lib')
    a = soup.find('a', {'class':'pages__last'})
    last_page = int(a.text)
    return last_page

def main(category):
    counter = 0
    for page in range(last_page):
        URL = f"https://www.rossmann.pl/promocje?CategoryId={category}&Page={page}&PageSize=96"
        request = requests.get(URL)
        soup = BeautifulSoup(request.content, 'html5lib')
        a = soup.find_all('a', {'class': "tile-product__name"})
        for element in a:
            link = "https://rossmann.pl" + element['href']
            print(f"{counter}. {link}")
            counter += 1
last_page = find_last_page(perfumes)
main(perfumes)
