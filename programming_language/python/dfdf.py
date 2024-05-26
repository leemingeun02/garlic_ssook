a, b = map(int, input().split())

list23 = [list(input()) for i in range(b)]

move = [(0,1), (0,-1), (1,1),(1,-1), (-1,1), (-1,-1), (1,0),(-1,0)]

for j in range(b):
    for i in range(a):
        if list23[j][i] == "*":
            print("*", end='')
        else:
            total = 0
            for mv_r, mv_c in move:
                new_r, new_c = i + mv_r, j + mv_c
                if (0 <= new_r < a)  and (0<= new_c < b) and (list23[new_c][new_r] == "*"):
                    total += 1
            print(total, end='')
    print()