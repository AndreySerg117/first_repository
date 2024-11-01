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

url_picture = 'https://cdn.dummyjson.com/products/images/smartphones/Vivo%20V9/1.png'

responce2 = requests.get(url_picture)

with open('phone.png', mode='wb') as file:
    file.write(responce2.content)

for product in products:
    if product.get('brand') == 'TechGear':
        print(product['id'])git