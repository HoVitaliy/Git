#Щоб реалізувати лічильник створених об'єктів за допомогою класу, можна використовувати змінну класу, яка буде зберігати кількість створених екземплярів класу. Давайте використаємо клас "Car" як приклад
class Car:
    # Змінна класу для лічильника
    count = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # Збільшення лічильника при створенні нового об'єкта
        Car.count += 1

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

# Виведення лічильника створених об'єктів
print(f"Кількість створених автомобілів: {Car.count}")