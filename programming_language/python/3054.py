string = input()

#1번째줄
print(".", end="")
for i in range(1, len(string)+1):
    if i % 3 != 0:
        print(".#..", end="")
    else:
        print(".*..", end="")
print()

#2번째줄
for i in range(1, len(string)+1):
    if i % 3 != 0:
        print(".#.#", end='')
    else:
        print(".*.*", end='')
print(".")
        

#3번째줄
third_string = ''
print("#.{}.".format(string[0]), end='')
for i in range(2, len(string)+1):
    if i % 3 == 0:
        print("*.{}.".format(string[i-1]), end='')
    elif i%3 == 1:
        print("*.{}.".format(string[i-1]), end='')
    else:
        print("#.{}.".format(string[i-1]), end='')       

if len(string) % 3 == 0:
    print("*")
else:
    print("#")


#4번째줄

for i in range(1, len(string)+1):
    if i % 3 != 0:
        print(".#.#", end='')
    else:
        print(".*.*", end='')
print(".")

#5번째줄
print(".", end="")
for i in range(1, len(string)+1):
    if i % 3 != 0:
        print(".#..", end="")
    else:
        print(".*..", end="")
print()