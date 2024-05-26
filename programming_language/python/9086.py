word = input()
answer = 0
dial_number = -1
for i in word:
    if i == 'A' or i == 'B' or i == 'C':
        dialnumber = 2
        answer += dialnumber + 1
    if i == 'D' or i == 'E' or i == 'F':
        dialnumber = 3
        answer += dialnumber + 1  
    if i == 'G' or i == 'H' or i == 'I':
        dialnumber = 4        
        answer += dialnumber + 1
    if i == 'J' or i == 'K' or i == 'L':
        dialnumber = 5
        answer += dialnumber + 1
    if i == 'M' or i == 'N' or i == 'O':
        dialnumber = 6
        answer += dialnumber + 1
    if i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        dialnumber = 7
        answer += dialnumber + 1
    if i == 'T' or i == 'U' or i == 'V':
        dialnumber = 8
        answer += dialnumber + 1
    if i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        dialnumber = 9
        answer += dialnumber + 1

print(answer)
