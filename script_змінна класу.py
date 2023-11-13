#Змінна класу є змінною, яка зберігається на рівні класу, а не на рівні екземплярів класу. Це означає, що всі екземпляри класу можуть спільно використовувати цю змінну. Давайте реалізуємо змінну класу та метод, що її використовує, на прикладі класу "Car":
class Car:
    # Змінна класу
    total_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Збільшення змінної класу при створенні нового об'єкта
        Car.total_cars += 1

    def drive(self):
        print(f"{self.year} {self.make} {self.model} почав рухатися.")

    def generate_description(self):
        return f"Автомобіль {self.year} року, виробництва {self.make}, модель {self.model}."

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

# Створення об'єктів класу Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Виклик методу для кожного об'єкта
car1.drive()
car2.drive()

# Виклик нового методу generate_description
print(car1.generate_description())
print(car2.generate_description())

# Виведення змінної класу
print(f"Кількість створених автомобілів: {Car.get_total_cars()}")
