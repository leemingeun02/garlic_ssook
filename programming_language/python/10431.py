import sys
input = sys.stdin.readline
testcase = int(input())


def asdf(target, listssss):
    for i in range(len(listssss)):
        if listssss[i] > target:
            return i
    return 0



for j in range(testcase):
    input_line = list(map(int, input().split()))
    output_line = [input_line[1]]
    answer = 0
    for i in range(2, len(input_line)):
        abc = asdf(input_line[i], output_line)
        if abc == 0:
            output_line.append(input_line[i])
        else:
            output_line.insert(abc, input_line[i])
            answer += len(output_line) - abc - 1
    print(j+1, answer, sep=" ")