class Car:
    def __init__(self, graduation, fuel: float, producer, mark):
        self.graduation = graduation
        self.producer = producer
        self.mark = mark
        self.run = 0
        self.fuel = fuel

    def drive(self, distance):
        self.run += distance
        text = f'Я авто марки {self.mark}, їду по справам господаря'
        return text

    @property
    def cost_of_service(self):
        costs = self.run * 7.6
        return costs


car1 = Car(graduation='10_09_2020', producer='German', mark='Toyota', fuel=25.5)
car2 = Car(graduation='04_11_2019', producer='Japan', mark='Audi', fuel=30.1)
car3 = Car(graduation='25_08_2022', producer='UK', mark='Porshe', fuel=24.7)
print(car1.drive(10))
print(car1.cost_of_service)
print(car2.drive(20))
print(car2.cost_of_service)
print(car3.drive(30))
print(car3.cost_of_service)
