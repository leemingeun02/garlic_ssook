score_total_sum = 0

xsum = 0
number = 20

for i in range(20):
    a = list(map(str, input().split()))
    a[1] = float(a[1])
    if a[2] == 'P':
        continue
    elif a[2] == 'A+':
        pj = 4.5
    elif a[2] == 'A0':
        pj = 4.0
    elif a[2] == 'B+':
        pj = 3.5
    elif a[2] == 'B0':
        pj = 3.0
    elif a[2] == 'C+':
        pj = 2.5
    elif a[2] == 'C0':
        pj = 2.0
    elif a[2] == 'D+':
        pj = 1.5
    elif a[2] == 'D0':
        pj = 1.0
    else:
        pj = 0
    xsum += pj * a[1]
    score_total_sum += a[1]


print(xsum / score_total_sum)
    
