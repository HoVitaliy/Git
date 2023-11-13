#Для попереднього прикладу з класом "Car" ми вже використовували змінну класу total_cars. Тепер додамо метод класу, який буде працювати з цією змінною класу. Давайте, наприклад, створимо метод класу, який дозволить збільшувати загальну кількість автомобілів на певну величину:
class Car:
    total_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1

    def drive(self):
        print(f"{self.year} {self.make} {self.model} почав рухатися.")

    def generate_description(self):
        return f"Автомобіль {self.year} року, виробництва {self.make}, модель {self.model}."

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

    @classmethod
    def increase_total_cars(cls, amount):
        cls.total_cars += amount

# Створення екземплярів класу Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Виклик методу класу для збільшення кількості автомобілів
Car.increase_total_cars(3)

# Виведення лічильника створених автомобілів
print(f"Кількість створених автомобілів: {Car.get_total_cars()}")