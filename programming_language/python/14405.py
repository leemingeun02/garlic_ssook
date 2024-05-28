import sys
input = sys.stdin.readline


pikachu = ["pi", "ka", "chu"]

S = input()

S = S.replace("pi", "1")
S = S.replace("ka", "2")
S = S.replace("chu","3")


try:
    if int(S) > 0:
        print("YES")
except:
    print("NO")