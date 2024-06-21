N, K = map(int, input().split())

counter = 0

while True:
    target = 
    N = (N //K) * K
    counter += N%K
    if N < K:
        break
    N = N // K
    counter += 1

counter += (N-1)
print(counter)