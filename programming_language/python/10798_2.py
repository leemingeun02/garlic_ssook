writing = [input() for i in range(5)]

for i in range(15):
    for j in range(5):
        if len(writing[j])>=1+i:
            print(writing[j][i], end="")