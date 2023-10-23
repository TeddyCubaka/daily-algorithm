value = {
    'I':1,
'V':5,
'X':10,
'L':50,
'C':100,
'D':500,
'M':1000
}

def solution(roman : str) -> int:
    nums = []
    for i, letter in enumerate(roman): 
        if i == len(roman)-1 : nums.append(value[letter])
        elif value[letter] >= value[roman[i+1]] : nums.append(value[letter])
        elif value[letter] < value[roman[i+1]] : nums.append(value[letter]*(-1))
    return sum(nums)

print(solution('CD'))