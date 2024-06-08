N = int(input())
while N != -1:
    array = []

    # 약수들 찾기
    for i in range(2, N):
        if N % i == 0:
            array.append(i)

    if N == sum(array) + 1:
        print(f"{N} = 1 + ", end="")
        for i in range(len(array)):
            if i + 1 == len(array):
                print(f"{array[i]}")
            else:
                print(f"{array[i]} + ", end="")
    else:
        print(f"{N} is NOT perfect.")

    N = int(input())