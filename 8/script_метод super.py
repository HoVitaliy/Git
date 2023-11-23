# Давайте створимо приклад на мові програмування Python з одним батьківським класом і декількома дочірніми класами, які успадковують частину властивостей та функціоналу від батьківського класу. Також ми будемо використовувати метод super() для доступу до методів батьківського класу.

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Дочірній клас Car, який успадковує властивості та методи від батьківського класу Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        # Використовуємо метод super() для отримання результату від батьківського класу
        vehicle_info = super().display_info()
        return f"{vehicle_info}, {self.num_doors} doors"

# Дочірній клас Motorcycle, також успадковує властивості та методи від батьківського класу Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, num_wheels):
        super().__init__(brand, model, year)
        self.num_wheels = num_wheels

    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}, {self.num_wheels} wheels"

# Створюємо об'єкти різних класів
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, 2)

# Викликаємо методи об'єктів
print(car.display_info())  # Виведе "2022 Toyota Camry, 4 doors"
print(motorcycle.display_info())  # Виведе "2022 Harley-Davidson Sportster, 2 wheels"