N, M = map(int, input().split())

# 최대공약수: 유클리드 호제법

def euclide(N,M):
    if N % M == 0:
        return M
    else:
        return euclide(M, N%M)


euclide_variable = euclide(N,M)
print(euclide_variable)
print(min(N,M)//euclide_variable*max(N,M))