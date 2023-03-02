def nb_dig(n, d):
    x = []
    count = 0
    for i in range(n+1): 
        x.append(i**2)
    for digit in x :
        count = count + str(digit).count(str(d))
    return count

print(nb_dig(25, 1))
