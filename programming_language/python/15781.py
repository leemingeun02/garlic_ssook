N, M = map(int, input().split())

helmet = list(map(int, input().split()))
vest = list(map(int, input().split()))

a = max(helmet)
b = max(vest)

print(a+b)
