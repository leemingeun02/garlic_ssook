N = int(input)
ARR = list(map(int, input().split()))
operator = list(input().split())
answer_set = set()
def backtracking(n, arr, OPERATOR, string=""):
    if len(string) == N-1: #연산자 조합 완성시 계산후 answer_set에 추가
        answer = arr[0]
        for i in range(N-1):
            if string[i] == "+":
                answer += arr[i+1]
            elif string[i] == "-":
                answer -= arr[i+1]
            elif string[i] == "*":
                answer *= arr[i+1]
            elif string[i] == "/":
                answer //= arr[i+1]
        answer_set.add(answer)
    OPERATOR_LIST = "+"*OPERATOR[0] + "-"*OPERATOR[1] + "*"*OPERATOR[2] + "/"*OPERATOR[3]
    for i in range(N-1): #연산자 조합 미완성 시 조합 만들기
        #연산자의 개수가 있을때 어떻게 조합을 만드는가?
        




backtracking(N, ARR, operator)
print(max(answer_set))
print(min(answer_set))
