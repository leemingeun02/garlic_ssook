import sys

input = sys.stdin.readline

N = int(input())

#최대공약수 함수정의
def euclide(a, b):
    rem = a % b
    if rem == 0:
        return b
    else: return euclide(b, rem)
    
#심어져 있던 가로수
garosu = []
for i in range(N):
    garosu.append(int(input()))

#간격을 집합으로 만들고 리스트로 변경
gap = set()
for i in range(N-1):
    gap.add(garosu[i+1] - garosu[i])
gap = sorted(list(gap))

#최대 간격 구하기
max_gap = 0
for i in range(len(gap)-1):
    asdf = euclide(gap[i+1], gap[i])
    if max_gap < asdf:
        max_gap = asdf

if max_gap = 0z

#답 구하기
total_garosu_number = (garosu[-1] - garosu[0])//max_gap + 1

print(total_garosu_number - N)