def nb_dig(n, d):
    x = []
    count = 0
    for i in range(n+1): 
        x.append(i**2)
    for digit in x :
        count = count + str(digit).count(str(d))
    return count

print(nb_dig(25, 1))


def inputer():
    var = input("entrer un nombre : ")
    if(var is int) : print('la valeur entré est : ', var)
    if(var is not int) : 
        print('la valeur entré n\'est pas un nombre. ')
        input('saisissez plutôt un nombre : ')
    return var
print(inputer())