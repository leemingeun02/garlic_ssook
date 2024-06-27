import sys
input = sys.stdin.readline

string = input().rstrip()

while string != "0":
    answer = "yes"
    for i in range(len(string)//2 + 1):
        if string[i] != string[-(i+1)]:
            answer = "no"
            break
    string = input().rstrip()

    print(answer)