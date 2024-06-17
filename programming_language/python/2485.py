N = int(input())

def euclide(a, b):
    rem = a % b
    if rem == 0:
        return b
    else: return euclide(b, rem)
    

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


#최대 간격 구하기
max_gap = 0
for i in range(len(gap)-1):
    if max_gap < euclide(gap[i+1], gap[i]):
        max_gap = euclide(gap[i+1], gap[i])
print(max_gap)
    