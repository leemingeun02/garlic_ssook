word = input()

reverse_word = word[::-1]

for i in range(len(word)):
    if word[i] == reverse_word[i]:
        output = 1
    else:
        output = 0
        break
print(output)