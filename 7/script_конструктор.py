#У багатьох об'єктно-орієнтованих мовах програмування, таких як Python, можна використовувати альтернативні конструктори для створення об'єктів класу з допомогою спеціальних методів. В Python такий метод зазвичай називається classmethod. Альтернативний конструктор дозволяє іншим способом створювати об'єкти класу, не використовуючи стандартний конструктор __init__. Давайте розглянемо приклад:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = cls.calculate_age(birth_year)
        return cls(name, age)

    @staticmethod
    def calculate_age(birth_year):
        current_year = 2023  # Припустимо, що поточний рік - 2023
        return current_year - birth_year

# Використання стандартного конструктору
person1 = Person("John", 25)

# Використання альтернативного конструктору
person2 = Person.from_birth_year("Alice", 1990)

# Виведення інформації про об'єкти
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")