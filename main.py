import requests
import util_email

url = 'https://script.google.com/macros/s/AKfycbxYigkBEdXIUkabwOiUo8xRLKYcYE2VjiQ8m7enou9i4MnDDznH0HJq3slZodFmrif9gA/exec'

response = requests.get(url)
response_json = response.json()
data = response_json['data']

total_poisonous = 0
for animal_info in data:
    if animal_info['poisonous'] == True:
        total_poisonous += animal_info['cost_of_care']
print(f'вартість догляду за отруйними тваринами: {total_poisonous}')

total_african = 0
for animal_info in data:
    if animal_info['continent'] == 'Африка':
        total_african += 1
print(f'скільки африканських тварин наразі в зоопарку: {total_african}')

most_expensive_animal = {}
most_expensive_service_cost_per_animal = 0

for animal_info in data:
    cost_of_care_animal = animal_info['cost_of_care']
    if cost_of_care_animal > most_expensive_service_cost_per_animal:
        most_expensive_service_cost_per_animal = cost_of_care_animal
        most_expensive_animal = animal_info
print(f'найбільш дорогу в обслуговуванні тварину {most_expensive_animal}')

if most_expensive_animal:
    from util_email import send_email, render_html

    result = render_html('Templates/tem.html', most_expensive_animal)

    send_email(
        ['test_hillel_api_mailing@ukr.net'],
        result,
        'mail subject',
        # 'README.md',
    )




