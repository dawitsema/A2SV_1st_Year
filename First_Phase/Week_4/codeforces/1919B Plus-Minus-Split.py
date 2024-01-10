t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    minus = 0
    plus = 0
    for i in range(n):
        if s[i] == "+":
            plus += 1
        else:
            minus += 1
    
    result = abs(plus - minus)
    print(result)