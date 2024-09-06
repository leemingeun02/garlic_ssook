import sys
input = sys.stdin.readline


asdf = 0
N = int(input())

menu_sticker_whether = [0] * (N+1)
max_sticker_number = 0

menu = list(map(int, input().split()))

for i in range(len(menu)):
    if menu_sticker_whether[menu[i]] == 0:
        menu_sticker_whether[menu[i]] = 1
        asdf+= 1
    else:
        menu_sticker_whether[menu[i]] = 0
        asdf-= 1
    if asdf > max_sticker_number:
        max_sticker_number = asdf
print(max_sticker_number)