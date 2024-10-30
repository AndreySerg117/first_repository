import requests

url = 'https://dummyjson.com/products?limit=200'

responce = requests.get(url)

responce_json = responce.json()

products = responce_json['products']
for product in products:
    print(product)

total_price = 0
for product in products:
    if product['price'] >= 800:
        total_price += product['price']
print(total_price)
