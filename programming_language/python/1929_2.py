import math
import sys
input = sys.stdin.readline().rstrip

M, N = map(int, input().split())

def sosu(a):
    if a == 1:
        return False
    asdf = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            asdf = False
    return asdf
            
    
for i in range(M, N+1):
    if sosu(i) == True:
        print(i)