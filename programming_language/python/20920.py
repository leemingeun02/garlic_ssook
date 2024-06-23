N, M = map(int, input().split())
words=list()
for i in range(N):
    A = input()
    if len(A)>=M:
        words.append(A)

data = dict()

final_words = list()