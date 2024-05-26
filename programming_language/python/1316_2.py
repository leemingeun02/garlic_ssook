N = int(input())
word = input()
output = -1
for j in range(N):
    for i in range(len(word)):
        if word[i] == word[i+1]:
            word[i] = word[i]

