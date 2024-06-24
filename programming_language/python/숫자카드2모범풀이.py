import sys
input = sys.stdin.readline
N = int(input())
cards = [0] * 20000001

for card in set(map(int,input().split())):
    cards[card+10000000] = 1

M = int(input())

for card in map(int, input().split()):
    print(cards[card+10000000],end=' ')