N, K = map(int, input().split(' '))
suyeol = list(map(int, input().split(',')))
suyeol2 = suyeol
if K == 0:
    print(*suyeol, sep=',')
else:
    for i in range(K):
        new_l = [suyeol2[i+1]-suyeol2[i] for i in range(len(suyeol2)-1)]
        suyeol2 = new_l
    print(*new_l, sep = ',')