A, B = map(int, input().split())
A1 = A
B1 = B

#최대공약수 구하기
while True:
    if max(A, B) % min(A, B) == 0:
        max_common = min(A, B)
        break
    else: R = max(A, B) % min(A, B)
    if A> B:
        A = R
    else:
        B = R

print(A1* B1 // max_common)