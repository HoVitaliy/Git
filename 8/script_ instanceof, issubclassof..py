# isinstance(): Ця функція використовується для перевірки того, чи є об'єкт екземпляром певного класу або чи є екземпляром будь-якого класу з перелік

class Vehicle:
    pass

class Car(Vehicle):
    pass

car = Car()

# Перевірка, чи є car екземпляром класу Car
print(isinstance(car, Car))  # True

# Перевірка, чи є car екземпляром класу Vehicle
print(isinstance(car, Vehicle))  # True

# Перевірка, чи є car екземпляром будь-якого класу з переліку
print(isinstance(car, (int, str, Car)))  # True



# issubclass(): Цей метод використовується для перевірки того, чи є один клас підкласом іншого.

class Vehicle:
    pass

class Car(Vehicle):
    pass

# Перевірка, чи є клас Car підкласом класу Vehicle
print(issubclass(Car, Vehicle))  # True

# Перевірка, чи є клас Vehicle підкласом класу object (всі класи є підкласами object)
print(issubclass(Vehicle, object))  # True