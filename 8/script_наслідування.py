# Наслідування (inheritance) - це одна з основних концепцій об'єктно-орієнтованого програмування (ООП). Вона дозволяє створювати новий клас на основі вже існуючого, використовуючи його властивості та методи. Це робить код більш модульним, зменшує дублювання коду і полегшує його обслуговування.
# Батьківський клас (клас, який буде успадкований)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


# Підклас (клас, який успадковує властивості та методи батьківського класу)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Створення об'єктів
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Виклик методів, успадкованих від батьківського класу
print(dog.speak())  # Виведе "Buddy says Woof!"
print(cat.speak())  # Виведе "Whiskers says Meow!"