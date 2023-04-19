def max_sequence(arr):
    seq = []
    if(arr == []) : return 0
    if(max(arr) < 0) : return 0
    for i in range(len(arr)) : [seq.append(arr[i:i + l + 1]) for l in range(len(arr[i:]))]
    return max(sum(count) for count in seq)   

# [-2, 1, -3, 4, -1, 2, 1, -5, 4] must be 6

# warning : this code is not optimal for array size 10000 <= size <= 20000 