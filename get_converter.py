from time import sleep
def get_convertor(conversions):
    print("What would you like to convert the prices to?")
    sleep(1)
    print("From GBP ~ ")
    print(*conversions)
    conversion = input().upper()
    if conversion not in conversions:
        print("Please input a valid currency")
        sleep(1)
        return get_convertor(conversions)
    return conversion

def convert_product_price(original_price,converter):
    return str(round(original_price*converter,2))