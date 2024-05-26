N = int(input())
numbers = list(input())
for i in range(N):
    numbers[i] = int(numbers[i])
sum = 0
for i in range(N):
    sum = sum + numbers[i]
print(sum)