youngsik = [['' for j in range(15)] for i in range(5)]
print(youngsik)

for i in range(5):
    youngsik[i]= input()
print(youngsik)

#C언어 > 문자열의 맨 마지막에 마이너스 1
answer = ''
for i in range(15):
    for j in range(5):
        if youngsik[j][i] != -1:
            answer = answer + youngsik[j][i]
            print(answer)