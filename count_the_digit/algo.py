def nb_dig(n, d):
    count = 0
    x = [str(i**2) for i in range(n+1)]
    for digit in x :
        count = count + digit.count(str(d))
    return count

print(nb_dig(11, 1))
