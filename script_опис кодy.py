#Щоб реалізувати метод, який генерує опис об'єкта на основі його властивостей, можна додати новий метод до класу. Використаємо попередній приклад з класом "Car" та додамо метод "generate_description":
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.year} {self.make} {self.model} почав рухатися.")

    def generate_description(self):
        return f"Автомобіль {self.year} року, виробництва {self.make}, модель {self.model}."

# Створення об'єктів класу Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Виклик методу для кожного об'єкта
car1.drive()
car2.drive()

# Виклик нового методу generate_description
print(car1.generate_description())
print(car2.generate_description())
