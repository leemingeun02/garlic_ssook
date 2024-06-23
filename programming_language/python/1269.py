N, M = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

answer = A^B

print(len(answer))