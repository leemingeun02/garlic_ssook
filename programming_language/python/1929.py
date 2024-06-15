def max_common(a, b):
    while True:
        if max(a,b) % min(a, b) == 0:
            return min(a, b)
        else: r = max(a,b) % min(a,b)
        if a > b:
            a = r
        else:
            b = r

son1, parent1 = map(int, input().split())
son2, parent2 = map(int, input().split())

B = parent1 * parent2
A = son1 * parent2 + son2 * parent1
maxcom = max_common(A, B)
B = B / maxcom
A = A / maxcom

print(int(A), int(B))