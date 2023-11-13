#Звичайні методи (Instance Methods):
class MyClass:
    def instance_method(self):
        print("Це звичайний метод")

# Створення екземпляра класу
obj = MyClass()

# Виклик звичайного методу
obj.instance_method()


#Методи класу (Class Methods):
class MyClass:
    class_variable = 0

    def __init__(self):
        MyClass.class_variable += 1

    @classmethod
    def class_method(cls):
        print(f"Кількість екземплярів класу: {cls.class_variable}")

# Створення екземплярів класу
obj1 = MyClass()
obj2 = MyClass()

# Виклик методу класу
MyClass.class_method()
