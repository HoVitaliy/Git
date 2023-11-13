#Щоб реалізувати альтернативний конструктор за допомогою методу класу, можна використовувати декоратор @classmethod та створити новий метод, який повертатиме новий об'єкт класу. Давайте змінимо клас "Car" так, щоб ми могли створювати автомобілі за допомогою іншого набору параметрів за допомогою методу класу:
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
    def from_string(cls, car_string):
        make, model, year = car_string.split(',')
        return cls(make, model, int(year))

# Створення екземплярів класу Car
car1 = Car("Toyota", "Camry", 2022)
car2 = Car.from_string("Honda,Accord,2023")

# Виклик методу для кожного об'єкта
car1.drive()
car2.drive()

# Виведення лічильника створених автомобілів
print(f"Кількість створених автомобілів: {Car.total_cars}")