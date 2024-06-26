N, K =map(int, input().split())

people = [i for i in range(0,N+1)]

st = K
print("<",end="")
while len(people) != 2:
    print(people[st],end=" ")
    del people[st+K]
    st = st+K
    st %= len(people)
print(people[-1],">",end="",sep="")