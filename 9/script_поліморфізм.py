# Перевизначення методів в Python схоже на те, як це відбувається в інших об'єктно-орієнтованих мовах. Ви можете визначити метод з тією ж назвою в дочірньому класі, що і в базовому класі, і цей метод буде викликано при використанні об'єкта дочірнього класу.

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

def animal_sounds(animal):
    animal.make_sound()

# Поліморфізм: виклик методу make_sound може мати різні реалізації
dog = Dog()
cat = Cat()

animal_sounds(dog)  # Woof!
animal_sounds(cat)  # Meow!

# Python не використовує строго типізовані інтерфейси, але ви можете створювати класи, які мають однакові методи. Це дозволяє вам використовувати об'єкти різних класів з однаковим інтерфейсом у спільних сценаріях.

class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

def draw_shape(shape):
    shape.draw()

# Поліморфізм: об'єкти різних класів використовуються зі спільним інтерфейсом
circle = Circle()
rectangle = Rectangle()

draw_shape(circle)     # Drawing a circle
draw_shape(rectangle)  # Drawing a rectangle





