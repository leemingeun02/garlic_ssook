N = input()
A = []
for i in range(len(N)):
    A.append(int(N[i]))

A.sort(reverse=True)

print(*A, end="",sep="")
