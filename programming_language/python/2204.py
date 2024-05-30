N = int(input())
words = []

while N != 0:
    for i in range(N):
        words.append(input())
    print(words)
    N = int(input())