class Solution:
    def helper(self, x, y, mod):   
        if y==1:
            return x
        if y < 1:
            return 1
        val = self.helper(x,y//2,mod)
        if y%2==0:
            return (val*val)%mod
        return (val*val*x)%mod

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        temp = self.helper(5, n//2, mod) * self.helper(4, n//2, mod)
        temp = temp * 5 if n % 2 else temp
        return temp % mod
