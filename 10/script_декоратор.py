# Декоратор @property в Python дозволяє створити так звані "read-only" атрибути для класу. Це означає, що ви можете отримувати значення цього атрибуту, але не змінювати його напряму. Вибірковий метод для такого атрибуту можна визначити за допомогою цього декоратора. Ось простий приклад:

class Circle:
    def __init__(self, radius):
        self._radius = radius  # приватне поле

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return 3.14 * self._radius ** 2

# Створюємо об'єкт класу Circle
my_circle = Circle(radius=5)

# Використовуємо @property для отримання значень
print(f"Радіус кола: {my_circle.radius}")
print(f"Площа кола: {my_circle.area}")