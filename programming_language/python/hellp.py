T = int(input())

U = list(map(int, input().split()))
for i in U:
    U2 = list()
    for j in range(1, i):
        if (i / j) % 1 == 0:
            U2.append(j)
    if sum(U2) == i:
        print("Perfect")
    elif sum(U2) > i:
        print("Abundant")
    else:
        print("Deficient")