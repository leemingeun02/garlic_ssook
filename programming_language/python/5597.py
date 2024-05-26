student = []


for i in range(30):
    student.append(i+1)


for i in range(28):
    attendent = int(input())
    for i in range(30):
        if attendent == student[i]:
            student[i] = 0

for i in range(30):
    if student[i] != 0:
        print(student[i], end='\n')
    