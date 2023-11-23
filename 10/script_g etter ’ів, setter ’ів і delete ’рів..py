# Концепція геттерів, сеттерів і дилетерів пов'язана з ідеєю контролю за доступом до атрибутів класу. Геттери використовуються для отримання значення атрибуту, сеттери для зміни його значення, а дилетери для видалення атрибуту. Ці методи можуть бути використані для встановлення додаткових логік або обмежень при роботі з атрибутами класу.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        # Геттер для отримання значення атрибуту
        print("Виклик геттера")
        return self._name

    @name.setter
    def name(self, value):
        # Сеттер для встановлення значення атрибуту
        print("Виклик сеттера")
        if not isinstance(value, str):
            raise ValueError("Ім'я повинно бути рядком")
        self._name = value

    @name.deleter
    def name(self):
        # Дилетер для видалення атрибуту
        print("Виклик дилетера")
        del self._name

# Створюємо об'єкт класу Person
person = Person("John")

# Викликаємо геттер
print(person.name)

# Викликаємо сеттер
person.name = "Alice"

# Викликаємо геттер знову
print(person.name)

# Викликаємо дилетер
del person.name