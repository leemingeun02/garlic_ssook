#M이 100억이상일경우
#큰수의 법칙 문제
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

first = data[0]
second = data[1]



repeat = M // (K+1)
remain = M % (K+1)

result = 0
result += (first * K + second) * repeat
result += first * remain

print(result)