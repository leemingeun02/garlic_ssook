class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    @staticmethod
    def is_time_valid(abc):
        hour, minute, second = map(int, abc.split(":"))
        if 0<= hour <=24 and 0<= minute <= 59 and 0 <= second <= 60:
            return True
    
    def from_string(abc):
        hour, minute, second = map(int, abc.split(":"))


        







time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')