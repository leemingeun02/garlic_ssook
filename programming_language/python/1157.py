word = input().upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabet2 = [0] * len(alphabet)
MAX = -1
answer = ''

for i in range(len(word)):
    for j in range(len(alphabet)):
        if word[i] == alphabet[j]:
            alphabet2[j] += 1

for i in range(len(alphabet)):
    if alphabet2[i] > MAX:
        MAX = alphabet2[i]
        answer = alphabet[i]

count = 0
for i in range(len(alphabet)):
    if MAX == alphabet2[i]:
        count = count + 1


if count == 1:
    print(answer)
else:
    print("?")