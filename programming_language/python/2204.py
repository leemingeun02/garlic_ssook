import sys
import copy

N = int(sys.stdin.readline())

while N != 0:
    words = [[0] for _ in range(N)]
    words_origin = deepcopy(words)
    for i in range(N):
        words_origin[i] = words[i] = sys.stdin.readline().rstrip().ljust(20)
        words[i] = words[i].upper()
    firstalphabet_origin = firstalphabet = "ZZZZZZZZZZZZZZZZZZZ"
    for i in range(N-1):
        for j in range(20):
            if ord(words[i][j]) > ord(words[i+1][j]):
                firstalphabet = words[i+1]
                firstalphabet_origin = words_origin[i+1]
                break
    print(firstalphabet.strip())
    N = int(sys.stdin.readline())