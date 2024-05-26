grade_list = list(map(int, input().split()))
sorted_list = list(reversed(sorted(grade_list)))
score = int(input())

ranking = sorted_list.index(score) + 1

if 1<= ranking <= 5:
    print("A+")
elif 6 <= ranking <= 15:
    print("A0")
elif 16 <= ranking <= 30:
    print("B+")
elif 31 <= ranking <= 35:
    print("B0")
elif 36 <= ranking <= 45:
    print("C+")
elif 46 <= ranking <= 48:
    print("C0")
else:
    print("F")
 