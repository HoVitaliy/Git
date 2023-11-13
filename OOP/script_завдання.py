#У нас є клас, визначений для транспортних засобів. Створіть два нових транспортних засобу під назвою car1 і car2. Встановіть, що car1 буде червоним кабріолетом вартістю $60 000,00 на ім’я Fer, а car2 — синім фургоном під назвою Jump вартістю $10 000,00.
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

# test code
print(car1.description())
print(car2.description())