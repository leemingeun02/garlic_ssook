N, K = map(int,input().split())

def factorial(a):
    if a >= 2:
        return a * factorial(a-1)
    
print(factorial(3))

print(factorial(N)/factorial(N-K)*factorial(K))