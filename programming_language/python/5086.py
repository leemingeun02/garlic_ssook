N, M = map(int,input().split(" "))

while N != 0 and M != 0:
    if N % M == 0:
        print("multiple")
    elif M % N == 0:
        print("factor")
    else:
        print("neither")
    N, M = map(int,input().split(" "))

