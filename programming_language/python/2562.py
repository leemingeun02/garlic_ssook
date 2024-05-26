max = 0
maxi = -1
A = [0] * 9
for i in range(9):
    B = int(input())
    A[i] = B
    

for i in A:
    if max < i:
        max = i
        maxi = A.index(i) + 1
print(max)
print(maxi)
# 질문: n개의 값을 차례대로 입력받아 리스트로 저장하는 방법이
# A = list(map(int, input())) 는 9개만을 모두 엔터를 통해 입력받아야 하기 때문에 안되는건가?
#
    