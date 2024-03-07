from collections import Counter, defaultdict
from bisect import bisect_right
import sys

def S(): return sys.stdin.readline().strip()
def I():return(int(S()))
def IL():return(list(map(int,S().split())))
def SL():return(list(S()))
def SIL():return list(map(int, SL()))
def IV():return(map(int,S().split()))
def M(n):return [IL() for _ in range(n)]
def SM(n):return [SIL() for _ in range(n)]

def solve():
    t = I()
    nums = IL()
    nums.sort()
    n = I()
    for _ in range(n):
        coin = I()
        val = bisect_right(nums, coin)
        print(val)
      


solve()