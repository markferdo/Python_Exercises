# Question1
class Publication:
    def __init__(self, name):
        self.publication_name = name

class Books(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def book_details(self):
        print(f'Book name: {self.publication_name} Author: {self.author} Page count: {self.page_count}')

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    def magazine_details(self):
        print(f'Magazine name: {self.publication_name} Chief editor: {self.editor}')

publication1 = Books(' Compartment No. 6', 'Rosa Liksom', 192 )
publication2 = Magazine('Donald Duck','Mark')

publication1.book_details()
publication2.magazine_details()


# Question2
class Car:
    def _init_(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        if change >= 0:
            self.current_speed = min(self.current_speed + change, self.max_speed)
        else:
            self.current_speed = max(self.current_speed + change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def _init_(self, registration_number, max_speed, battery_capacity):
        super()._init_(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def _init_(self, registration_number, max_speed, tank_volume):
        super()._init_(registration_number, max_speed)
        self.tank_volume = tank_volume



electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(40)
gasoline_car.accelerate(30)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric Car - Kilometers driven: {electric_car.travelled_distance} km")
print(f"Gasoline Car - Kilometers driven: {gasoline_car.travelled_distance} km")

