# Додайте «Джейк» до телефонної книги з номером телефону 938273443 і видаліть Джил з телефонної книги.

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

phonebook["Jake"] = 938273443  
del phonebook["Jill"]  

if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  