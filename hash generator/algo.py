from random import Random

def hash_generator(string:str, key:str):
    string_ord = [(ord(i)+3) for i in string]
    key_ords = [(ord(i)+3) for i in key]
    hash_string = "" 
    for ordi in string_ord:
        ordi = (ordi+ sum(key_ords))
    
    return Random
    


print(hash_generator("abc", "fhzrui"))