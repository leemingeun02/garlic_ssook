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



    #sys.stdin.readline 을 할 시에는 rstrip 하는 습관 기를 것
    #pikachu 를 리스트로 만들 필요 없음 >> 공간낭비
    #replace를 "(아무것도없는문자열)"로 바꾸면 좋음
    #replace함수는 처repl음부터 끝까지 찾는 함수이므로
    문자열 개수가 1억개 정도되면 극도로 느려짐.
    try except는 에러가 나올시를 가정하므로 알고리즘 문제 풀이에서는
지양하는것이 좋음.
