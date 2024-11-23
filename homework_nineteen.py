class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        text = f'{self.brand} {self.model}'
        return text


vehicle1 = Vehicle(brand='BMW', model='M5')
print(vehicle1.info())

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        text = f'{self.brand} {self.model} {self.num_doors}'
        return text


car1 = Car(brand='Tesla', model='model X', num_doors=4)
print(car1.info())


class Bike(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def info(self):
        text = f'{self.brand} {self.model} {self.type}'
        return text


bike1 = Bike(brand='Motorsport', model='UTEW 50', type='гірський')
print(bike1.info())


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        text = f'{self.brand} {self.model} {self.capacity}'
        return text


truck1 = Truck(brand='Man', model='GT 8', capacity=500)
print(truck1.info())
