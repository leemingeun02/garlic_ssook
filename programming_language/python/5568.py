N = input()
K = input()
answer = set()
cards = [0] * int(N)

for i in range(int(N)):
    cards.append(input())

def backtracking(i = 0, answer_element = []): #k장을뽑아서나열
    global answer
    if i == K:
        string=""
        for j in answer_element:
            string += cards[j]
        answer.add(string)
        return
    for j in range(N):
       backtracking(i+1, answer_element + [j])
backtracking()
print(len(answer))