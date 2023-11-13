#Функції в Python визначаються за допомогою ключового слова блоку «def», після якого вказується ім’я функції як ім’я блоку. Наприклад:
def my_function():
    print("Hello From My Function!")



#Функції також можуть отримувати аргументи (змінні, що передаються від викликаючого до функції). Наприклад:
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


#Функції можуть повертати значення викликаючому за допомогою ключового слова 'return'. Наприклад:
def sum_two_numbers(a, b):
    return a + b