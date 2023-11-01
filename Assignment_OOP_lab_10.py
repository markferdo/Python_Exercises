class Elevator:  # 1
    def __init__(self, top, bottom=1):
        self.bottom = bottom
        self.top = top
        self.current_floors = bottom

    def go_to_floor(self, target_floor):
        self.target_floor = target_floor
        if self.current_floors < self.target_floor:
            while self.target_floor > self.current_floors:
                self.floor_up()
        elif self.target_floor < self.current_floors:
            while self.target_floor < self.current_floors:
                self.floor_down()
    def floor_up(self):
        self.current_floors += 1
        print(f'Elevator is on {self.current_floors} floor')
    def floor_down(self):
        self.current_floors -= 1
        print(f'Elevator is on {self.current_floors} floor')


print('Question 1')
h = Elevator(7)
h.go_to_floor(5)
h.go_to_floor(1)

print('Question 2')

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for _ in range(num_elevators):
            elevator = Elevator(top_floor, bottom_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(destination_floor)
        else:
            print("Invalid elevator number. Please choose a valid elevator.")

    def fire_alarm(self):
        print("Fire alarm activated. All elevators are moving to the bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)

my_building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

# Run elevator 0 to the 5th floor
my_building.run_elevator(0, 5)

# Run elevator 1 to the 7th floor
my_building.run_elevator(1, 7)

# Run elevator 2 to the 3rd floor
my_building.run_elevator(2, 3)

print('Question 3')

my_building.fire_alarm()

print('Question 4')

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


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_passes(self):
        for car in self.car_list:
            car.drive()

print(f'Race finished {hour} hours')





