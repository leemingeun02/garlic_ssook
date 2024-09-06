start_time, end_time = input().split()
start_h, start_m = map(int, start_time.split(":"))
end_h, end_m = map(int, end_time.split(":"))


#택배기사의 하루 업무 총시간 구하기
if end_m > start_m:
    one_day_total_m = end_m - start_m
    one_day_total_h = end_h - start_h
else:
    one_day_total_m = end_m - start_m + 60
    one_day_total_h = end_h - start_h - 1

one_day_total_minute = one_day_total_m + one_day_total_h * 60


#입력받기
N, T = map(int, input().split())

#몇일뒤 도착하는가?
if one_day_total_minute % T == 0:
    one_day_delivery_amount = (one_day_total_minute // T) - 1
else:
    one_day_delivery_amount = (one_day_total_minute // T)
print(N // one_day_delivery_amount)


#몇시 몇분에 도착하는가?
answer_m = (((N+1 - (one_day_delivery_amount)*(N // one_day_delivery_amount))*T)% one_day_total_minute)%60
answer_h = (((N+1 - (one_day_delivery_amount)*(N // one_day_delivery_amount))*T)% one_day_total_minute)//60

answer_m += start_m
answer_h += start_h
if answer_m >= 60:
    answer_m -= 60
    answer_h += 1



answer_h = "{:02}".format(answer_h)
answer_m = "{:02}".format(answer_m)
print(answer_h,answer_m,sep=":") 