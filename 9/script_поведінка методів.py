# В Python, перевизначення (або перевантаження) поведінки методів відбувається за допомогою механізму перевизначення методів в дочірньому класі. Ось декілька прикладів:
# Базовий клас

class Animal:
    def make_sound(self):
        return "Some generic sound"

# Клас-спадкоємець
class Dog(Animal):
    # Перевизначення методу make_sound
    def make_sound(self):
        return "Woof!"

# Ще один клас-спадкоємець
class Cat(Animal):
    # Перевизначення методу make_sound
    def make_sound(self):
        return "Meow!"

# Створення об'єктів
generic_animal = Animal()
dog = Dog()
cat = Cat()

# Виклик методів
print(generic_animal.make_sound())  # Some generic sound
print(dog.make_sound())             # Woof!
print(cat.make_sound())             # Meow!