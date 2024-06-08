writings = [[" " for _ in range(15)] for _ in range(5)]
writings2 = [0 for i in range(5)]

for i in range(5):
    writings2[i] = input()


for i in range(5):
    for j in range(15):
        try:
            writings[i][j] = writings2[i][j]
        except:
            pass


for j in range(15):
    for i in range(5):
        if writings[i][j] != " ":
            print(writings[i][j], end="")