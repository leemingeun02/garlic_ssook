N = int(input())

seats = input()
seats2 = seats
seats = seats.replace("S", "*S")
seats = seats.replace("LL", "*LL") + "*"

seats = seats.replace("*LL*", "")
seats = seats.replace("*L", "")
seats = seats.replace("L*", "")
seats = seats.replace("*S", "")
seats = seats.replace("S*", "")
seats = seats.replace("*", "")

print(len(seats2) - len(seats))