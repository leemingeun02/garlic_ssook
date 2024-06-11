N = input()

for i in range(int(N)):
    i = str(i)
    make_sum = int(i)
    for j in range(len(i)):
        make_sum += int(i[j])
    if make_sum == int(N):
        print(i)
        break
    if int(i) == int(N) -1:
        print(0)