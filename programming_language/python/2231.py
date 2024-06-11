N = input()

for i in range(int(N)+1):
    asdf = 0
    i = str(i)
    for j in range(len(str(i))):
        asdf += int(i) + int(i[j])
    if asdf == N:
        print(i)