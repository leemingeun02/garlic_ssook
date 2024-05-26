A, B, C = map(int, input().split())


same = 0
if A == B:
    same = A
if A == C:
    same = A
if B == C:
    same = B


if (A != B) and (B != C) and (C != A):
    max = 0
    if A > max:
        max = A
    if B > max:
        max = B
    if C > max:
        max = C
    print(max * 100)
elif (A == B == C):
    print(same * 1000 + 10000)
else:
    print(same * 100 + 1000)