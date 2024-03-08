from collections import Counter, defaultdict
from math import ceil
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
    position = IL()
    speed = IL()
    con = 1/10000000
    
    left, right = 0, ceil((max(position) - min(position))/2)
    time = right
    
    while left + con < right:
        midd = (left + right)/2
        
        maxx = float("-inf")
        minn = float("inf")
        
        for i in range(len(position)):
            maxx = max(maxx, position[i] - speed[i]*midd)
            minn = min(minn, position[i] + speed[i]*midd)
        if minn >= maxx:
            time = midd
            right = midd - con
        else:
            left = midd + con
    
    print(time)
            
   
      


solve()