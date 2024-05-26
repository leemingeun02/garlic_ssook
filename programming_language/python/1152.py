string = input()
answer = 0

if len(string) == 1:
    if string ==' ':
        answer = 0
    else: answer = 1
if len(string) == 2:
    answer = 1
if not (len(string) == 1 or len(string) == 2):
    for i in range(1, len(string)-1):
        if string[i] == ' ':
            answer = answer + 1
    if answer != 0:
        answer = answer + 1
 
print(answer)