word = input()

c_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in c_word:
    if i in word:
        word = word.replace(i, '?')
print(len(word))