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

def main(category, last_page):
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
            single_sale(link)

def single_sale(URL):
    request = requests.get(URL)
    soup = BeautifulSoup(request.content, "html5lib")
    span = soup.find('small', {"class" : "h2 d-block text-primary"})
    #strong = small.find_all ('strong')
    print (span)


def menu():
    print("""
    PLEASE CHOOSE YOUR CATEGORY
    
    1. FACE
    2. MAKEUP
    3. HAIR
    4. BODY
    5. PERFUMES
    
    TYPE IN CORESPONDING NUMBER""")
    choice = input(">> ")
    if choice == "1":
        last_page = find_last_page(face)
        main(face, last_page)
    elif choice == "2":
        last_page = find_last_page(makeup)
        main(makeup, last_page)
    elif choice == "3":
        last_page = find_last_page(hair)
        main(hair, last_page)
    elif choice == "4":
        last_page = find_last_page(body)
        main(body, last_page)
    elif choice == "5":
        last_page = find_last_page(perfumes)
        main(perfumes, last_page)
    else:
        print("Thats an error")

menu()