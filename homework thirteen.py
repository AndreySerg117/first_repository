characteristic = {
 'first_dict': {
     'Petrol': '2,5 (171 к.с.) 4х2 АКП (CVT)',
     'Petrol2': '2,5 (171 к.с.) 4х4 АКП (CVT) (INTENSE)',
     'price': 18_512,
     'Has_LED_rear_lights_with_dynamic_turn_indicators?': 'ZEN - false' 'INTENSE - true',
     'Elements_of_exterior_design': [
        'Layers on the roof',
        'Protective cover on the bumper',
        'Additional tinting of rear windows',
        'Alloy wheels 2-color 18'' new design with diamond grinding',
        'Metallic paint',
        'Special paint "black amethyst"'
     ]
 },
 'description of the panoramic glass roof': {
     'Aesthetics':
     'The roof creates a modern and stylish look, adding to the elegance of the building',
     'Natural lighting':
     'Provides optimal lighting in the premises, reducing the need for artificial lighting',
     'View of nature':
     'Creates a feeling of space and connection with nature,'
     'thanks to the opportunity to enjoy the scenery',
     'price_glass_roof': 1_400
 }
}

price_glass_roof = characteristic['description of the panoramic glass roof']['price_glass_roof']
petrol = characteristic['first_dict']['Petrol2']
exterior_design_elements = characteristic['first_dict']['Elements_of_exterior_design']
print(f'{price_glass_roof} для {petrol}')
for exterior_design_element in exterior_design_elements:
    print(exterior_design_element)