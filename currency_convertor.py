import requests 
import re
from get_conversions import get_conversions, calc_conversions
from get_page_data import get_page_data
from get_converter import get_convertor,convert_product_price
from time import sleep



conversion_data = get_conversions()
conversions = [conversion for conversion in conversion_data]
convertor = get_convertor(conversions)
    

with open("original_currency.csv","w") as file:
    file.write(f"Title, 'Original currency ~ GBP', 'Converted currency ~ {convertor}'\n")
page_count = 1
while page_count:
    products = get_page_data(page_count)
    if not products:
        if page_count == 1:
            print("api call failed")
        else:
            print("could not find that page, must be finished")
        break
    
    with open("original_currency.csv","a",encoding="utf-8") as file:
        for product in products:
            product_title = product.select_one("h3>a")["title"]
            product_price = product.select_one("p.price_color").string

            match = re.search(r"[^\d]*([0-9\.]*)[^\d]*",product_price)
            product_price_float_str = match.group(1)
            product_price_float = float(product_price_float_str)
            
            converted_product_price = convert_product_price(product_price_float,conversion_data[convertor]['value'],)

            file.write(f'"{product_title}", {product_price_float_str} GBP, {converted_product_price} {convertor}\n\n')
    page_count+=1