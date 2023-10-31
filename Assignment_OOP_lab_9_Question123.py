import random
class Car:
    def __init__(self, reg, max_speed=142): # 1
        self.registration_number = reg
        self.maximum_speed = max_speed
        self.brake = - 200
        self.travel_distance = 0
        self.current_speed = 0
        self.hours = 0

    def accelerate(self, speed):  # 2
        self.speed = speed
        self.current_speed = self.current_speed + speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours=1):  # 3
        distance = self.speed * hours
        self.travel_distance = distance + self.travel_distance


# Assigning properties
car_1 = Car('ABC-123')
# Assigning change of speed
car_1.accelerate(30)
car_1.accelerate(70)
car_1.accelerate(50)
# Assigning brake property
brake =car_1.brake
# Assigning travel time
car_1.drive()
car_1.drive()
car_1.drive(2)


print('Question 1')
print(f'Car registration no: {car_1.registration_number}')
print(f'maximum speed: {car_1.maximum_speed}')

print('Question 2')
print(f'After 3 change of speed: {car_1.current_speed}')
# after hit brake
after_brake = car_1.current_speed + brake
if after_brake < 0:
    after_brake = 0
print(f'After hit brake: {after_brake}')

print('Question 3')
print(f'Travel distance: {car_1.travel_distance}')

