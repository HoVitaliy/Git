#Додайте функцію з іменем, list_benefits()яка повертає такий список рядків: «Більш упорядкований код», «Більш читабельний код», «Легше повторне використання коду», «Дозволяти програмістам ділитися та з’єднувати код разом»
#Додайте функцію з іменем build_sentence(info), яка отримує один аргумент, що містить рядок, і повертає речення, що починається з заданого рядка та закінчується рядком "є перевагою функцій!"

# Modify this function to return a list of strings as defined above
def list_benefits():
    return []

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ""

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()