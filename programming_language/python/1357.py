A, B = map(str, input().split(" "))

A = list(A)
A.reverse()
A=int(''.join(A))

B = list(B)
B.reverse()
B= int(''.join(B))

C = A + B
C = str(C)
C = list(C)
C.reverse()
C = int(''.join(C))

print(C)
