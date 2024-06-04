import sys
input = sys.stdin.readline().rstrip()


N = input().rstrip()

N = S.replace("pi", "")
N = S.replace("ka", "")
N = S.replace("chu", "")

if not N:
    print("YES")
else:
    print("NO")