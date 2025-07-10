from bs4 import BeautifulSoup
import requests 
import re

with open("original_currency.csv","w") as file:
    file.write("Title,'Original currency','Converted currency'\n")

url = "https://books.toscrape.com/"
page_count = 1
while True:
    response = requests.get(url+f"/catalogue/page-{page_count}.html")
    if response.status_code != 200 :
        break
    soup = BeautifulSoup(response.text, "html.parser")
    products = [product for product in soup.select("li.col-xs-6.col-sm-4.col-md-3.col-lg-3")]
    with open("original_currency.csv","a") as file:
        for product in products:
            product_title = product.select_one("h3>a")["title"]
            product_price = product.select_one("p.price_color").string
            product_price_int = re.match(r".*\d*\.\d\d",product_price)

            file.write(f"'{product_title}', {product_price} \n")
    page_count+=1