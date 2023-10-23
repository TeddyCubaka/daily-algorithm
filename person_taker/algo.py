def person_taker():
    print("Hi and welcome.")
    print("Note that we don't save your informations. You can't lie. It's just a fun.")
    print("____________________________________________________")
    print(" ")
    name = input("What's your name ? : ")
    age:int = input("What's your age.(insert a number please.) ? : ")
    print(f'your are {name}, you are {age} old.')
    return {
        'age' : age, 
        'name' : name, 
    }

def age_calculus():
    person = person_taker()
    auth = input('we must have your authorization to continue. Reply by Y/n : ')
    if(auth == "n" or auth == 'N') : return 'Thanks you ! This is the end.'
    else :
        age:int = person['age']
        age_confirm:int = input(f'Your current age is {age}. Want you to continue ?. (Y/n)')
        if(age_confirm == 'n' or age_confirm == 'N') : age:int = input('Insert your new age : ')
        number:int = input("with what number do you want multiply your age ? ")
        return int(age) * int(number)

print(age_calculus())

