#Статичний метод використовується, коли функціональність не залежить від конкретного екземпляру класу або його атрибутів. Давайте додамо статичний метод до класу "Car" і перевіримо його роботу. Наприклад, ми можемо створити статичний метод, який порівнює дві машини за роком випуску та виводить результат:
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

    @staticmethod
    def compare_cars(car1, car2):
        if car1.year < car2.year:
            print(f"{car1.make} {car1.model} старший за {car2.make} {car2.model}.")
        elif car1.year > car2.year:
            print(f"{car1.make} {car1.model} молодший за {car2.make} {car2.model}.")
        else:
            print(f"{car1.make} {car1.model} і {car2.make} {car2.model} випущені в однаковому році.")

# Створення екземплярів класу Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Виклик статичного методу для порівняння двох автомобілів
Car.compare_cars(car1, car2)