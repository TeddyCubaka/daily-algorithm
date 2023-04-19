def solution(s):
    return [(s+"_")[i:i+2] for i in range(len(s)) if i%2 == 0]

print(ord("a"))
