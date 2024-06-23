import sys
input = sys.stdin.readline
N = int(input().rstrip())

person = set()
result = 0
for i in range(N):
    chatting = input().rstrip()
    if chatting=="ENTER":
        result += len(person)
        person=set()
        continue
    person.add(chatting)
result+= len(person)
print(result)