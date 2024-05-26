price = int(input())
N = int(input())
sum = 0
for i in range(N):
    A, B = map(int, input().split())
    sum = sum + (A * B)
if sum == price:
    print("Yes")
else:
    print("No")