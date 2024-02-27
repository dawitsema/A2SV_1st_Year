from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input()))
    
    dictionary = defaultdict(int)
    dictionary[0] = 1
    
    run_sum = 0
    count = 0
    for i in range(len(nums)):
        run_sum += nums[i]
        temp = run_sum - i - 1
        count += dictionary[temp] 
        dictionary[temp] += 1
    
    print(count)