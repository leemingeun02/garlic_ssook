import sys
input = sys.stdin.readline

string = input().rstrip()

extracted = [0,0] #12번째줄때메 0,0그냥넣엇음아무의미없음

while string != ".":
    for i in string:
        if i == "(" or i == ")" or i == "[" or i == "]":
            extracted.append(i)

        if extracted[-1]== ")" and extracted[-2]=="(":
            extracted.pop()
            extracted.pop()
        if extracted[-1]== "]" and extracted[-2]=="[":
            extracted.pop()
            extracted.pop()
    if extracted == [0,0]:
        print("yes")
    else:
        print("no")
    extracted = [0,0]
    string = input().rstrip()