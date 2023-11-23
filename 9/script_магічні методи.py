# "Магічні методи" в Python відомі також як "спеціальні методи" або "dunder-методи" (double underscore methods). Це методи, які мають подвійні підкреслення на початку та кінці свого імені. Ці методи викликаються автоматично при використанні спеціальних мовних конструкцій, таких як оператори, або при виклику вбудованих функцій. Давайте реалізуємо кілька "магічних методів" для класу Person:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        return hash((self.name, self.age))

# Створення об'єктів класу
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
person3 = Person("Alice", 25)

# Використання магічного методу __str__
print(person1)  # Виведе: Person(name=Alice, age=25)

# Використання магічного методу __eq__
print(person1 == person2)  # Виведе: False
print(person1 == person3)  # Виведе: True

# Використання магічного методу __hash__
print(hash(person1))  # Виведе: виведе хеш-код для об'єкта

