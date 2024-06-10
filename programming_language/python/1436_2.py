N = int(input())

counter = 0
number = 0
while True:
    number += 1

    if "666" in str(number):
        counter += 1
        if counter == N:
            break
print(number)