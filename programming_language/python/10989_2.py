import sys
input = sys.stdin.readline


N = int(input())

counting_sort = [0] * 10001
for _ in range(N):
    asdf = int(input())
    counting_sort[asdf] += 1







for i in range(1, 10001):
    for j in range(counting_sort[i]):
        print(i)