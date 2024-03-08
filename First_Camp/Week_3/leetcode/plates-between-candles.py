class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        nums = [1 if x == "*" else 0 for x in s]
        prefix_sum = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            prefix_sum.append(temp)
        
        candle = []
        for i in range(len(s)):
            if s[i] == "|":
                candle.append(i)
        # print(candle)
        # print(prefix_sum)
        
        ans = [0]*len(queries)
        if candle:
            for i in range(len(queries)):
                pt1 = queries[i][0]
                pt2 = queries[i][1]
                
                m = bisect_left(candle, pt1)
                n = bisect_left(candle, pt2)

                
                # print(m, n)
                if n == len(candle):
                    n -= 1
                if m == len(candle):
                    m -= 1
                if candle[n] > pt2:
                    n -= 1
                ind1 = candle[m]
                ind2 = candle[n]
                # print(ind1, ind2)
                if n >= m:
                    ans[i] = prefix_sum[ind2] - prefix_sum[ind1]
                    
        # print(ans)
        return ans