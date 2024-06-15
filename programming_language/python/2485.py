N = int(input())

def max_common(a, b):
    if max(a, b) / min(a, b) == 0:
        return(min(a,b))
    else: r = max(a,b) % min(a,b)
    if a > b:
        a = r
    else:
        b = r

garosu = []
for i in range(N):
    garosu.append(int(input()))
garosu.sort()
gap = set()
for i in range(N-1): #간격을 리스트로
    gap.add(garosu[i+1] - garosu[i])
gap = list(gap).sort()
print(gap)
print(garosu)
result = 
for i in range(len(gap)-1):
    asdf = max_common(gap[i], gap[i+1])
    if result >asdf:
        result = asdf