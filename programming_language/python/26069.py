import sys
input = sys.stdin.readline
N = int(input())

dancing_people = set()
dancing_people.add("ChongChong")
for i in range(N):
    people= list(map(str, input().split()))
    for j in dancing_people:
        if j in people:
            dancing_people.add(people[0])
            dancing_people.add(people[1])
            break

print(len(dancing_people))