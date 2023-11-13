#Щоб отримати доступ до функції всередині об’єкта, ви використовуєте нотацію, подібну до доступу до змінної:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()