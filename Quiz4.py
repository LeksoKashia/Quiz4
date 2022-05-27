import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randrange

file = open('book.csv', 'w', newline='\n', encoding='utf-8_sig')
file_object = csv.writer(file)
file_object.writerow(['Book', 'Price', 'IMG_URL'])

page = 1
while page < 6:

    url = 'https://biblusi.ge/products?category=291&page=' + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sub_soup = soup.find('div', class_="row")
    books = sub_soup.find_all('div', class_="mb-1_875rem col-sm-4 col-md-3 col-xl-2 col-6")

    for each in books:
        img_url = each.a.div.attrs.get('style')
        book = each.div.div.acronym.text
        price = each.find('div', class_='text-primary font-weight-700').text
        price = price.replace(' ', '').replace('\n', '')
        file_object.writerow([book, price, img_url])
        print(img_url)
        print(book)
        print(price)

    page += 1
    sleep(randrange(15, 20, 1))
