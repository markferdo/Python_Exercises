import random
class Car:
    def __init__(self, reg, max_speed):
        self.registration_number = reg
        self.maximum_speed = max_speed
        self.travel_distance = 0
        self.current_speed = 0
        self.hours = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.current_speed = max(0, self.current_speed + speed_change)
        self.current_speed = min(self.current_speed, self.maximum_speed)

    def drive(self):  # 3
        self.accelerate()
        self.hours += 1
        self.travel_distance += self.current_speed

    def __str__(self):
        return f'Car registration no: {self.registration_number}, Maximum speed: {self.maximum_speed}, Current speed: {self.current_speed}, Travel distance: {self.travel_distance}'


car_list = []
for i in range(10):
    max_speed = random.randint(100,200)
    x = Car(f'ABC-{i+1}', max_speed)
    car_list.append(x)
    x.accelerate()
    x.drive()



race_finished = False
hour = 0
while not race_finished:
    for car in car_list:
        if car.travel_distance >= 10000:
            race_finished = True
            break
        car.drive()
    hour += 1


for i, car in enumerate(car_list):
    print(f'Car {i + 1}: {car}')


print(f'Race finished {hour} hours')

