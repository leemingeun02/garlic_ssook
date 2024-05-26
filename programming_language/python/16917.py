A,B,C,X,Y = map(int, input().split(" "))

# 반반 필요없는 경우
if 2 * C  >= A + B:
        print(A*X + B*Y)

# 반반만 사야하는경우
elif A>2*C and B> 2*C:
    if X > Y:
        print(C*2*X)
    else:
        print(C*2*Y)
    
# 반반도 사야하는경우
else:
    if 2 * C < A+B and (C < A and C < B):
        if X >= Y:
            print(C*2*Y + A*(X-Y))
        else:
            print(C*2*X + B*(Y-X))
    else:
        pass