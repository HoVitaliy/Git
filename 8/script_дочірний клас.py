# Давайте внесемо зміни в наш попередній приклад, щоб продемонструвати використання методів об'єктів-представників іншого дочірнього класу. Введемо новий клас Garage, який буде містити об'єкти інших класів.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, {self.num_doors} doors"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, num_wheels):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, {self.num_wheels} wheels"


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all_vehicles_info(self):
        for vehicle in self.vehicles:
            print(vehicle.display_info())


# Створюємо об'єкти різних класів
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, 2)

# Створюємо гараж і додаємо туди об'єкти
garage = Garage()
garage.add_vehicle(car)
garage.add_vehicle(motorcycle)

# Виводимо інформацію про всі об'єкти в гаражі
garage.display_all_vehicles_info()