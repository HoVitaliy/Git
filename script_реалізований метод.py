#Припустимо, ми хочемо створити клас "Car" і створити кілька об'єктів цього класу. Також, ми хочемо мати метод "drive", який виводить повідомлення про те, що автомобіль їде.
# Оголошення класу
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.year} {self.make} {self.model} почав рухатися.")

# Створення об'єктів класу Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Виклик методу для кожного об'єкта
car1.drive()
car2.drive()