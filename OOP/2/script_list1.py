#Метою цієї вправи є створення рядка, цілого числа та числа з плаваючою комою. 
# Рядок повинен мати назву mystringта містити слово «привіт». Число з плаваючою комою має бути названо myfloatта повинно містити число 10,0, а ціле число має бути названо myintта повинно містити число 20.


# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)