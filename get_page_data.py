import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
def get_page_data(page_count):
    response = requests.get(url+f"/catalogue/page-{page_count}.html")
    if response.status_code != 200 :
        return False
    soup = BeautifulSoup(response.text, "html.parser")
    return [product for product in soup.select("li.col-xs-6.col-sm-4.col-md-3.col-lg-3")]