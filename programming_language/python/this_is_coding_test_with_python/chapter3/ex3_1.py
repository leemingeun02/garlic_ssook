#거스름돈
#내 코드
N = int(input())

rem500 = N // 500
N = N% 500

rem100 = N // 100
N = N% 100

rem50 = N // 50
N = N%50

rem10 = N//10


print(rem500,rem100,rem50,rem10)


