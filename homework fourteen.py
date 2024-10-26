students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

eighteen_student3 = students['Маша Кера']['Вік']
if 40 >= eighteen_student3 >= 18:
    print(students['Маша Кера'])

if students['Іван Петров']['Середній бал'] > 90:
    print(f'Іван Петров {students['Іван Петров']['Середній бал']}')

average_score = students['Іван Петров']['Середній бал']
average_score2 = students['Женя Курич']['Середній бал']
average_score3 = students['Маша Кера']['Середній бал']
sum_score = (average_score + average_score2 + average_score3)
average_sum = (sum_score // 3)
print(average_sum)

if students['Женя Курич']['Номер телефону'] == None:
    print(f'+1234567890')