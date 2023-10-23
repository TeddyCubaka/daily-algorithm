import math

def split_integer(number, spliter) :
    ratio = 1
    if spliter > 0 : ratio = number/spliter

    list = [math.floor(ratio*(i/i)) for i in range(1, spliter+1)]

    rest = round((ratio-math.floor(ratio))*spliter)
    if rest > 0 :
        for i in range(1, rest+ 1) :
            list[-i] = list[-i]+1

    return list

print(split_integer(20, 6))

# test = [1, 2,3,4,5]
# print(test[-2])