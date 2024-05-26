a, b, c = map(int, input().split())
asdf = [a,b,c] #asdf = list(a,b,c)는 왜 안되는데
asdf = sorted(asdf)
print(asdf)

if a+b>c:
    print(asdf[0]+asdf[1]+asdf[2])
else:
    print(asdf[0]+asdf[1]+asdf[1])

