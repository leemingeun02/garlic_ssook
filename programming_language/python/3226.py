N = int(input())

fee = 0

for i in range(N):
    string = input()
    string = string.replace(" ", ":")
    hour, minute, during = map(int, string.split(":"))




    f_minute = (minute + during) % 60
    adder = (minute + during) // 60
    f_hour = (hour + adder) % 24     #during이 최대 육십이므로 하루지나도상관없음

    if f_hour == hour:
        if 7<= hour < 19:
            fee += during * 10
        else:
            fee += during * 5
    else:
        if f_hour == 7:
            fee += f_minute * 10 + (60 - minute) * 5
        elif f_hour == 19:
            fee += f_minute * 5 + (60 - minute) * 10
        else:
            if 7< f_hour < 19:
                fee += during * 10
            else:
                fee += during * 5

print(fee)