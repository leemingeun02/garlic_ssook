N, M = map(int, input().split(" "))
card = list(map(int, input().split(" ")))

sum_before = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if not(i==k or k == j or j == i):
                sum_after = card[i] + card[j] + card[k]
                if sum_after - M <= 0 and sum_before <sum_after:
                    sum_before = sum_after
print(sum_before)