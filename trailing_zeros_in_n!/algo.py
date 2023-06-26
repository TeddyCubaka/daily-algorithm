def fact(n) :
    return 1 if n == (0 or 1) else n * fact(n-1)
print(fact(6))

def zeros (n):
    c = 0;
    for i in str(fact(n))[::-1] :
        if i != "0" : break
        else : c += 1
    return c

print(zeros(1000))