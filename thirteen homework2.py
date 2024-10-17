first_car = {
    'price': 1_263_400,
    'LED_lights_indicators': 'False',
    'Elements_design': [
        'Darkness salon',
        'Combined seat',
        'Leather steering',
        'Comfortable LED lighting(front door)'
    ],
    'Panoramic glass roof': {}
}
Second_car = {
    'price': 1_375_700,
    'LED_lights_indicators': 'True',
    'Elements_design': [
        'Darkness salon',
        'Seat upholstery',
        'NAPPA',
        'Leather steering',
        'Comfortable LED lighting(front door)',
        'Comfortable LED lighting(back door)'
    ],
    'Panoramic glass roof': {
        'price': 29_486
    }
}
price_panoramic_glass_roof = Second_car['Panoramic glass roof']
print(price_panoramic_glass_roof)
Element_design_first_car = first_car['Elements_design']
Element_design_second_car = Second_car['Elements_design']
for Element_design in Element_design_first_car, Element_design_second_car:
    print(Element_design)