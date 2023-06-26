def create_two_sets_of_equal_sum(n:int): 
    arr = [*range(1, n)]
    list = []
    for i in range(n-1): 
        list.append([arr[i]])
        list.append(arr[:i])
        list.append([*arr[:i], *arr[i+1:]])
        list.append([*arr[:i+1], *arr[i-1:]])
        list.append([i for i in [*arr[:i], *arr[i+1:]] if i%2==0])
        list.append([i for i in [*arr[:i], *arr[i+1:]] if i%2==1])
    sums = [sum(i) for i in list]
    print(list)
    return sums

print(create_two_sets_of_equal_sum(8))
