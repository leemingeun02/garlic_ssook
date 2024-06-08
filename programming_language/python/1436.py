N = int(input())

counter = 0
number = 0
while counter != N:
    number += 1

    if str(number).count("666") >= 1:
        counter += 1
print(number)
    