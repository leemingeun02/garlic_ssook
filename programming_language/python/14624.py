N = int(input())
GROUP = [list(map(int, input().split(" "))) for i in range(9)]
maxvalue = 0
asdf = {1:'PROBRAIN', 2: 'GROW', 3: 'ARGOS', 4: 'ADMIN', 5: 'ANT', 6: 'MOTION', 7: 'SPG', 8: 'COMON', 9: 'ALMIGHTY'}
for i in range(9):
    if maxvalue < max(GROUP[i]):
        maxvalue = max(GROUP[i])
        CANDIDATE = i

print(asdf[CANDIDATE+1])