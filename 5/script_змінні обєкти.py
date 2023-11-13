#Щоб отримати доступ до змінної всередині щойно створеного об’єкта «myobjectx», ви повинні зробити наступне:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.varia


#Так, наприклад, наведене нижче виведе рядок "blah":
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variab)

#Ви можете створити кілька різних об’єктів одного класу (з однаковими змінними та визначеними функціями). Проте кожен об’єкт містить незалежні копії змінних, визначених у класі. Наприклад, якби ми мали визначити інший об’єкт із класом «MyClass», а потім змінити рядок у змінній вище:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)