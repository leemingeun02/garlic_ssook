H, M = map(int, input().split())

if (H == 0) and (M < 45):
    H = 23
    M = M + 15
else:
    if M < 45:
        H = H-1
        M = M + 15
    else:
        H = H
        M = M - 45
print(H,M)