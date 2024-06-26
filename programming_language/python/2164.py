from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

cards = deque([i for i in range(1,N+1)])


while len(cards) !=1:
    cards.popleft()
    cards.append(cards[0])
    cards.popleft()

print(cards[0])